# What is Type Casting?

# Type casting means converting one data type into another data type.

# String → Integer
# Integer → String
# Float → Integer
# Integer → Float

# Implicit Type Conversion
# python automaticaly converts the one data type to another data type without you 
# explicity telling python to do it 
a = 20
b = 15.6

print(type(a + b))

# Explicit  we have to say to python convert the data into any type 

# int()
# float()
# str()
# bool()
# list()
# tuple()
# set()
# dict()

# convert to int
a = "20"
result = int(a)
print(result)
print(type(result))

# convert to string

num = 10
result = str(num)
print(result)
print(type(result))

flot = "54.56"
result = float(flot)

print(result)
print(type(result))

print(bool(1))
print(bool(0))

# List 
name = "Python"

print(list(name))

# Tuple
tupl = (10,20,30)
print(tuple(tupl))

# Set 
num = {1,2,3,1}
print(set(num))

# Important Type Casting Example
age = int(input("Enter your age : "))
print(type(age))