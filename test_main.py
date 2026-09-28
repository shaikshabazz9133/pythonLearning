from datetime import date, timedelta

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("TODO_DB", str(tmp_path / "test.db"))
    return TestClient(app)


def make(client, **kw):
    kw.setdefault("title", "Task")
    r = client.post("/tasks", json=kw)
    assert r.status_code == 201, r.text
    return r.json()


def test_create_and_get(client):
    t = make(client, title="  Buy milk  ", priority=3)
    assert t["title"] == "Buy milk"
    assert t["created_at"] and t["completed_at"] is None
    assert client.get(f"/tasks/{t['id']}").json()["priority"] == 3


@pytest.mark.parametrize("bad", [{"title": "   "}, {"title": ""}, {"title": "x", "priority": 9}])
def test_validation(client, bad):
    assert client.post("/tasks", json=bad).status_code == 422


def test_404s(client):
    assert client.get("/tasks/99").status_code == 404
    assert client.patch("/tasks/99", json={"done": True}).status_code == 404
    assert client.delete("/tasks/99").status_code == 404
    assert client.post("/tasks/99/complete").status_code == 404


def test_patch_only_changes_sent_fields(client):
    t = make(client, title="A", priority=2)
    r = client.patch(f"/tasks/{t['id']}", json={"done": True}).json()
    assert r["done"] and r["title"] == "A" and r["priority"] == 2
    assert r["completed_at"] is not None
    r = client.patch(f"/tasks/{t['id']}", json={"done": False}).json()
    assert r["completed_at"] is None


def test_patch_rejects_null_title(client):
    t = make(client)
    assert client.patch(f"/tasks/{t['id']}", json={"title": None}).status_code == 422


def test_put_replaces(client):
    t = make(client, title="Old", description="keep?")
    r = client.put(f"/tasks/{t['id']}", json={"title": "New"}).json()
    assert r["title"] == "New" and r["description"] is None


def test_complete_and_delete(client):
    t = make(client)
    assert client.post(f"/tasks/{t['id']}/complete").json()["done"] is True
    assert client.delete(f"/tasks/{t['id']}").status_code == 204
    assert client.get(f"/tasks/{t['id']}").status_code == 404


def test_filter_search_sort_paginate(client):
    make(client, title="Write report", priority=3)
    make(client, title="Buy milk", priority=1, done=True)
    make(client, title="Report bug", priority=5, description="urgent")
    assert len(client.get("/tasks?done=true").json()) == 1
    assert len(client.get("/tasks?priority=5").json()) == 1
    assert {t["title"] for t in client.get("/tasks?q=report").json()} == {"Write report", "Report bug"}
    assert len(client.get("/tasks?q=urgent").json()) == 1

    r = client.get("/tasks?sort_by=priority&order=desc")
    assert [t["priority"] for t in r.json()] == [5, 3, 1]

    r = client.get("/tasks?limit=2&offset=0")
    assert len(r.json()) == 2 and r.headers["X-Total-Count"] == "3"
    assert len(client.get("/tasks?limit=2&offset=2").json()) == 1
    assert client.get("/tasks?sort_by=bogus").status_code == 422


def test_due_date_sorting_puts_nulls_last(client):
    make(client, title="none")
    make(client, title="later", due_date=str(date.today() + timedelta(days=5)))
    make(client, title="soon", due_date=str(date.today() + timedelta(days=1)))
    titles = [t["title"] for t in client.get("/tasks?sort_by=due_date").json()]
    assert titles == ["soon", "later", "none"]


def test_overdue_and_stats(client):
    make(client, title="late", due_date=str(date.today() - timedelta(days=2)))
    make(client, title="late but done", done=True, due_date=str(date.today() - timedelta(days=2)))
    make(client, title="future", due_date=str(date.today() + timedelta(days=2)), priority=4)
    assert [t["title"] for t in client.get("/tasks?overdue=true").json()] == ["late"]
    s = client.get("/tasks/stats").json()
    assert s["total"] == 3 and s["done"] == 1 and s["pending"] == 2 and s["overdue"] == 1
    assert s["by_priority"] == {"1": 2, "4": 1}


def test_clear_completed(client):
    make(client, done=True)
    make(client, done=True)
    keep = make(client)
    assert client.delete("/tasks/completed").json()["deleted"] == 2
    assert [t["id"] for t in client.get("/tasks").json()] == [keep["id"]]