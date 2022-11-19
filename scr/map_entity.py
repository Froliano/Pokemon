import pygame
from scr.entity import Entity


class Player(Entity):

    def __init__(self, name = "player", fight_speed=1, xp=0, health=10, attack=1, defense=1, mana=10, money=0):
        super().__init__(name=name, x=0, y=0)
        self.default_speed = 4
        self.speed = self.default_speed

        self.fight_speed = fight_speed
        self.money = money
        self.xp = xp
        self.max_xp = 100
        self.level = 1
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.mana = mana
        self.max_mana = mana
        self.alive = True

        self.actions = {
            1 : "Punch",
            2 : "heal",
            3 : "Fire_ball",
            4 : "Thunder"
        }
        self.show_bar = False
        self.bar_position = [0, 560]

    def add_xp(self, amount):
        """
        :param amount: montant d'exp
        :return: ajout de l'exp et verification du level up
        """
        self.xp += amount
        if self.xp >= self.max_xp:
            current_xp = self.xp - self.max_xp
            self.xp = 0 + current_xp
            self.level_up()

    def add_money(self, amount):
        """
        :param amount: montant de money
        :return: ajout de la money
        """
        self.money += amount

    def level_up(self):
        """
        :return: incrémentation de l'exp et agmentation des stats
        """
        self.level += 1
        self.max_xp = int(self.max_xp * 1.09)

        self.max_health += 10
        self.attack += 1
        self.defense += 1
        print("level up")

    def change_show_bar(self):
        """
        :return: invertion du bool pour afficher la barre de vie
        """
        if self.show_bar:
            self.show_bar = False
        else:
            self.show_bar = True

    def update_health_bar(self, surface):
        """
        :param surface: surface sur laquelle appliquer la barre
        :return: affichage de la barre de vie, d'exp et de mana
        """
        # dessiner notre barre de vie
        if self.show_bar:
            health_barre = self.health/self.max_health
            xp_barre = self.xp/self.max_xp
            mana_barre = 1- self.mana/self.max_mana
            # barre de vie
            pygame.draw.rect(surface, (105, 106, 99), [self.bar_position[0], self.bar_position[1], 400, 40])
            pygame.draw.rect(surface, (30, 225, 30), [self.bar_position[0], self.bar_position[1], 400*health_barre, 40])

            # barre d'exp
            pygame.draw.rect(surface, (196, 196, 196), [self.bar_position[0], self.bar_position[1]+30, 400, 10])
            pygame.draw.rect(surface, (36, 168, 240), [self.bar_position[0], self.bar_position[1]+30, 400*xp_barre, 10])

            #barre de mana
            pygame.draw.rect(surface, (113, 24, 249), [self.bar_position[0], self.bar_position[1]-400, 40, 350])
            pygame.draw.rect(surface, (105, 106, 99), [self.bar_position[0], self.bar_position[1]-400, 40, 350*mana_barre])

    def withdraw_mana(self, amount):
        """
        :param amount: montant de mana
        :return: enlever le mana demandé
        """
        self.mana -= amount

    def damage(self, amount = 3) :
        """
        :param amount: montant de degats
        :return: diminuer la vie du joueur
        """
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.change_show_bar()

    def heal(self, amount = 2):
        """
        :param amount: montant de vie
        :return: ajout de la vie au joueur
        """
        if self.health + amount <= self.max_health:
            self.health += amount
        else:
            self.health = self.max_health

    def regen(self):
        """
        :return: reinitialiser la vie et le mana à la fin du combat
        """
        self.health = self.max_health
        self.mana = self.max_mana

    def is_alive(self):
        """
        :return: bool self.alive
        """
        return self.alive


class NPC(Player):

    def __init__(self, name, nb_points, dialog = [], id=0, fight_speed=1, xp=1, health=10, attack=1, defense=1, money=0):
        super().__init__(name=name, fight_speed=fight_speed, xp=xp, health=health, attack=attack, defense=defense, money=money)
        self.nb_points = nb_points
        self.points = []
        self.current_point = 0

        self.name = name
        self.id = id
        self.default_speed = 1.2
        self.dialog = dialog

        self.bar_position = [400, 0]

    def update_health_bar(self, surface):
        """
        :param surface: surface sur laquelle appliquer la barre
        :return: affichage de la barre de vie
        """
        # dessiner notre barre de vie
        if self.show_bar:
            barre = 1 - self.health/self.max_health
            pygame.draw.rect(surface, (30, 225, 30), [self.bar_position[0], self.bar_position[1], 400, 30])
            pygame.draw.rect(surface, (105, 106, 99), [self.bar_position[0], self.bar_position[1], 400*barre, 30])

    def move(self):
        """
        :return: déplacement du NPC en fonction du path
        """
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
        """
        :return: placement du NPC au lancement du jeux
        """
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def teleport_path(self, obj):
        """
        :param obj: path d'une map
        :return: teleporter la NPC sur un path
        """
        self.move_down()
        self.position[0] = obj.x
        self.position[1] = obj.y
        self.save_location()

    def load_points(self, tmx_data):
        """
        :param tmx_data: données de la map
        :return: chargement de tout les path des NPC
        """
        for num in range(1, self.nb_points + 1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)
