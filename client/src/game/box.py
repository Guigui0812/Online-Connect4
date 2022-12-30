import pygame
import pygame.gfxdraw

# Represents a box in the grid (just visual)
class Box:
    
        # constructor
        def __init__(self, x, y, width, height):
            self.rect = pygame.rect.Rect((x, y), (width, height))

        # draw an empty box
        def draw_empty(self, screen):

            pygame.gfxdraw.filled_circle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 30, (194, 197, 205))
            pygame.gfxdraw.aacircle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 30, (194, 197, 205))

        # draw a red box (player 1)
        def draw_red(self, screen):
            pygame.gfxdraw.filled_circle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 30, (223, 59, 15))
            pygame.gfxdraw.aacircle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 30,(223, 59, 15))

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 25, (254, 91, 47))
            pygame.gfxdraw.aacircle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 25, (254, 91, 47))

        # draw a yellow box (player 2)
        def draw_yellow(self, screen):
            pygame.gfxdraw.filled_circle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 30, (61, 120, 255))
            pygame.gfxdraw.aacircle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 30, (61, 120, 255))

            pygame.gfxdraw.filled_circle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 25, (111, 153, 250))
            pygame.gfxdraw.aacircle(screen, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 25, (111, 153, 250))