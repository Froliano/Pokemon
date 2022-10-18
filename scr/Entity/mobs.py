

class Mobs:

    def __init__(self, speed, xp, health, attack, defense):
        self.speed = speed
        self.xp = xp
        self.health = health
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

    def is_alive(self): return self.alive