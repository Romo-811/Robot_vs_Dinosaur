import random

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = int()
        self.check_if_alive = True

    def attack(self, robot):
        total_damage = self.attack_power + random.randint(-5, 25)
        robot.health -= total_damage
        print(f'{self.name} fires a shot at {robot.name} with the attack power of {total_damage}')
        print(f'With that shot from {self.name}, {robot.name} is now at {robot.health} health')
        print("")

    def is_alive(self):
        if self.health > 0:
            self.check_if_alive == True
        else:
            self.check_if_alive == False
