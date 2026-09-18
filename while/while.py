'''l = eval(input("Enter the collection"))
i=0
while i<len(l):
    if type(l[i]) in (str,list,tuple,set,dict):
        print(len(l[i]))
    elif type(l[i])==int:
        print(l[i]**2)
    elif type(l[i])==float:
        print(l[i]**3)
    else:
        print(l[i])
    i+=1
print(l)'''

l = eval(input("Enter the collection"))
for i in l:
    if type(i) in (str,list,tuple,set,dict):
        print(len(i))
    elif type(i) == int:
        print(i**2)
    elif type(i) == float:
        print(i**3)
    else:
        print(i)