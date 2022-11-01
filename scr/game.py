import pygame

from scr.combat import Combat
from scr.map import MapManager
from scr.dialog import DialogBox
from scr.map_entity import Player


class Game:

    def __init__(self):
        # creer la fenetre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pygamon")

        # generer un joueur
        self.combat = Combat()
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialogue_box = DialogBox()

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

    def update(self):
        self.map_manager.update(self.screen)

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.map_manager.draw()
            self.map_manager.fight()
            self.update()
            self.dialogue_box.render(self.screen)
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