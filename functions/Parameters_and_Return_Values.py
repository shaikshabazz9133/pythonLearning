# 1.Write a function area_rectangle(length, width) that returns the area of a rectangle.
# def area_rectangle(length,width):
#     area = length*width
#     return area
# print(f"The area of rectangle is {area_rectangle(20,30)}")

# 2.Write a function area_circle(radius) that returns the area of a circle.
# def area_circle(radius):
#     pie = 3.14
#     area = pie*radius**2
#     return area
# print(f"Area of circle for the given values is {area_circle(5)}")

# 3.Write a function average(a, b, c) that returns the average of three numbers.
# def average(a,b,c):
#     total = a+b+c
#     return total/3
# print(f"average = {average(3,4,7)}")

# 4.Write a function calculate_bill(price, quantity) that returns the total bill.
# def calculate_bill(price,quantity):
#     return price*quantity
# print(f"Total bill is {calculate_bill(250,3)}")

# # 5.Write a function convert_temperature(celsius) that converts Celsius to Fahrenheit.
# def convert_temp(celsius):
#     Fahrenheit = (celsius*9/5)+32
#     return Fahrenheit
# print(convert_temp(30))

# 6.Write a function calculate_percentage(total, obtained) that returns the percentage.
# def calculate_percentage(total,obtained):
#     percentage = (obtained/total)*100
#     return percentage
# print(f"Percentage is {calculate_percentage(100,70)}")

# 7.Write a function largest_of_three(a, b, c) that returns the largest number.
# def largest_of_three(a,b,c):
#     if a>b and a>c:
#         return a 
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(f"Largest among the three numbers is {largest_of_three(40,30,90)}")

# 8.Write a function smallest_of_three(a, b, c) that returns the smallest number.
# def smallest_of_three(a, b, c):
#     if a<b and a<c:
#         return a
#     elif b<a and b<c:
#         return b
#     else:
#         return c
# print(f"The samllest among three is {smallest_of_three(3,2,1)}")

# 9.Write a function check_voting_age(age) that returns "Eligible" if age is 18 or above, 
# otherwise "Not Eligible".
# def check_voting_age(age):
#     if age>=18:
#         return "Eligible"
#     else:
#         return "Not Eligible"
# print(f"You are {check_voting_age(29)}")

#10.Write a function factorial(n) that calculates and returns the factorial of a number.
# def factorial(n):
#     i=1
#     fact=1
#     while i<n+1:
#         fact*=i
#         i+=1
#     return fact
# result = factorial(5)
# print(result)