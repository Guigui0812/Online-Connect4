import game
import pygame

# Class that represents the motherclass "Game"
class Game:
    
    def __init__(self, screen, width, height):
        self._end = False
        self._screen = screen
        self._player_number = 1
        self._grid = game.Grid()
        self.width = width
        self.height = height
        self.layers = [pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA) for i in range(2)]
        self.clock = pygame.time.Clock()

    # Abstract methods that must be implemented in the child classes
    def _check_win(self):
        pass

    # Abstract methods that must be implemented in the child classes
    def start_game(self):
        pass

    # Draw the game board
    def _draw(self, mouse_x):    
        self.layers[0].fill("#F3F4FA")
        self._grid.draw_triangle(self.layers[0], mouse_x)
        self._grid.draw(self.layers)

    # Render the game board
    def _render(self):
        self._screen.blit(self.layers[0], (0, 0))
        self._screen.blit(self.layers[1], (0, 0))

    # Abstract methods that must be implemented in the child classes
    def _event_loop(self):
        pass