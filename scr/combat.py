import pygame

from random import randint
import random
from scr.map_entity import Player, NPC


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
                if type(self.player) is Player:
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_1]:
                        self.ennemy.damage()
                        self.clock = 0
                        self.change_joueur()
                    elif pressed[pygame.K_2]:
                        self.player.heal()
                        self.clock = 0
                        self.change_joueur()
                elif type(self.player) is NPC:
                    self.fight_turn(self.player, self.ennemy)
                    self.clock = 0
                    self.change_joueur()

    def fight_turn(self, NPC, ennemy, amount=3):
        prc_health = NPC.health / NPC.max_health

        if prc_health <= 0.2 and random.randint(0, 100) < 60:
            NPC.heal()
        elif prc_health <= 0.5 and random.randint(0, 100) < 40:
            NPC.heal()
        else:
            ennemy.damage(amount)

    def heal(self):
        if self.health + 2 <= self.max_health:
            self.health += 2
        else:
            self.health = self.max_health