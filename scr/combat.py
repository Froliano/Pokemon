from Entity.player_fight import Player_Combat
from random import randint

from scr.Entity.mobs import Mobs


class Combat:

    def __init__(self):

        self.player = Player_Combat(5, 15, 30, 3, 60)
        self.player2 = Mobs(5, 15, 30, 3, 60)
        self.premier_joueur()

    def premier_joueur(self):
        if self.player.speed > self.player2.speed:
            self.current_player = self.player
            self.ennemy = self.player2
        elif self.player.speed < self.player2.speed:
            self.ennemy = self.player2
            self.current_player = self.player
        else:
            a = randint(0, 1)
            if a == 0:
                self.current_player = self.player
                self.ennemy = self.player2
            elif a == 1:
                self.ennemy = self.player2
                self.current_player = self.player

    def change_joueur(self):
        self.current_player, self.ennemy = self.ennemy, self.current_player

    def play(self):
        while self.ennemy.is_alive():
            action=input('Attaquez:1\n Heal:2')
            if action==1:
                self.ennemy.damage(3)
            elif action == 2:
                self.current_player.heal()
            self.change_joueur()
            print(self.player2.health, self.player.health)

    def update(self):
        self.play()
