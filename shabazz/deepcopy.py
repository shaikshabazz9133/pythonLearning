# Deep Copy

# Deep copy creates an independent copy of nested objects as well.

# Use the copy module.

# import copy

# a = [
#     [1,2],
#     [3,4]
#     ]
# b = copy.deepcopy(a)
# b[0].append(10)

# print(a)
# print(b)

# it wil not chnage the original array it will change that particular varibale array only what we have created with the name of deep


import copy

orginal = [[1,2],[3,4]]

deep =copy.deepcopy(orginal)
deep[0].append(50)

print(orginal)
print(deep)


# List Slicing

number = [10,20,30,40]

d = list(number)
d.append(50)
print(number)
print(d)
