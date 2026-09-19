while True:
    o = input("Enter +, -, *, / or q: ")

    if o == "":
        pass
    elif o == "q":
        break
    elif o not in ["+", "-", "*", "/"]:
        print("Invalid operator")
        continue
    else:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if o == "+":
            r = a + b
        elif o == "-":
            r = a - b
        elif o == "*":
            r = a * b
        else:
            if b == 0:
                print("Cannot divide by zero")
                continue
            r = a / b

        print("Answer:", r)