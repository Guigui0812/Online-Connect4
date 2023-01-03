import pygame
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

        pygame.display.set_caption('Partie en cours')

        #text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((10, 10), (50, 50)), manager=self.gui_manager)

        while self._end == False:

            # Fill the _screen with the background color
            self.layers[0].fill('#F3F4FA')

            mouse_x, mouse_y = pygame.mouse.get_pos()   
            self._grid.draw_triangle(self.layers[0], mouse_x)
            self._grid.draw(self._screen, self.layers)

            self._screen.blit(self.layers[0], (0, 0))
            self._screen.blit(self.layers[1], (0, 0))
            
            #self.gui_manager.update(60/1000)
            #self.gui_manager.draw_ui(self._screen)

            pygame.display.update()

            # Event loop
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()

                #self.gui_manager.process_events(event)

                if event.type == pygame.MOUSEBUTTONDOWN:   
                             
                    if self._grid.set_box(mouse_x, self._player_number, self._screen, self.layers[0]) == True:

                        self.__check_win()

                        if self._player_number == 1:
                            self._player_number = 2
                        else:
                            self._player_number = 1