x = float(input("enter the first number: "))
y = float(input("enter the second number: "))
# Fixed the spelling of "subtract"
operator = input("add/subtract/multiply/divide: ")

if operator == "add":
    ans = x + y
elif operator == "subtract":
    ans = x - y
elif operator == "multiply":
    ans = x * y
elif operator == "divide":
    # Prevent division by zero crash
    if y == 0 or x == 0:
        ans = 0
    else:
        ans = x / y
else:
    # Catch any typos or invalid inputs
    ans = "Error: Invalid operator chosen."

print(ans)
