# a = {10,20,-3,4,-6}
# pos =[]
# neg = []
# for numbers in a:
#     if numbers > 0:
#         pos += [numbers]
#     elif numbers < 0:
#         neg += [numbers]
#     else:
#         print("error")  
# print(pos)
# print(neg)   

student = {
    "john":45,
    "Doe":50,
    "Hari":75,
    "Krish":23
}

for name,marks in student.items():
    if marks>=50:
        print("pass")
    else:
        print("Fail")    

studen = {
    "ravi":34,
    "baby":56,
    "nobi":75,
    "john":90
}

stud = list(studen.items())

i = 0

while i < len(stud):
    name,marks = stud[i]
    if marks >= 50:
        print(name,marks,"Pass")
    else:
        print(name,marks,"Fail")
    i += 1    

