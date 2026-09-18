l = [10,25,5,80,45,100,112]
largest = l[0]
i=1
while i<len(l):
    if largest<l[i]:
        largest = l[i]
    i+=1
print(largest)

