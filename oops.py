class Student:
    school_name = "Green Valley High"
    city = "Banglore"

    def __init__(self, name, age, id):
        self._name = name     
        self._age = age
        self._id = id

    def display(self):
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"ID: {self._id}")
        print(f"School: {self.school_name}")
        print(f"City: {self.city}")
        print()

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            print("Invalid age!")


class teacher(Student):
    def __init__(self, name, age, id, subjects, period):
        super().__init__(name, age, id)
        self._subjects = subjects
        self._period = period

    def display(self):
        super().display()
        print(f"subjects:{self._subjects}")
        print(f"periods:{self._period}")


class batch(teacher):
    def __init__(self, name, age, id, subjects, period, batchnumber, code):
        super().__init__(name, age, id, subjects, period)
        self._batchnumber = batchnumber
        self._code = code

    def display(self):
        super().display()
        print(f"batchnumber:{self._batchnumber}")
        print(f"code:{self._code}")


s1 = Student("shaik", 25, 454)
s2 = Student("shahidd", 23, 456)
s3 = teacher("manar", 25, 459, "history", 7)
s4 = batch("saughat", 28, 434, "pythonx", 6, 808, "zapa")

people = [s1, s2, s3, s4]
for person in people:
    person.display()