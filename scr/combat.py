import pygame

from random import randint
import random
from scr.map_entity import Player, NPC


class Combat:

    def __init__(self):
        self.player = Player()
        self.ennemy = Player()
        self.clock = 0
        self.run = False
        self.alls_attack = [Punch, Fire_ball, Thunder]

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

    def fight_turn(self, NPC, ennemy):
        prc_health = NPC.health / NPC.max_health

        if prc_health <= 0.2 and random.randint(0, 100) < 60:
            NPC.heal()
        elif prc_health <= 0.5 and random.randint(0, 100) < 40:
            NPC.heal()
        else:
            ennemy.damage(self.player.attack)
        self.clock = 0
        self.change_joueur()

    def define(self, player, ennemy):
        self.run = True
        self.premier_joueur(player, ennemy)

    def chose_attack(self, attack_name):
        for attack in self.alls_attack:
            if attack_name == attack.name:
                return attack
        return attack_name

    def damage(self, attack):
        attack = self.chose_attack(attack)
        if attack == "heal":
            self.player.heal()
            self.clock = 0
            self.change_joueur()
        elif self.player.mana >= attack.mana_use:
            self.player.withdraw_mana(attack.mana_use)
            dgt = (self.player.level * self.player.attack * attack.puissance) // (self.ennemy.defense * 10)
            self.ennemy.damage(dgt)
            self.clock = 0
            self.change_joueur()

    def play(self):
        if self.player.is_alive():
            self.clock += 1
            if self.clock >= 30:
                if type(self.player) is NPC:
                    self.fight_turn(self.player, self.ennemy)
                elif type(self.player) is Player:
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_1]:
                        self.damage(self.player.actions[1])
                    elif pressed[pygame.K_2]:
                        self.damage(self.player.actions[2])
                    elif pressed[pygame.K_3]:
                        self.damage(self.player.actions[3])
                    elif pressed[pygame.K_4]:
                        self.damage(self.player.actions[4])

        if not self.player.is_alive() and type(self.player) is NPC:
            self.ennemy.add_xp(self.player.xp)
            self.run = False


class Punch:
    name = "Punch"
    puissance = 10
    mana_use = 0


class Fire_ball:
    name = "Fire_ball"
    puissance = 15
    mana_use = 5


class Thunder:
    name = "Thunder"
    puissance = 25
    mana_use = 10
