import pygame
import threading
import pygame.gfxdraw
import math

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

        radius = 50
        x, y = 320, 240
        color = (255, 255, 255)
        counter = 0
        num_frames = 60

        while self._running:

            self._screen.fill('#C2C5CD')
            
            angle = 360 * counter / num_frames
    
            # Calculate the new position of the circle based on the angle
            x = int(320 + radius * math.cos(math.radians(angle)))
            y = int(240 + radius * math.sin(math.radians(angle)))
            
            # Draw the circle to the screen with anti-aliasing and fill
            pygame.gfxdraw.filled_circle(self._screen, x, y, radius, color)
                   
            pygame.display.update()
            counter += 1
            
            if counter == num_frames:
                counter = 0

            self.clock.tick(60)

    def stop(self):
        self._running = False