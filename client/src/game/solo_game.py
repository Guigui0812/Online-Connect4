import pygame
import game

# Class that handles the solo game
class SoloGame(game.Game):
    def __init__(self, _screen, width, height):
        game.Game.__init__(self, _screen, width, height)
        self.clock = pygame.time.Clock()

    def _check_win(self):

        if self._grid.check_win(self._active_player) == True:
            self._end = True
            self.game_song.stop()
            end_screen = game.EndScreen(self._screen, self.width, self.height, self._active_player)
            end_screen.display()

    # Change the player
    def _change_player(self):

        if self._active_player == 1:
            self._active_player = 2
        else:
            self._active_player = 1

    # Event handler
    def _event_loop(self, mouse_x):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self._grid.set_box(mouse_x, self._active_player, self._screen, self.layers[0]) == True:
                    coin_song = pygame.mixer.Sound('../assets/sounds/coin_song.wav')
                    coin_song.play()
                    self._check_win()
                    self._change_player()

    # game loop de la partie

    def start_game(self):

        pygame.display.set_caption("Puissance 4 - Solo Game")

        # Play a song in the background of the game infinite times
        self.game_song.play(-1)

        while self._end == False:

            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Update the _screen
            self._draw(mouse_x)
            self._render()
            self._display_player()
            pygame.display.update()

            # Event handler
            self._event_loop(mouse_x)

            # Set the FPS
            self.clock.tick(60)