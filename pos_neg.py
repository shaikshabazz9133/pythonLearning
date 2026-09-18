'''s = eval(input("Enter the set"))
pos=[]
neg=[]
for i in s:
    if 0<=i<=9:
        pos+=[i]
    else:
        neg+=[i]
print(pos,neg)
'''
di = {"saughat":40,"shabaz":75,"usman":60,"mannar":75,"umar":70}
i=list(di.keys())
j=0
while j<len(di):
    if di[i[j]]>30:
        print("pass")
    else:
        print("fail")
    j+=1

