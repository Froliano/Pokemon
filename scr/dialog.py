import pygame


class DialogBox:

    X_POSITION = 60
    Y_POSITION = 470

    fX_POSITION = 420
    fY_POSITION = 480

    def __init__(self):
        self.box = pygame.image.load("../assets/dialogs/dialog_box.png")

        self.fight_box = pygame.transform.scale(self.box, (400, 120))

        self.shop_box = pygame.transform.scale(self.box, (800, 600))

        self.game_over_box = pygame.transform.scale(self.box, (860, 600))
        self.game_over = pygame.image.load("../assets/dialogs/game_over.png")
        self.game_over = pygame.transform.scale(self.game_over, (600, 600))

        self.chat_box = pygame.transform.scale(self.box, (700, 100))
        self.text_index = 0
        self.letter_index = 0

        self.font = pygame.font.Font("../assets/dialogs/dialog_font.ttf", 18)
        self.mana_font = pygame.font.Font("../assets/dialogs/dialog_font.ttf", 10)
        self.money_font = pygame.font.Font("../assets/dialogs/dialog_font.ttf", 25)
        self.reading = False
        self.show_money = True

    def shop(self, screen):
        screen.blit(self.shop_box, (0, 0))

    def game_over_render(self, screen):
        screen.blit(self.game_over_box, (-30, 0))
        screen.blit(self.game_over, (100,20))

    def money_render(self, player,  screen, x = 780, y = 10):
        if self.show_money:
            text = self.money_font.render(f"{player.money} $", False, (0, 0, 0))
            screen.blit(text, text.get_rect(topright=(x, y)))

    def mana_render(self, player,  screen):
        if not self.show_money:
            text = self.font.render(f"{player.mana} / {player.max_mana} mana", False, (102, 168, 238))
            screen.blit(text, text.get_rect(topleft=(0, 140)))

    def health_render(self, player, screen):
        if not self.show_money:
            text = self.font.render(f"{player.health} / {player.max_health} HP",False, (102, 238, 130))
            screen.blit(text, (player.bar_position[0], player.bar_position[1]-25))

    def NPC_health_render(self, NPC, screen):
        if not self.show_money:
            text = self.font.render(f"{NPC.health} / {NPC.max_health} HP",False, (102, 238, 130))
            screen.blit(text, text.get_rect(topleft=(NPC.bar_position[0]+280, NPC.bar_position[1]+30)))

    def fight_render(self, player, screen):
        texts = []
        screen.blit(self.fight_box, (self.fX_POSITION, self.fY_POSITION))
        for attack in player.actions:
            texts.append(self.font.render(f"{attack} : {player.actions[attack]}", False, (0, 0, 0)))

        x, y = 60,0
        for i in range(len(texts)):
            if i%2 == 0:
                x += 120*i//2
                y = 30
            else:
                y = 60
            screen.blit(texts[i], (self.fX_POSITION +x, self.fY_POSITION +y))

    def chat_execute(self, dialog=[]):
        if self.reading:
            self.next_text()
        else:
            self.reading = True
            self.text_index = 0
            self.texts = dialog

    def chat_render(self, screen):
        if self.reading:
            if self.letter_index < len(self.texts[self.text_index]):
                self.letter_index += 1

            screen.blit(self.chat_box, (self.X_POSITION, self.Y_POSITION))
            text = self.font.render(self.texts[self.text_index][0: self.letter_index], False, (0, 0, 0))
            screen.blit(text, (self.X_POSITION +60, self.Y_POSITION +30))

    def next_text(self):
        self.text_index += 1
        self.letter_index = 0

        if self.text_index >= len(self.texts):
            self.reading = False
