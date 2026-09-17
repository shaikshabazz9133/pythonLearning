# def add_num(*args):
#     print(*args)
#     return sum(args)
# result = add_num(1,2,3,)

# print(result)

# def num(*args):
#     return sum(args)

# print(num(1,2,3))

#  Lambda Functions 

# square = lambda x : x * x

# print(square(5))

# num = lambda a,b : a + b

# print(num(2,3))

# cube = lambda x : x * x * x

# print(cube(3))

# is_even = lambda x : x % 2 == 0

# print(is_even(10))
# print(is_even(3))

# maximum = lambda a,b : a if a != b else b

# print(maximum(10,34))

# numbers = [1,2,3,4,5]

# result = list(map(lambda x : x * x, numbers))

# print(result)

# result = list(map(lambda x : x * 2, numbers))

# print(result)

# names = ['john','doe']

# result = list(map(lambda name: name.upper(),names) )


# print(result)

# numbers = [1,2,3,4,5,6]

# result = list(filter(lambda x : x%2 == 0 , numbers))

# print(result)

# numbers = [1,3,6,12,14,1,19]

# result = list(filter(lambda x : x > 10, numbers))

# print(result)

# a = [1, 2]
# b = [1, 2]

# print(a == b)
# print(a is b)

import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
shallow[0][1] = 100

deep = copy.deepcopy(original)
deep[1][0] = 500


print(shallow)
print(deep)
print(original)
