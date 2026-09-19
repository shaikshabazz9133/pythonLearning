n = [1, 2, 3, 4, 5]

n.append(6)
print(n)

n.insert(2, 10)
print(n)

n.remove(3)
print(n)

n.pop()
print(n)

n.sort()
print(n)

n.reverse()
print(n)

t = (10, 20, 30, 20)

print(t.count(20))
print(t.index(30))

s = {1, 2, 3}

s.add(4)
s.remove(2)

print(s)

d = {"name": "Sam", "age": 20}

d["city"] = "Delhi"
d["age"] = 21

print(d)
print(d["name"])