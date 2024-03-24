from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self):
        self.robot = Robot("Sparky")
        self.dinosaur = Dinosaur("Rocky")

    def run_game(self):
        self.display_welcome()
        self.battle_phase()

    def display_welcome(self):
        print('Welcome to the Main Event. This match is scheduled for one fall!')
        print("")

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
        self.display_winner()
                

    def display_winner(self):
        if self.dinosaur.health > 0:
            winner = self.dinosaur.name
            print(f'The winner of the match and new champion is {winner}')
            print("")

        else:
            winner = self.robot.name
            print(f'The winner of the match and new champion is {winner}')
            print("")
