# Shallow Copy
# A shallow copy creates a new outer object.

# in shallow copy it will change the original array also 

a = [10,20,30,40]

b = a.copy()

b.append(50)

print(a)
print(b)



# Method Slicing 
num = [10,20,30]

c = num[:]

c.append(40)

print(num)
print(c)



