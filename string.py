l = [10, "madam", "python", 20, "level", "hello", "radar"]
r = []

for i in l:
    if type(i) == str and i == i[::-1]:
        r.append(i)

print(r)