# student = {
#     "name":"shabazz",
#     "age":25,
#     "course":"B.sc"
# }


# print(student.keys())
# print(student.values())

student = {
    "name":"shabazz",
    
    "course":"B.sc"
}

for key,value in student.items():
    print(key, ":", value)
print(student.items()) #  we get the key and value pair 

print(student.get("name")) # get the particular value
student.update({
    "Salary":25000
})
student.pop('course') # remove the seected element
student.popitem() # remove the last indexing element
student.setdefault("age", 30) # set the default value it will not replaced again 
student.setdefault("age",40)
print(student)

# fromkeys Creates a new dictionary using a list/tuple of keys.
new_student = ["name","age","salary"]

result = dict.fromkeys(new_student) # it will show none values 
result = dict.fromkeys(new_student,"Not Available") # it will show Not Available Values 

print(result)
