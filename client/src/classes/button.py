import pygame as pg

class Button:

    def __init__(self, txt, pos, screen):
        self.string = txt
        self.pos = pos
        self.font = pg.font.Font('freesansbold.ttf', 32)
        self.screen = screen
        self.rect = pg.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self, screen):

        # Draw the button
        pg.draw.rect(screen, "#4049E7", self.rect)       
        text = self.font.render(self.string, True, "#DDDEEB")
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.rect.collidepoint(pg.mouse.get_pos()) and pg.mouse.get_pressed()[0]:
            return True
        else:
            return False