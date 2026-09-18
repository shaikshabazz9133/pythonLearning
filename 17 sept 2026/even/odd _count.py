even = 0
odd = 0
for i in range(1,21):
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"Count of even numbers between range{even}")
print(f"Odd numbers between range{odd}")