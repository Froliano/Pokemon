from dataclasses import dataclass
import pygame, pytmx, pyscroll

from scr.map_entity import NPC
from scr.combat import Combat


@dataclass
#donnée de la classe portail
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str
    npc_id: int = None


@dataclass
#donnée de la classe Map
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]


class MapManager:

    def __init__(self, screen, player):
        self.maps = dict() # "house" -> Map("house", walls, group)
        self.current_map = "world"
        self.previous_map = self.current_map
        self.previous_player_pos = None

        self.screen = screen
        self.player = player
        self.combat = Combat()

        #chargement des map/portail rataché/NPC rattaché
        self.register_map("world", portals=[
            Portal(from_world="world", origin_point="enter_house1", target_world="house", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_house2", target_world="house2", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="fight", target_world="fight", teleport_point="spawn_fight", npc_id=1)
        ], npcs=[
            NPC("paul", id=0, nb_points=7, dialog=["Bonne aventure", "je m'appelle Paul", "a+"]),
            NPC("robin", id=1, nb_points=4, xp=10)
        ])
        self.register_map("house", portals=[
            Portal(from_world="house", origin_point="exit_house", target_world="world", teleport_point="exit_house1")
        ])
        self.register_map("house2", portals=[
            Portal(from_world="house2", origin_point="exit_house", target_world="world", teleport_point="exit_house2")
        ])
        self.register_map("fight", npcs=[
            NPC("robin", id=2, nb_points=1)
        ])

        self.teleport_player("player")
        self.teleport_npcs()

    #on regarde si un npc est en contact avec une collision
    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.feet.colliderect(self.player.feet) and type(sprite) is NPC:
                dialog_box.chat_execute(sprite.dialog)

    #on regarde si le joueur est en contact avec une collision
    def check_collision(self, dialog_box):
        #portails
        npc_value = None
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                if portal.npc_id is not None:
                    for npc in self.get_npcs():
                        if npc.id == portal.npc_id:
                            rect = pygame.Rect(npc.position[0], npc.position[1], point.width, point.height)
                            npc_value = npc
                else:
                    rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.previous_map = self.current_map
                    self.previous_player_pos = self.player.position
                    self.current_map = portal.target_world
                    self.teleport_player(copy_portal.teleport_point)
                    if self.current_map == "fight":
                        self.player.change_show_bar()
                        self.change_npc(self.get_npcs()[0], npc_value)
                        self.combat.define(self.player, self.get_npcs()[0])
                        self.get_npcs()[0].change_show_bar()
                        dialog_box.fight_execute()


        #collision
        for sprite in self.get_group().sprites():

            if type(sprite) is NPC:
                if sprite.feet.colliderect(self.player.feet):
                    sprite.speed = 0
                    self.player.move_back()
                else:
                    sprite.speed = sprite.default_speed

            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def fight(self):
        if self.current_map == "fight":
            self.combat.play()

    def change_npc(self, npc2, npc):
        npc2.fight_speed = npc.fight_speed
        npc2.xp = npc.xp
        npc2.health = npc.health
        npc2.attack = npc.attack
        npc2.defense = npc.defense

    def teleport_player(self, name):
        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, portals=[], npcs=[]):
        # charger la carte
        tmx_data = pytmx.util_pygame.load_pygame(f"../assets/map/{name}.tmx")
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # definir une liste qui va stocker les rectangles de collision
        walls = []
        npcs_portal = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        # recuperer tout les npcs pour les ajouter au groupe
        for npc in npcs:
            group.add(npc)

        # Creer un objet map
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls
    def get_npcs(self): return self.get_map().npcs

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self, screen, dialogue_box):
        self.get_group().update()
        self.check_collision(dialogue_box)

        for npc in self.get_map().npcs:
            npc.move()
            npc.update_health_bar(screen)