
import random

class Hero():
    def __init__(self, name):
        self.name = name
        self.hilth = 100
        self.atack_power = 20
    def attack(self, enemy):
        if enemy.hilth > 0:
            enemy.hilth -= self.atack_power
            print(f"{self.name} attack {enemy.name} and deals {self.atack_power} damage")
        else:
            print(f"{enemy.name} is dead")

    def is_alive(self):
        if self.hilth > 0:
            return True
        else:
            return False


class Game():
    def __init__(self,player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")
    def start(self):
        print("Start game!")
        print(f"{self.player.name} vs {self.computer.name}")
        print(f"{self.player.name} hilth {self.player.hilth}")
        print(f"{self.computer.name} hilth {self.computer.hilth}")

        turn = random.randint(0,1)
        while self.player.is_alive() and self.computer.is_alive():
            # turn = random.randint(0,1)
            if turn == 0:
                self.player.attack(self.computer)
                turn = 1
            else:
                self.computer.attack(self.player)
                turn = 0

        if self.player.is_alive():
            print(f"{self.player.name} WIN!!!")
        else:
            print(f"{self.computer.name} WIN!!!")

if __name__ == "__main__":

    game = Game(input("Enter Hero name: "))
    game.start()
