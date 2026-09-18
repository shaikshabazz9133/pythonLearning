# arthemetic operators are +,-,*,/,%
a = 10
b = 10
sum = a+b
sub = a-b
multi = a*b
divide = a/b
modulo = a % b
print(f'sum :{sum}')
print(f'sub:{sub}')
print(f'multi:{multi}')
print(f'divsion:{divide}')
print(f"modulus:{modulo}")
# relational operators:<, >,==,<=,>=,==
a = 10
b = 20
lessthan = a < b
greaterthan = a > b
equalto = a == b
notequalto = a != b
lessthanorequal = a <= b
greaterthanorequal = a >= b
print(f"Less than: {lessthan}")
print(f"Greater than: {greaterthan}")
print(f"Equal to: {equalto}")
print(f"Not equal to: {notequalto}")
print(f"Less than or equal: {lessthanorequal}")
print(f"Greater than or equal: {greaterthanorequal}")
# logical operators :
x = True
y = False
resultand = x and y   # True only if both are True
resultor = x or y     # True if at least one is True
resultnot = not x     # gives opposite the boolean answer
print(f"AND: {resultand}")
print(f"OR: {resultor}")
print(f"NOT x: {resultnot}")

# assignment operator:
x = 10   # Assign
x += 5   # x = x + 5 (15)
x -= 3   # x = x - 3 (12)
x *= 2   # x = x * 2 (24)
x /= 4   # x = x / 4 (6.0)
print(f"Final Assigned Value: {x}")
# identity operator:
a = [1, 2, 3]
b = [1, 2, 3]
c = a
isoperator = a is c       # True, because c points to a exact object
isnotoperator = a is not b  # True, because a and b are separate objects in memory

print(f"a is c: {isoperator}")
print(f"a is not b: {isnotoperator}")

# memborship operator:
fruits = ["apple", "banana", "cherry"]
inoperator = "banana" in fruits
notinoperator = "grape" not in fruits
print(f"Is 'banana' in fruits?: {inoperator}")
print(f"Is 'grape' not in fruits?: {notinoperator}")
