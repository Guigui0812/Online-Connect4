import pygame as pg
import classes

# Représente une partie
class Game:

    def __init__(self, screen):
        self.gameOver = False
        self.screen = screen
        self.grid = classes.Grid()

    # Affichage de la grille
    def print_board(self, Grid):       
        self.screen.blit(pg.transform.scale(pg.image.load("../assets/vide.png"), (70, 70)), (10, 10))

    def startGame(self):

        while self.gameOver == False:

            self.screen.fill('#EE550E')
            mousePos = pg.mouse.get_pos()
            
            self.print_board(self.grid)
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()