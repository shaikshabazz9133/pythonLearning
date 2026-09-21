class Animal:
    def __init__(self, name, sound):
        # self.name and self.sound are ATTRIBUTES (data stored on the object)
        self.name = name
        self.sound = sound

    def make_sound(self):
        # This is a METHOD (a function that belongs to the class)
        print(f"{self.name} says {self.sound}")

    def info(self):
        print(f"I am an animal named {self.name}")