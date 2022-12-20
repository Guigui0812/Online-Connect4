import pygame as pg
import sys
import classes

class Main_Menu:

    def __init__(self, screen, widht, height):
        self.gameOver = False
        start_button = classes.Button(
            'Jouer', (widht / 2 - 130, height / 2 - 20), screen)
        self.buttons = [start_button]
        self.screen = screen

    def draw_menu(self):

        for button in self.buttons:
            button.draw(self.screen)

    def run_menu(self):

        while True:

            self.screen.fill('#898A9C')
            self.draw_menu()
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
