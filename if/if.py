l = eval(input("enter the values"))
if type(l) in (str,list,tuple,set,dict):
    print(len(l))
elif type(l)==int:
    print(l**2)
elif type(l)==float:
    print(l**3)
else:
    print(l)