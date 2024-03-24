from weapon import Weapon
import random

weapons = [Weapon('Club', 10), Weapon('Blaster', 15), Weapon('Rocket Grenade', 20)]

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.check_if_alive = True
        self.active_weapon = random.choice(weapons)


    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f'{self.name} fires a shot at {dinosaur.name} with a {self.active_weapon.name} which results in {self.active_weapon.attack_power} damage')
        print(f'With that shot from {self.name}, {dinosaur.name} is now at {dinosaur.health} health')
        print("")

    def is_alive(self):
        if self.health > 0:
            self.check_if_alive == True
        else:
            self.check_if_alive == False
