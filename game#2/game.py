import pygame
import pytmx
import pyscroll
from player import Player

class Game:

    def __init__(self):
        # creer la fenetre
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("pygamon")

        # charger la carte
        tmx_date = pytmx.util_pygame.load_pygame("assets/carte.tmx")
        map_date = pyscroll.data.TiledMapData(tmx_date)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_date, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur
        player_position = tmx_date.get_object_by_name("player")
        self.player = Player(player_position.x, player_position.y)

        # definir une liste qui va stocker les rectangles de collision
        self.walls = []
        for obj in tmx_date.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # definir le rect de collision pour entrer dans la maison
        enter_house = tmx_date.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        self.map = "world"

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation("up")
        if pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation("down")
        if pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation("left")
        if pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation("right")

    def switch_house(self):
        # charger la carte
        tmx_date = pytmx.util_pygame.load_pygame("assets/house.tmx")
        map_date = pyscroll.data.TiledMapData(tmx_date)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_date, self.screen.get_size())
        map_layer.zoom = 2

        # definir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_date.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # definir le rect de collision pour entrer dans la maison
        exit_house = tmx_date.get_object_by_name("exit_house")
        self.exit_house_rect = pygame.Rect(exit_house.x, exit_house.y, exit_house.width, exit_house.height)

        # recuperer le point de spawn de la maison
        spawn_house_point = tmx_date.get_object_by_name("spawn_house")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y - 20

    def switch_world(self):
        # charger la carte
        tmx_date = pytmx.util_pygame.load_pygame("assets/carte.tmx")
        map_date = pyscroll.data.TiledMapData(tmx_date)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_date, self.screen.get_size())
        map_layer.zoom = 2

        # definir une liste qui va stocker les rectangles de collision
        self.walls = []

        for obj in tmx_date.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        self.group.add(self.player)

        # definir le rect de collision pour entrer dans la maison
        enter_house = tmx_date.get_object_by_name("enter_house")
        self.enter_house_rect = pygame.Rect(enter_house.x, enter_house.y, enter_house.width, enter_house.height)

        # recuperer le point de spawn de la maison
        spawn_house_point = tmx_date.get_object_by_name("exit_house_world")
        self.player.position[0] = spawn_house_point.x
        self.player.position[1] = spawn_house_point.y

    def update(self):
        self.group.update()

        # verification entree maison
        if self.map == "world" and self.player.feet.colliderect(self.enter_house_rect):
            self.switch_house()
            self.map = "house"

        # verification sortie maison
        if self.map == "house" and self.player.feet.colliderect(self.exit_house_rect):
            self.switch_world()
            self.map = "world"

        # verification collision
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()


    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.group.center(self.player.rect)
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            clock.tick(60)

        pygame.quit()