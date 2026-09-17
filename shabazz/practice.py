# Variables
name = "shabazz"
print(name)
# Data Type
age = 25
name = "shabazz"
course = "BSC"

print(type(name))

# Type Casting
name = int(input("Enter your age : "))

print(name)


# Check the == and is 

a = [1,2,3]

b = [1,2,3]

print(a == b)
print(a is b)

# Mutable List
# list is used to store the data in the particular variable we can change the data after create the list

number = [1,2,3,4,5]

number.append(6)
number[0] = 8

print(number)

# Immutable tuple is used to store the data in particular varibale but we can't change the data after create the tuple
numbers = (1,2,3,4)

print(numbers[0])

# Set is us used to set the unordered the unique values

num = {1,3,2,4,5,4}

print(num)

# Dictonary is used to to store the values in key and value pair

student = {
    "name": "shabaz",
    "age":24,
    "course":"BSC"
}


student["salary"] = 15000 
student["name"] = "John"

print(student)

# Conditional statement is used to make a decision 

age = 17

if age >= 18:
    print("Eligible to vote")
else:
    print("age is not match")

marks = 75

if marks >= 65:
    print("A+")
elif marks >= 60:
    print("A")
elif marks >= 50:
    print("C")
else:
    print("Fail")           

# For loop is used to run the condition continously

numbers = [10,20,30]

for i in numbers:
    print(i)

for i in range(1,11):
    print(i)    

for i in range(1,11,3):
    print(i)

for i in range(10,0,-1):
    print(i)
name = "Python"
for i in name:
    print(i)


