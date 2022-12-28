import pygame as pg
import game

class SoloGame(game.Game):

    def __init__(self, _screen, width, height):
        game.Game.__init__(self, _screen,  width, height)

    def __check_win(self):

        if self._grid.check_win(self._player_number) == True:
            self._end = True

            # Display the winner _screen
        
    # game loop de la partie
    def start_game(self):

        pg.display.set_caption('Partie en cours')

        while self._end == False:

            # Fill the _screen with the background color depending on the self.self._player_number
            if self._player_number == 1:
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
                    mouse_x, mouse_y = pg.mouse.get_pos()            
                    
                    if self._grid.set_box(mouse_x, mouse_y, self._player_number) == True:

                        self.__check_win()

                        if self._player_number == 1:
                            self._player_number = 2
                        else:
                            self._player_number = 1