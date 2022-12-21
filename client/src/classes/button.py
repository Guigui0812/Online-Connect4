import pygame as pg

class Button:

    def __init__(self, txt, pos, screen):
        self.string = txt
        self.pos = pos
        self.font = pg.font.Font('../assets/Starborn.ttf', 26)
        self.screen = screen
        self.rect = pg.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self, screen):

        # Draw the button rect
        pg.draw.rect(screen, "#4049E7", self.rect) 

        # Write text and center it
        text = self.font.render(self.string, True, "#DDDEEB")
        text_rect = text.get_rect(center = self.rect.center)
        screen.blit(text, text_rect)

    def check_clicked(self):
        if self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            return True
        else:
            return False