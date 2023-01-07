import pygame
import game

# Class that handles the solo game
class SoloGame(game.Game):
    def __init__(self, _screen, width, height):
        game.Game.__init__(self, _screen, width, height)

    def _check_win(self):

        if self._grid.check_win(self._player_number) == True:
            self._end = True
            # Display the winner _screen

    # Change the player
    def _change_player(self):

        if self._player_number == 1:
            self._player_number = 2
        else:
            self._player_number = 1

    # Event handler
    def _event_loop(self, mouse_x):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._grid.set_box(mouse_x, self._player_number, self._screen, self.layers[0]) == True:
                    self._check_win()
                    self._change_player()

    # game loop de la partie

    def start_game(self):

        pygame.display.set_caption("Partie en cours")

        while self._end == False:

            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Update the _screen
            self._draw(mouse_x)
            self._render()
            pygame.display.update()

            # Event handler
            self._event_loop(mouse_x)

            # Set the FPS
            self.clock.tick(60)