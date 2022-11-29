import pygame

from scr.combat import Combat
from scr.map import MapManager
from scr.dialog import DialogBox
from scr.map_entity import Player


class Game:

    def __init__(self):
        # creer la fenetre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game")

        # generer un joueur
        self.combat = Combat()
        self.player = Player(attack=3)
        self.map_manager = MapManager(self, self.screen, self.player)
        self.dialogue_box = DialogBox()
        self.shop_open = False

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
        if pressed[pygame.K_DOWN]:
            self.player.move_down()
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
        if pressed[pygame.K_RIGHT]:
            self.player.move_right()

    def game_over(self):
        if self.player.is_alive() is False:
            self.dialogue_box.game_over_render(self.screen)

    def shop(self):
        self.dialogue_box.shop(self.screen)
        self.dialogue_box.money_render(self.player, self.screen, 720, 50)

    def update(self):
        self.map_manager.draw()
        self.map_manager.fight(self.screen, self.dialogue_box)
        self.map_manager.update(self.screen)
        self.map_manager.play_main_music()
        self.map_manager.play_battle_music()

        self.player.update_health_bar(self.screen)
        self.dialogue_box.chat_render(self.screen)
        if not self.shop_open:
            self.dialogue_box.money_render(self.player, self.screen)
        self.dialogue_box.mana_render(self.player, self.screen)
        self.dialogue_box.health_render(self.player, self.screen)

        self.game_over()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialogue_box)

            clock.tick(60)

        pygame.quit()