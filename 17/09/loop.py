# for i in range(2,20):
#     print(i)

# sum of 2 even numbers

# total =0
# for i in range(2,101):
#     if i % 2 == 0:
        
#         total += i  
# print(total)

# multiplication of table

# num = 2

# for i in range(1,11):
#     print(num, "X", i, "=", num *i)

# for num in range(2,11):
#     print("Table num", num)

#     for i in range(1,11):
#         print(f"{num} X {i} = {num * i}")  
# 
#   Count how many even and odd numbers exist

# even =0
# odd = 0

# for i in range(1,21):
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1   

# print(even)
# print(odd)

# Find the largest number

num = [10,20,43,67,80]
largest = 0

for i in num:
    if i > largest:
        largest = i

print(largest)    

number = [10,23,45,56,78]
largest_num = 0
second_largest = 0
i=1

while i < len(number):
    if number[i] > largest_num:
        second_largest = largest_num
        largest_num = number[i]
    elif number[i] > second_largest and number[i] != largest_num:
        second_largest = number[i]
    i += 1    
    
print("largest",largest_num)    
print("SECOND",second_largest)    



