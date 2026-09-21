class Student:
    school_name = "Green Valley High"
    city = "Banglore"

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"ID: {self.id}")
        print(f"School: {self.school_name}")
        print(f"City: {self.city}")
        print()   # blank line for spacing

class teacher(Student):
    def __init__(self, name, age, id,subjects,period):
        super().__init__(name,age,id)
        self.subjects=subjects
        self.period=period
    def display(self):
        super().display()
        print(f"subjects:{self.subjects}")
        print(f"periods:{self.period}")
    

s1 = Student("shaik", 25, 454)
s2 = Student("shahidd", 23, 456)
s3 = teacher("manar",25,459,"history",7)

people=[s1,s2,s3]
for person in people:
    person.display()

