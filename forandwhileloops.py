# 1. First 10 Even Numbers (Q1)
print("1. First 10 Even Numbers:")
counter = 1
currentNum = 2
while counter <= 10:
    print(f"Even Number: {currentNum}")
    currentNum += 2
    counter += 1
print()


# 2. First 10 Odd Numbers (Q2)
print("2. First 10 Odd Numbers:")
for oddNum in range(1, 20, 2):
    print(f"Odd Number: {oddNum}")
print()


# 3. First 10 Natural Numbers in Reverse Order (Q8)
print("3. Reverse Natural Numbers (10 down to 1):")
currentNum = 10
while currentNum >= 1:
    print(f"Number: {currentNum}")
    currentNum -= 1
print()


# 4. Sum of First 10 Natural Numbers (Q9)
currentNum = 1
totalSum = 0
while currentNum <= 10:
    totalSum += currentNum
    currentNum += 1
print(f"4. Sum of First 10 Natural Numbers: {totalSum}\n")


# 5. Factorial of a Number (Q19)
num = 5
factorialResult = 1
tempNum = num
while tempNum > 0:
    factorialResult *= tempNum
    tempNum -= 1
print(f"5. Factorial of {num}: {factorialResult}\n")


# 6. Print Characters of a String (Q40)
targetString = "PYTHON"
index = 0
print("6. Characters of String 'PYTHON':")
while index < len(targetString):
    print(f"Character: {targetString[index]}")
    index += 1
print()


# 7. Print Table of a Number (Q11)
userNumber = 5
print(f"7. Multiplication Table for {userNumber}:")
for multiplier in range(1, 11):
    productValue = userNumber * multiplier
    print(f"{userNumber} * {multiplier} = {productValue}")
print()


# 8. Count Vowels in a String (Q59)
inputText = "hello world"
vowelCount = 0
for character in inputText:
    if character in "aeiouAEIOU":
        vowelCount += 1
print(f"8. Total Vowels in '{inputText}': {vowelCount}\n")


# 9. Extract Even Values from a Dictionary (Q47)
sampleDict = {"val1": 10, "val2": 20, "val3": 23, "val4": 22}
print("9. Even Values in Dictionary:")
for dictKey, dictValue in sampleDict.items():
    if dictValue % 2 == 0:
        print(f"{dictKey} -> {dictValue}")
print()


# 10. Print 'Thank You' N Times (Q100)
repeatTimes = 3
print(f"10. Print 'Thank You' {repeatTimes} times:")
for step in range(repeatTimes):
    print("Thank you")
