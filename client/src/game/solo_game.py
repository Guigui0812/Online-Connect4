import pygame as pg
import game

class Solo_Game(game.Game):

    def __init__(self, _screen):
        game.Game.__init__(self, _screen)

    def __check_win(self):

        if self._grid.check_win(self._playerNb) == True:
            self._gameOver = True

            # Display the winner _screen
        
    # game loop de la partie
    def start_game(self):

        pg.display.set_caption('Partie en cours')

        while self._gameOver == False:

            # Fill the _screen with the background color depending on the self.self._playerNb
            if self._playerNb == 1:
                self._screen.fill('#FA6565')
            else:
                self._screen.fill('#FAD065')

            self._grid.draw(self._screen)
            pg.display.update()

            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.MOUSEBUTTONDOWN:   
                    print("mouse down")
                    mouseX, mouseY = pg.mouse.get_pos()            
                    
                    if self._grid.set_box(mouseX, mouseY, self._playerNb) == True:
                        self.__check_win()
                        if self._playerNb == 1:
                            self._playerNb = 2
                        else:
                            self._playerNb = 1