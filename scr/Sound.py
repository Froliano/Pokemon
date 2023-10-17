import pygame


class SoundManager:

    def __init__(self):
        self.sounds = {
            "main" : pygame.mixer.Sound("../assets/sounds/Main_song.mp3"),
            "house": pygame.mixer.Sound("../assets/sounds/house_song.mp3"),
            "battle": pygame.mixer.Sound("../assets/sounds/battle_song.mp3"),
            "shop": pygame.mixer.Sound("../assets/sounds/shop_song.mp3"),
            "recovery": pygame.mixer.Sound("../assets/sounds/recovery.mp3"),
        }
        self.active = False

    def first_music(self):
        if not self.active:
            self.play("main")
            self.active = True

    def play(self, name):
        self.sounds[name].play()

    def stop(self, name):
        self.sounds[name].stop()