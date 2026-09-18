# Tomorrow Program
numbers = input("Enter numbers separated by spaces: ")

numbers = numbers.split()

numbers = [int(num) for num in numbers]

print("Original:", numbers)

print("First 3:", numbers[:3])

print("Last 2:", numbers[-2:])

print("Reverse:", numbers[::-1])

# second program

copy_numbers = numbers.copy()

copy_numbers.append(100)

print("Original:", numbers)
print("Copy:", copy_numbers)