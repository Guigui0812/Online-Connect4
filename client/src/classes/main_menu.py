import pygame as pg
import classes

class Main_Menu:

    def __init__(self, screen, widht, height):
        self.gameOver = False
        start_button = classes.Button('Jouer', (widht / 2 - 130, height / 2 - 20), screen)
        exit_button = classes.Button('Quitter', (widht / 2 - 130, height / 2 + 30), screen)
        self.buttons = [start_button, exit_button]
        self.screen = screen

    def __draw_menu(self):

        for button in self.buttons:
            button.draw(self.screen)

    def run_menu(self):

        while True:

            mousePos = pg.mouse.get_pos()
            self.screen.fill('#898A9C')
            self.__draw_menu()
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if(event.type == pg.MOUSEBUTTONDOWN):
                    if(self.buttons[0].rect.collidepoint(mousePos)):
                        game = classes.Game(self.screen)
                        game.startGame()

                    if(self.buttons[1].rect.collidepoint(mousePos)):
                        pg.quit()