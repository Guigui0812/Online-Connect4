import pygame as pg

# Improvmement: 
# - Use a thread to handle the waiting screen
# - Every 2 seconds, change the color of the text

class WaitingScreen():

    def __init__(self, screen, width, height):
        self._screen = screen
        self._running = True
        self._text = "En attente d\'un joueur..."
        self.width = width
        self.height = height
        self.font = pg.font.Font('../assets/Starborn.ttf', 26)

    def draw(self):
        self._screen.fill('#898A9C')
        text = self.font.render(self._text, True, "#DDDEEB")
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self._screen.blit(text, text_rect)   
        pg.display.update()