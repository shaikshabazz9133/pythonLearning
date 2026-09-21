a = [17,20,"level","mango","banana","radar"]
b =[]

for i in a:
    if type(i)==str and i==i[::-1]:
        b.append(i)
        print(b)
       
  
