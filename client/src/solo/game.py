import pygame as pg
import solo

# Représente une partie
class Game:

    def __init__(self, screen):
        self.gameOver = False
        self.screen = screen
        self.grid = solo.Grid()    
        
    def __check_win(self, player):

        # Check if the player won
        if self.grid.check_win(player) == True:
            self.gameOver = True
            # Display the winner screen
        
    # game loop de la partie
    def startGame(self):

        player = 1

        pg.display.set_caption('Partie en cours')

        while self.gameOver == False:

            # Fill the screen with the background color depending on the player
            if player == 1:
                self.screen.fill('#FA6565')
            else:
                self.screen.fill('#FAD065')

            self.grid.draw(self.screen)
            pg.display.update()

            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.MOUSEBUTTONDOWN:   
                    print("mouse down")
                    mouseX, mouseY = pg.mouse.get_pos()            
                    
                    if self.grid.set_box(mouseX, mouseY, player) == True:
                        self.__check_win(player)
                        if player == 1:
                            player = 2
                        else:
                            player = 1
            
            