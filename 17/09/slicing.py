# Slicing means taking a portion of a sequence.
num = [1,2,3,4,5,6,7,8,9]

# print(num[3:])
# print(num[2:6])
# print(num[:7])
# print(num[1:6:2])
# print(num[:-1])
# print(num[-2])
# print(num[-5:-2])

# text = "python"
# print(text[::-1])

# text1 = "python programming"

# print(text1[4:8])

# name = "sir"

# if name == name[::-1]:
#     print("it is a palindrom")
# else:
#     print("it is not palindrome") 

# a = [10,20,30]

# b = a[:]

# print(b)

# tuple slicing

a =(1,2,3,4,5)

print(a[1:4])

student = {
    "name": "Shabazz",
    "age": 25,
    "city": "Bangalore",
    "role": "Developer"
}

keys = list(student.keys())

print(keys[0:2])

numb = [1,2,3,4,5,6,7,8,9]

print(numb[::-2])

# Does slicing modify the original list?
# No 