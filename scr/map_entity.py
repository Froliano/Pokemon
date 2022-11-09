import pygame
import random
from scr.entity import Entity


class Player(Entity):

    def __init__(self, name = "player", fight_speed=1, xp=1, health=10, attack=1, defense=1):
        super().__init__(name, 0, 0)
        self.speed = 4

        self.fight_speed = fight_speed
        self.xp = xp
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.alive = True

        self.show_bar = False
        self.bar_position = [0, 570]

    def change_show_bar(self):
        if self.show_bar:
            self.show_bar = False
        else:
            self.show_bar = True

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        if self.show_bar:
            barre = self.health/self.max_health
            pygame.draw.rect(surface, (105, 106, 99), [self.bar_position[0], self.bar_position[1], 400, 30])
            pygame.draw.rect(surface, (30, 225, 30), [self.bar_position[0], self.bar_position[1], 400*barre, 30])

    def damage(self, amount = 3) :
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False

    def heal(self, amount = 2):
        if self.health + amount <= self.max_health:
            self.health += amount
        else:
            self.health = self.max_health

    def is_alive(self):
        return self.alive


class NPC(Player):

    def __init__(self, name, nb_points, dialog = [], id=0, fight_speed=1, xp=1, health=10, attack=1, defense=1):
        super().__init__(name, fight_speed, xp, health, attack, defense)
        self.nb_points = nb_points
        self.points = []
        self.current_point = 0

        self.name = name
        self.id = id
        self.default_speed = 1.2
        self.dialog = dialog

        self.bar_position = [400, 0]

    def move(self):
        current_point = self.current_point
        target_point = self.current_point + 1

        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_down()
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_up()
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_left()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_right()

        if self.feet.collidepoint(target_rect.center):
            self.current_point = target_point

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        for num in range(1, self.nb_points + 1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)
