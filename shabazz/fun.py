def sum(a,b):
    return a + b
result = sum(2,3)
print(result)

def greet(name):
    print(f"Hello {name}")
greet("Shabazz")

# Args allows a function to accept any number of positional arguments.
# Args --> means Arguments
# * --> collect multiple arguments
# args is stored in tuple
def add(*args):
    total = 0
    for i in args:
        total += i
    return total
print(add(10,20))
print(add(10,20,30))

# **kwargs allows a function to accept any number of keyword arguments.
# kwargs is stored in dictonary

def student(**kwrgs):
    print(kwrgs)

print(student(name= "Shabazz",age=24,course="BSC"))   

# *args and **kwargs 

def test(*products,**customers):
    print("product", products)
    print("customer", customers)

print(test(
    "Mouse",
    "keyboard",
    "laptop",
    name = "John",
    city="Banglore"
))




