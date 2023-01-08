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
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 30)
        self.clock = pygame.time.Clock()
        self.waiting_song = pygame.mixer.Sound('../assets/sounds/waiting_song.wav')

    def run(self):

        radius = 10
        x, y = 300, 320
        color = (61, 120, 255)
        counter = 0
        num_frames = 60

        self.waiting_song.play(-1)

        while self._running:

            self._screen.fill('#F3F4FA')

            text = self.font.render(self._text, True, (223, 59, 15))
            text_rect = text.get_rect(center=(self.width/2, self.height/2))
            self._screen.blit(text, text_rect)   
            
            angle = 360 * counter / num_frames
    
            # Calculate the new position of the circle based on the angle
            x = int(300 + radius * math.cos(math.radians(angle)))
            y = int(350 + radius * math.sin(math.radians(angle)))
            
            # Draw the circle to the screen with anti-aliasing and fill
            pygame.gfxdraw.filled_circle(self._screen, x, y, radius, color)
                   
            pygame.display.update()
            counter += 1
            
            if counter == num_frames:
                counter = 0

            self.clock.tick(60)

    def stop(self):
        self._running = False
        self.waiting_song.stop()