def list_sum(numbers):
    total = 0

    for num in numbers:
        total = total + num

    return total

numbers = [10, 20, 30, 40, 50]

print(list_sum(numbers))
