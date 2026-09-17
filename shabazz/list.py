# numbers = [10,20,30,40]

# print(numbers[0])

# # numbers[0] = 100

# print(numbers.append(50))
# print(numbers)

# Append 

fruits = ["apple","banana"]

fruits.append("orange") # append the data like added the one more data in end of the list 
print(fruits)

# Extend add multiple items in end of the list 

num = [1,2,3]

num.extend([4,5])
print(num)

# insert add the item in specific position

# syntax : list.insert(index,value)

fruit = ["apple","banana"]
fruit.insert(1,"orange") 
fruit.remove('banana') #remove the item in the list (it remove the value not index)
print(fruit)

# pop is used to remove and return the item 

numbe = [1,2,3,4]

result = numbe.pop() # it remove the last element default

print(numbe)
print(result)

# clear 
num1 = [1,2,3] 
num1.clear()
print(num1)

# index is used find the index of the element

num2 = ["apple","banana","orange"]

result = num2.index('banana')
print(result)

# count it check the particular how many times appear in list
num3 = [1,2,3,4,1,5,1]

print(num3.count(1))

# Sort the list 
num4 = [1,4,2,5,7,8,3]

num4.sort()
print(num4)

num4.sort(reverse = True)

print(num4)

# Reverse the list or item 

num5 = [10,20,30,40]

num5.reverse()

print(num5)

# Copy means it create the shallow copy like it create the new variable and store the data
num6 = [10,20,30,40]

new_num = num6.copy()
new_num.append(50)

print(num6)
print(new_num)