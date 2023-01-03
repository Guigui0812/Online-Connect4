import game
import pygame

# Représente une partie
class Game():

    def __init__(self, screen, width, height):
        self._end = False
        self._screen = screen
        self._player_number = 1
        self._grid = game.Grid()     
        self.width = width
        self.height = height
        self.layers = [ pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA) for i in range(2)]
        self.clock = pygame.time.Clock()
        
    def _check_win(self):
        pass

    def start_game(self):
        pass

    def _draw(self):
        pass

    def _event_loop(self):
        pass
    
    def _update(self):
        pass