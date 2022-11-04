import pygame

from random import randint
from scr.map_entity import Player


class Combat:

    def __init__(self):
        self.player = Player()
        self.ennemy = Player()
        self.clock = 0

    def premier_joueur(self, p1, p2):
        if p1.speed > p2.speed:
            self.player = p1
            self.ennemy = p2
        elif p1.speed < p2.speed:
            self.player = p2
            self.ennemy = p1
        else:
            a = randint(0, 1)
            if a == 0:
                self.player = p1
                self.ennemy = p2
            elif a == 1:
                self.player = p2
                self.ennemy = p1

    def change_joueur(self):
        self.player, self.ennemy = self.ennemy, self.player

    def define(self, player, ennemy):
        self.premier_joueur(player, ennemy)

    def play(self):

        if self.player.is_alive():
            self.clock += 1
            if self.clock >= 50:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_1]:
                    self.ennemy.damage(3)
                    self.clock = 0
                    self.change_joueur()
                elif pressed[pygame.K_2]:
                    self.player.heal()
                    self.clock = 0
                    self.change_joueur()
                print(self.player.health, self.ennemy.health)