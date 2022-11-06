
class Enemyv2:

    def __init__(self,inventaire=[], name='enemy' , level=5, speed=4, xp_give= 20, health=30, attack=3,attack_spe=5, mana=20):
        self.speed = speed
        self.inventaire=inventaire
        self.attack_spe= attack_spe
        self.level = level
        self.name = name
        self.xp_give = xp_give
        self.mana = mana
        self.health = health
        self.attack = attack
        self.alive = True

        assert (isinstance(name, str))
        assert (isinstance(attack_spe, int))
        assert (isinstance(level,int))
        assert (isinstance(speed, int))
        assert (isinstance(xp_give, int))
        assert (isinstance(mana, int))
        assert (isinstance(health, int))
        assert (isinstance(attack, int))
        assert (isinstance(True, bool))



    def show_stats(self):
        print(f"nom: {self.name}\n point de vie: {self.health}\n niveau: {self.level}\n xp_give: {self.xp_give}\n attack: {self.attack}\n attack_spé: {self.attack_spe}\n mana: {self.mana}\n speed: {self.speed}\n ")


class Playerv2:

    def __init__(self,inventaire = [] ,name='player',attack_spe=5, speed = 10, xp = 0,xp_max=100, health = 50, attack = 0, level=5, mana=10 ,):
        self.speed = speed
        self.inventaire=inventaire
        self.xp_max = xp_max
        self.level = level
        self.name = name
        self.xp = xp
        self.attack_spe = attack_spe
        self.mana = mana
        self.health = health
        self.attack = attack
        self.alive = True

        assert (isinstance(name, str))
        assert (isinstance(inventaire,list))
        assert (isinstance(attack_spe, int))
        assert (isinstance(xp_max, int))
        assert (isinstance(level,int))
        assert (isinstance(speed, int))
        assert (isinstance(xp, int))
        assert (isinstance(mana, int))
        assert (isinstance(health, int))
        assert (isinstance(attack, int))
        assert (isinstance(True, bool))

    def show_stats(self):
        print(f"nom: {self.name}\n point de vie: {self.health}\n niveau: {self.level}\n xp: {self.xp}/{self.xp_max}\n attack: {self.attack}\n attack_spé: {self.attack_spe}\n mana: {self.mana}\n speed: {self.speed}\n ")

