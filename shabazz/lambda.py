#  lambda is a ananomous function 

def square(x):
    return x * x

print(square(5))

square = lambda x : x * x

print(square(5))

add = lambda a,b : a + b

print(add(20,30))

# map() applies a function to every item in an iterable.

numbers = [1,2,3,4,5]

squares = list(map(lambda x : x * x , numbers))

print(squares)

# filters is used to select based on condition 

num = [1,2,3,4,5,6]

even = list(
    filter(lambda x : x % 2 != 0 , num)
)
print(even)

# Keyword and Reserved Words
