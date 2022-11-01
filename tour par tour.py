

class Player:

    def __init__(self, speed = 5, xp = 0, health = 30, attack = 0, defense = 0):
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

    def get_health(self):
        return self.health


def change_joueur(p1, p2):
    return p2, p1

player1 = Player()
player2 = Player()

while player1.is_alive():
    action = input(":")
    if action == "1":
        player2.damage(3)
    elif action == "2":
        player1 .heal()
    player1, player2 = change_joueur(player1, player2)
    print(player1.get_health(), player2.get_health())



