l = [1, 2, 34, 5, 77, 88, 96, 99, 10, 12]
largest = l[0]
secondlargest = -1

for i in range(0, len(l)):
    if l[i] > largest:
        secondlargest = largest
        largest = l[i]
    elif secondlargest != largest and l[i] > secondlargest:
        l[i] = secondlargest


print(largest)
print(secondlargest)
