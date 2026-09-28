class Dog:
    def speak(self):
        print("Woof")

class Cat:
    def speak(self):
        print("Meow")

class Hybrid(Cat):
    pass

class umar(Dog):
    pass
Hybrid().speak()
umar().speak()   # 