import pygame
import threading

# Improvmement: 
# - Use a thread to handle the waiting screen
# - Every 2 seconds, change the color of the text

class WaitingScreen(threading.Thread):

    def __init__(self, screen, width, height):
        threading.Thread.__init__(self)
        self._screen = screen
        self._running = True
        self._text = "En attente d\'un joueur..."
        self.width = width
        self.height = height
        self.font = pygame.font.Font('../assets/Starborn.ttf', 26)
        self.clock = pygame.time.Clock()

    def run(self):

        while self._running:
            self._screen.fill('#C2C5CD')
            text = self.font.render(self._text, True, "#DDDEEB")
            text_rect = text.get_rect(center=(self.width/2, self.height/2))
            self._screen.blit(text, text_rect)   
            pygame.display.update()
            self.clock.tick(60)

    def stop(self):
        self._running = False