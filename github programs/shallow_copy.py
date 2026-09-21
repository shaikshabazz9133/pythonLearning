#general
'''a=[10,20,30]
b=a
b.append(50)
print(a)
print(b)'''


#shallow
import copy

'''a = [[10, 20, 30], [40, 50]]

b = copy.copy(a)

b[0].append(60)

print(a)
print(b)'''


#deep
'''import copy
a=[[10,20],[30,40]]
b=copy.deepcopy(a)
b[0].append(50)
print(a)
print(b)'''