import pygame as pg

import classes

# Représente une partie
class Game:

    def __init__(self, screen):
        self.gameOver = False
        self.screen = screen

    def startGame(self):

        while True:
            self.screen.fill('#EE550E')
            mousePos = pg.mouse.get_pos()
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if(event.type == pg.MOUSEBUTTONDOWN):
                    if(self.buttons[0].rect.collidepoint(mousePos)):
                        game = classes.Game(self.screen)
                        game.startGame()