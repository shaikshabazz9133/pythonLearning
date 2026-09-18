"""
my_list=[1,2,3,4]
empty=[]
mixed=[1,"hello",3.14,True]
nested=[1,[2,3],[4,5,6]]

#Accessing Elements
fruits=["apple","banana","cherry","date"]
print(fruits[0]) #apple
print(fruits[-1])#date

# inbuilt methods
# append():
fruits = ["apple", "banana", "cherry", "date"]
# it will add the value at last of the listand only value is taken.
fruits.append("orange")
fruits.append("kiwi")
print(fruits)
"""
# 2.Insert():
# fruits = ["apple", "banana", "cherry", "date"]
# fruits.insert(2, "mango")#it is used to add a value i the specified index position.
# Print(fruits)

# Extend():
# fruits = ["apple", "banana", "cherry", "date"]
# fruits.extend(["watermelon"])
# fruits.extend("watermelon", "mango")
# here the extends keyword takes only one argument and if you want to add two arguments the you need to use a list[]
# TypeError: list.extend() takes exactly one argument (2 given)
# print(fruits)

# remove():
# fruits = ["apple", "banana", "cherry", "date"]
# fruits.remove("apple")# this is used to remove the element from the list
# print(fruits)

# pop():
# fruits = ["apple", "banana", "cherry", "date"]
# fruits.pop(2)
# print(fruits)
