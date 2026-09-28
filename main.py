"""To-Do API: FastAPI + SQLite (stdlib only, no ORM)."""
import os
import sqlite3
from datetime import date, datetime, timezone
from typing import Iterator, Literal

from fastapi import Depends, FastAPI, HTTPException, Query, Response
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="To-Do API", version="2.0")

SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT    NOT NULL,
    description  TEXT,
    done         INTEGER NOT NULL DEFAULT 0,
    priority     INTEGER NOT NULL DEFAULT 1,
    due_date     TEXT,
    created_at   TEXT    NOT NULL,
    updated_at   TEXT    NOT NULL,
    completed_at TEXT
)
"""


# ---------- Database ----------
def get_db() -> Iterator[sqlite3.Connection]:
    """One connection per request. Path is read from TODO_DB at call time."""
    conn = sqlite3.connect(os.environ.get("TODO_DB", "todo.db"), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute(SCHEMA)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


DB = Depends(get_db)


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------- Models ----------
def _clean_title(value: str) -> str:
    value = value.strip()
    if not value:
        raise ValueError("Title cannot be just whitespace")
    return value


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    done: bool = False
    priority: int = Field(default=1, ge=1, le=5)
    due_date: date | None = None

    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str) -> str:
        return _clean_title(v)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    """All fields optional, for PATCH."""
    title: str | None = Field(default=None, min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=1000)
    done: bool | None = None
    priority: int | None = Field(default=None, ge=1, le=5)
    due_date: date | None = None

    @field_validator("title")
    @classmethod
    def clean_title(cls, v: str | None) -> str | None:
        return v if v is None else _clean_title(v)


class TaskOut(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    completed_at: datetime | None = None


class Stats(BaseModel):
    total: int
    done: int
    pending: int
    overdue: int
    by_priority: dict[int, int]


# ---------- Helpers ----------
def get_or_404(db: sqlite3.Connection, task_id: int) -> sqlite3.Row:
    row = db.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return row


def to_out(row: sqlite3.Row) -> TaskOut:
    data = dict(row)
    data["done"] = bool(data["done"])
    return TaskOut(**data)


def db_value(key: str, value):
    if isinstance(value, date):
        return value.isoformat()
    if key == "done":
        return int(value)
    return value


# ---------- Routes ----------
@app.get("/")
def home():
    return {"message": "Welcome to your To-Do API!"}


SortField = Literal["id", "title", "priority", "due_date", "created_at"]


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(
    response: Response,
    db: sqlite3.Connection = DB,
    done: bool | None = None,
    priority: int | None = Query(None, ge=1, le=5),
    q: str | None = Query(None, min_length=1, description="Search title/description"),
    overdue: bool = False,
    sort_by: SortField = "id",
    order: Literal["asc", "desc"] = "asc",
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
):
    where, params = [], []
    if done is not None:
        where.append("done = ?")
        params.append(int(done))
    if priority is not None:
        where.append("priority = ?")
        params.append(priority)
    if q:
        where.append("(title LIKE ? OR description LIKE ?)")
        params += [f"%{q}%", f"%{q}%"]
    if overdue:
        where.append("done = 0 AND due_date IS NOT NULL AND due_date < ?")
        params.append(date.today().isoformat())

    clause = f"WHERE {' AND '.join(where)}" if where else ""
    total = db.execute(f"SELECT COUNT(*) FROM tasks {clause}", params).fetchone()[0]

    # sort_by/order are validated Literals, so interpolating them is safe.
    if sort_by == "due_date":  # tasks without a due date always go last
        order_sql = f"due_date IS NULL, due_date {order}, id ASC"
    else:
        order_sql = f"{sort_by} {order}, id ASC"

    rows = db.execute(
        f"SELECT * FROM tasks {clause} ORDER BY {order_sql} LIMIT ? OFFSET ?",
        [*params, limit, offset],
    ).fetchall()

    response.headers["X-Total-Count"] = str(total)
    return [to_out(r) for r in rows]


@app.get("/tasks/stats", response_model=Stats)
def task_stats(db: sqlite3.Connection = DB):
    total, done = db.execute("SELECT COUNT(*), COALESCE(SUM(done), 0) FROM tasks").fetchone()
    overdue = db.execute(
        "SELECT COUNT(*) FROM tasks WHERE done = 0 AND due_date IS NOT NULL AND due_date < ?",
        (date.today().isoformat(),),
    ).fetchone()[0]
    by_priority = {
        r["priority"]: r["n"]
        for r in db.execute("SELECT priority, COUNT(*) AS n FROM tasks GROUP BY priority")
    }
    return Stats(total=total, done=done, pending=total - done, overdue=overdue, by_priority=by_priority)


@app.delete("/tasks/completed")
def clear_completed(db: sqlite3.Connection = DB):
    deleted = db.execute("DELETE FROM tasks WHERE done = 1").rowcount
    return {"message": "Completed tasks cleared", "deleted": deleted}


@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: sqlite3.Connection = DB):
    return to_out(get_or_404(db, task_id))


@app.post("/tasks", response_model=TaskOut, status_code=201)
def add_task(task: TaskCreate, db: sqlite3.Connection = DB):
    ts = now()
    cur = db.execute(
        """INSERT INTO tasks (title, description, done, priority, due_date,
                              created_at, updated_at, completed_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            task.title, task.description, int(task.done), task.priority,
            task.due_date.isoformat() if task.due_date else None,
            ts, ts, ts if task.done else None,
        ),
    )
    return to_out(get_or_404(db, cur.lastrowid))


@app.put("/tasks/{task_id}", response_model=TaskOut)
def replace_task(task_id: int, task: TaskCreate, db: sqlite3.Connection = DB):
    existing = get_or_404(db, task_id)
    ts = now()
    completed_at = (existing["completed_at"] or ts) if task.done else None
    db.execute(
        """UPDATE tasks SET title=?, description=?, done=?, priority=?, due_date=?,
                            updated_at=?, completed_at=? WHERE id=?""",
        (
            task.title, task.description, int(task.done), task.priority,
            task.due_date.isoformat() if task.due_date else None,
            ts, completed_at, task_id,
        ),
    )
    return to_out(get_or_404(db, task_id))


@app.patch("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, changes: TaskUpdate, db: sqlite3.Connection = DB):
    existing = get_or_404(db, task_id)
    data = changes.model_dump(exclude_unset=True)

    for field in ("title", "done", "priority"):
        if field in data and data[field] is None:
            raise HTTPException(status_code=422, detail=f"'{field}' cannot be null")
    if not data:
        return to_out(existing)

    ts = now()
    if "done" in data:
        data["completed_at"] = (existing["completed_at"] or ts) if data["done"] else None
    data["updated_at"] = ts

    assignments = ", ".join(f"{k} = ?" for k in data)  # keys come from the model, not the client
    db.execute(
        f"UPDATE tasks SET {assignments} WHERE id = ?",
        [*(db_value(k, v) for k, v in data.items()), task_id],
    )
    return to_out(get_or_404(db, task_id))


@app.post("/tasks/{task_id}/complete", response_model=TaskOut)
def complete_task(task_id: int, db: sqlite3.Connection = DB):
    get_or_404(db, task_id)
    ts = now()
    db.execute(
        "UPDATE tasks SET done = 1, completed_at = COALESCE(completed_at, ?), updated_at = ? WHERE id = ?",
        (ts, ts, task_id),
    )
    return to_out(get_or_404(db, task_id))


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: sqlite3.Connection = DB):
    get_or_404(db, task_id)
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))