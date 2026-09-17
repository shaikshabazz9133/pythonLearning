#  slicing is used to extract the porition of sequence
# slicing works with 
# list , tuple , String , OtherSequence

# sequenc[start:stop:step]. ------------ Syntax

# Example1  

name = "Shabazz"

print(name[0:4])

#  we can write like this below also 
print(name[:4]) # it will automaticall convert to [0:4]

print(name[2:]) # start with 2 index and there is no stop so it will execute all

print(name[1:4]) # here i have added the start and end so it will get hab output

# Negative Step
# You can slice backwards.
numbers = [10,20,30,40,50]

print(numbers[::-1])

# reverse string

name = "Python"

print(name[::-1])

name = "Sir"

if name == name[::-1]:
    print('it is a palindrome')
else:
    print('it is not a palindrome')

# Slicing List

numbers = [10,20,30,40]

print(numbers[1:2])

#  Slicing Tuples
num = (10,20,30,40,50,60,70,80)

print(num[2:5:2])

# Important Slicing 
number = [0,1,2,3,4,5,6,7,8,9]

print(number[:2])
print(number[1:])
print(number[2:5])
print(number[::-1])
print(number[::-2])




t = [1,2,3,['hello','hi']]
a = t[3]

# i have to a use the tuple and list with slicing to get the value
