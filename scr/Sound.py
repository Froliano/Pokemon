import pygame

class Sound:
    def __init__(self):
        self.main_music = pygame.mixer.Sound("../assets/sounds/Main_song.mp3")
        self.battle_music = pygame.mixer.Sound("../assets/sounds/battle_song.mp3")
        self.shop_music = pygame.mixer.Sound("../assets/sounds/shop_song.mp3")
        self.house_music = pygame.mixer.Sound("../assets/sounds/house_song.mp3")


    def play_main(self):
        self.main_music.play(loops=-1,maxtime=71000,fade_ms=10000)

    def play_battle(self):
        self.battle_music.play(loops=-1, maxtime=0)

    def play_house(self):
        self.house_music.play(loops=-1, maxtime=0)

    def play_shop(self):
        self.shop_music.play(loops=-1, maxtime=0)

    def stop_main_music(self):
        self.main_music.stop()

    def stop_shop_music(self):
        self.shop_music.stop()

    def stop_house_music(self):
        self.house_music.stop()

    def stop_battle_music(self):
        self.battle_music.stop()

