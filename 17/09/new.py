numbers = input("Enter your number : ")

numbers = numbers.split()

numbers = [int(num) for num in numbers]
slic=numbers[3:]

print(numbers)
print(slic)