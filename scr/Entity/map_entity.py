import pygame
from scr.Entity.entity import Entity

class Player(Entity):

    def __init__(self, fight_speed=0, xp=0, health=10, attack=0, defense=0):
        super().__init__("player", 0, 0)
        self.fight_speed = fight_speed
        self.speed = 5
        self.xp = xp
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.alive = True


    def damage(self, amount):
        if self.health - amount >= amount:
            self.health -= amount
        else:
            self.alive = False


    def heal(self):
        self.health += 2

    def is_alive(self):
        return self.alive


class NPC(Entity):

    def __init__(self, name, nb_points):
        super().__init__(name, 0, 0)
        self.nb_points = nb_points
        self.points = []
        self.current_point = 0
        self.speed = 1.2
        self.name = name

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
