from scr.player import Player_Combat
from random import randint


class Combat:

    def __init__(self):

        self.player = Player_Combat(5, 15, 30, 3, 60)
        self.player2 = Player_Combat(5, 15, 30, 3, 60)
        self.premier_joueur()

    def premier_joueur(self):
        if self.player.speed > self.player2.speed:
            self.current_player = self.player
            self.ennemy = self.player2
        elif self.player.speed < self.player2.speed:
            self.start.append(self.player2)
            self.start.append(self.player)
        else:
            a = randint(0, 1)
            if a == 0:
                self.start.append(self.player)
                self.start.append(self.player2)
            elif a == 1:
                self.start.append(self.player2)
                self.start.append(self.player)

    """def change_joueur(self):
        self.player.change_start()
        self.player2.change_start()"""

    def play(self):

        self.current_player = self.sta
        self.start.append(self.current_player)
        self.current_player.damage(self.start.pop(0))
        self.start


    def update(self):
        self.play()
