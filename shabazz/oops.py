# Class is a tempelate/blueprint we can call for creating the object

# class obj:
#     name = "sha"
#     age = 25

# Constructor 
# __init__ is called when object is created

# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# students1 = student("shabazz",26)

# print(students1.name)
# print(students1.age)
        
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

emp1 = Employee("john",25,10000)
emp2 = Employee("doe",26,15000)

print(emp1.name)
print(emp2.name)

name ="shabazz"
age =25

print(list(name))

age = "25"       # string
age = int(age)   # string → integer

print(age)
print(type(age))

async def fun():
    print("Hello")

a = [1,2,3]
b = a

print(a == b)
print(a is b)