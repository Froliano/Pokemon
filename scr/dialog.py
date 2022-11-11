import pygame


class DialogBox:

    X_POSITION = 60
    Y_POSITION = 470

    fX_POSITION = 420
    fY_POSITION = 480

    def __init__(self):
        self.box = pygame.image.load("../assets/dialogs/dialog_box.png")

        self.fight_box = pygame.transform.scale(self.box, (400, 120))

        self.game_over_box = pygame.transform.scale(self.box, (860, 600))
        self.game_over = pygame.image.load("../assets/dialogs/game_over.png")
        self.game_over = pygame.transform.scale(self.game_over, (600, 600))

        self.chat_box = pygame.transform.scale(self.box, (700, 100))
        self.text_index = 0
        self.letter_index = 0

        self.font = pygame.font.Font("../assets/dialogs/dialog_font.ttf", 18)
        self.reading = False

    def game_over_render(self, screen):
        screen.blit(self.game_over_box, (-30, 0))
        screen.blit(self.game_over, (100,20))

    def fight_render(self, screen):
        screen.blit(self.fight_box, (self.fX_POSITION, self.fY_POSITION))
        text1 = self.font.render("1: attack", False, (0, 0, 0))
        text2 = self.font.render("2: heal", False, (0, 0, 0))
        screen.blit(text1, (self.fX_POSITION +60, self.fY_POSITION +30))
        screen.blit(text2, (self.fX_POSITION +60, self.fY_POSITION +70))

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
