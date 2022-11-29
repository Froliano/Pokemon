import pygame

class Sound:
    def __init__(self):
        self.main_music = pygame.mixer.Sound("../assets/sounds/Main_song.mp3")
        self.battle_music = pygame.mixer.Sound("../assets/sounds/battle_song.mp3")
        self.music_volume=pygame.mixer.music.set_volume(0.25)


    def play_main(self):
        self.main_music.play(loops=-1,maxtime=20000,fade_ms=2000)

    def play_battle(self):
        self.battle_music.play(loops=-1, maxtime=0)

    def stop_main_music(self):
        self.main_music.stop()

    def stop_battle_music(self):
        self.battle_music.stop()

