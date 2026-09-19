n = 1

while n <= 5:
    if n == 2:
        print("Two")
    elif n == 4:
        n += 1
        continue
    elif n == 5:
        break
    else:
        pass

    print(n)
    n += 1