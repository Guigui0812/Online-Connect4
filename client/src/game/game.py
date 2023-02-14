import game
import pygame

# Class that represents the motherclass "Game"
class Game:
    
    def __init__(self, screen, width, height):
        self._end = False
        self._screen = screen
        self._active_player = 1
        self._grid = game.Grid()
        self.width = width
        self.height = height
        self.layers = [pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA) for i in range(2)]
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 40)
        self.game_song = pygame.mixer.Sound('../assets/sounds/game_song.wav')

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

    # Display the player who is playing
    def _display_player(self):
        
        if self._active_player == 1:
            color = (254, 91, 47)
            title = "Tour du joueur 1"
        else:
            color = (61, 120, 255)
            title = "Tour du joueur 2"

        text = self.font.render(title, True, color)
        text_rect = text.get_rect(center=(self.width/2, 40))
        self._screen.blit(text, text_rect)  

    def _end_game(self):
        
        if self._active_player == 1:
            color = (254, 91, 47)
            title = "Le joueur 1 a gagné !"
        else:
            color = (61, 120, 255)
            title = "Le joueur 2 a gagné !"

        text = self.font.render(title, True, color)
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self._screen.blit(text, text_rect)