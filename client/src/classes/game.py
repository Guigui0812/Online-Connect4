import pygame as pg
import classes

# Représente une partie
class Game:

    def __init__(self, screen):
        self.gameOver = False
        self.screen = screen
        self.grid = classes.Grid()    
        
    # game loop de la partie
    def startGame(self):

        while self.gameOver == False:

            print("game loop")
            self.screen.fill('#9C9FA8')
                  
            self.grid.draw(self.screen)
            pg.display.update()

            # Gestion des évènements
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if(event.type == pg.MOUSEBUTTONDOWN):      
                        mouseX, mouseY = pg.mouse.get_pos()            
                        self.grid.set_box(mouseX, mouseY, 1)
