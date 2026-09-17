for i in range(1,10):
    if i == 5:
        break
    print(i)

marks = [10,20,30,40]
total = 0
for i in marks:
    total += i
print(total)    

num = [1,2,3,4,5,6]

for i in num:
    if i % 2 == 0:
        print(i)

numbers = [1,2,3,4,5,6]

for i in numbers:
    if i % 2 != 0:
        print(i)

numbers = [1,2,3,4,5,6]

for i in numbers:
    if i % 2 == 0:
        print(i , "Even")
    else:
        print(i, "Odd")    
users = ["John","Doe","Shs"]

for i in users:
    if i == "John":
        print("User found !")
        break
    print("Users",users)    

# Cpntinue 

for i in range(1,6):
    if i == 3:
        continue
    print(i)


 