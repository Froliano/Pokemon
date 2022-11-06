from tour_par_tour_v2 import Playerv2
from tour_par_tour_v2 import Enemyv2
from random import randint


class Game_tour_par_tour:
    def __init__(self):
        self.playerv2 = Playerv2()
        self.enemyv2 = Enemyv2()
        self.enemy_commence=True


    def commmence(self):
        if self.playerv2.speed<self.enemyv2.speed:
            self.enemy_commence=True
        elif self.playerv2.speed>self.enemyv2.speed:
            self.enemy_commence=False
        else:
            a=randint(0,1)
            if a == 0:
                self.enemy_commence=True
            elif a == 1:
                self.enemy_commence=False

    def attac_enemy(self):
        running_attack=True
        while running_attack==True:
            a=randint(1,2)
            if a == 1:
                print(f"{self.enemyv2.name} lance un coup de masse sur {self.playerv2.name} !")
                dmg=self.enemyv2.attack
                self.playerv2.health -= dmg
                print(f"{self.playerv2.name} perd {dmg}HP")
                running_attack=False
            if a == 2:
                if self.enemyv2.mana>4:
                    print(f"{self.enemyv2.name} lance une tournade sur {self.playerv2.name} !")
                    self.enemyv2.mana-=4
                    dmg=self.enemyv2.attack_spe+8
                    self.playerv2.health-=dmg
                    print(f"{self.playerv2.name} perd {dmg}HP")
                    running_attack=False


    def attac_player(self):
        running_attack=True
        while running_attack==True:
            a=int(input('quelle attaque veut tu lancer ?\n 1:Boule de feu (5 de mana) \n 2:Simple coup dépée \n 3:Coup de boule (-2 pv) \n 4:Tonnerre (7 de mana) \n'))
            if a == 1:
                if self.playerv2.mana>5:
                    print(f"{self.playerv2.name} lance une boule de feu sur {self.enemyv2.name} !")
                    self.playerv2.mana-=5
                    self.enemyv2.health-=self.playerv2.attack_spe+4
                    running_attack=False
                else:
                    print("Vous navez pas assez de mana")
            if a ==2:
                print(f"{self.playerv2.name} lance un coup dépée sur {self.enemyv2.name} !")
                self.enemyv2.health -= self.playerv2.attack
                running_attack = False
            if a ==3:
                if self.playerv2.health>2:
                    print(f"{self.playerv2.name} lance un coup dépée sur {self.enemyv2.name} !")
                    self.enemyv2.health -= self.playerv2.attack+2
                    running_attack = False
                else:
                    print('Vous navez pas assez de point de vie !')
            if a ==4:
                if self.playerv2.mana>7:
                    print(f"{self.playerv2.name} lance un éclair sur {self.enemyv2.name} !")
                    self.playerv2.mana-=7
                    self.enemyv2.health-=self.playerv2.attack_spe+4
                    running_attack=False
                else:
                    print("Vous navez pas assez de mana")

    def heal_enemy(self):
        running_heal = True
        while running_heal == True:
            a = randint(1,2)
            if a == 1:
                if self.enemyv2.mana >= 5:
                    self.enemyv2.mana -= 5
                    self.enemyv2.health += 10
                    print(f"{self.enemyv2.name} c soigner")
                    running_heal = False
                else:
                    a=randint(1,2)
            if a == 2:
                for i in self.enemyv2.inventaire:
                    b = 0
                    if i == 'potion':
                        del self.enemyv2.inventaire[b]
                    else:
                        b += 1
                        if b==len(self.enemyv2.inventaire)-1:
                            print("il ny a pas de potion")
                            a=randint(1,2)
                    print(f"{self.enemyv2.name} à utiliser une potion")
                    self.playerv2.inventaire.pop(i)
                    self.playerv2.health += 10
                    running_heal = False

    def heal_player(self):
        running_heal=True
        while running_heal==True:

            a=int(input('Comment voulez vous vous soigner ?\n\n1:low_heal (5mana)\n 2:utiliser une potion (il vous en faut une)'))
            if a==1:
                if self.playerv2.mana>=5:
                    self.playerv2.mana-=5
                    self.playerv2.health+=10
                    running_heal=False
                else:
                    print('Vous navez pas assez de mana')
            if a==2:
                for i in self.playerv2.inventaire:
                        b=0
                        if i=='potion':
                            del self.playerv2.inventaire[b]
                        else:
                            b+=1
                        self.playerv2.inventaire.pop(i)
                        self.playerv2.health+=10
                        running_heal=False
                else:
                    print('Vous navez pas de potion')
                    a = int(input('Comment voulez vous vous soigner ?\n\n1:low_heal (5mana)\n 2:utiliser une potion (il vous en faut une)'))



    def lvl_up(self):
        self.playerv2.xp-=self.playerv2.xp_max
        self.playerv2.attack+=1
        self.playerv2.attack_spe+=2
        self.playerv2.health+=3
        self.playerv2.xp_max+=30
        self.playerv2.speed+=1
        self.playerv2.level+=1


    def escape(self):
        if self.playerv2.speed>self.enemyv2.speed:
            a=randint(1,2)
            if a ==1:
                return 1
            else:
                return 2
        else:
            return 3


    def run(self):
        running=True
        Game.commmence()
        while running == True:
            if self.enemy_commence ==True:
                print(f"C le tour de {self.enemyv2.name}.\n" )
                print(self.enemyv2.health)
                running_tour_enemy=True
                while running_tour_enemy is True:
                    action = randint(1,2)
                    print('a')
                    if action == 1:
                        self.attac_enemy()
                        print('b')
                        running_tour_enemy = False
                    if action == 2:
                        self.heal_enemy()
                        print('c')
                        running_tour_enemy = False

                if self.playerv2.health<=0:
                    print(f"{self.playerv2.name} à perdu !")
                    running=False
                else:
                    running_tour_player = True
                    print(f"C le tour de {self.playerv2.name} .\n")
                    while running_tour_player is True:

                        action=int(input('1: stat\n2: attaquer\n3: Se soigner\n4: Fuite\n'))
                        if action == 1:
                            self.playerv2.show_stats()
                        if action == 2:
                            self.attac_player()
                            running_tour_player = False
                        if action == 3:
                            self.heal_player()
                            running_tour_player = False
                        if action == 4:
                            if self.escape()==1:
                                print("Vous vous etes enfui")
                                running=False
                            elif self.escape()==2:
                                print("Vous navez pas reussi a vous enfuir")
                                running_tour_player=False
                            elif self.escape()==3:
                                print("Vous etes trop lent pour vous enfuir")
                        print("\n")
                    if self.enemyv2.health <= 0:
                        print(f"{self.enemyv2.name} à perdu !")
                        running = False
            else:
                print(f"C le tour de {self.playerv2.name} .\n")
                running_tour_player = True
                while running_tour_player is True:

                    action = int(input('1: stat\n2: attaquer\n3: Se soigner\n4: Fuite\n'))
                    if action == 1:
                        self.playerv2.show_stats()
                    if action == 2:
                        self.attac_player()
                        running_tour_player = False
                    if action == 3:
                        self.heal_player()
                        running_tour_player = False
                    if action == 4:
                        if self.escape() == 1:
                            print("Vous vous etes enfui")
                            running = False
                            running_tour_player=False
                        elif self.escape() == 2:
                            print("Vous navez pas reussi a vous enfuir")
                            running_tour_player = False
                        elif self.escape() == 3:
                            print("Vous etes trop lent pour vous enfuir")
                    print("\n")
                if self.enemyv2.health <= 0:
                    print(f"{self.enemyv2.name} à perdu !")
                    running = False
                else:
                    while running is True:
                        print(f"C le tour de {self.enemyv2.name}.\n")
                        print(self.enemyv2.health)
                        running_tour_enemy = True
                        while running_tour_enemy is True:
                            action = randint(1, 2)
                            if action == 1:
                                self.attac_enemy()
                                running_tour_enemy = False
                            if action == 2:
                                self.heal_enemy()
                                running_tour_enemy = False

                        if self.playerv2.health <= 0:
                            print(f"{self.playerv2.name} à perdu !")
                            running = False
                        else:
                            print(f"C le tour de {self.playerv2.name} .\n")
        print("merci davoir jouer")






Game=Game_tour_par_tour()
Game.run()






