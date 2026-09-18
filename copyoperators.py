# n1 = [1, 2, 3, 4]
# n2 = n1  # general copy
# print(n1)
# print(n2)
# n2.append(5)
# print(n2)
# print(n1)
# here if i append value 5 to n2 ,even n1 is getting changed in order to avoid this we use shallow copy

# SHALLOW COPY:
import copy
n1 = [1, 2, 3, 4]
n2 = n1.copy()
n2.append(5)
print(n1)
print(n2)
# here as we use shallow copy the n1 value remains unchanged ,but if there are nested lists in a list then we have to use Deep copy

# DEEPCOPY:

n1 = [1, 2, [3, 4], 3, 4]
n2 = copy.deepcopy(n1)
print(n2)
print(n1)
n1.append(5)

print(n1)
print(n2)
