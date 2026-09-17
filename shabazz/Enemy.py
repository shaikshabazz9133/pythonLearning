class Enemy:


    type_of_enemy = str
    health_points = int = 10
    attack_damage = int = 1

    def talks(self):
        print(f"I am a {self.type_of_enemy} be prepared to fight me!")

    def walk_forwar(self):
        print(f"{self.type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.type_of_enemy} attacks you for {self.attack_damage} damage")       
