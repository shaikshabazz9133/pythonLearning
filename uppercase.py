s = input("Enter a string: ")
r = ""

for c in s:
    if c.isupper():
        r += c

print(r)