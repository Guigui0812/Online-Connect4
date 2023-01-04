import pygame
import pygame.gfxdraw
import threading

# Represents a box in the grid (just visual)
class Box:

    # constructor
    def __init__(self, x, y, width, height):
        self.rect = pygame.rect.Rect((x, y), (width, height))
        self.y = 45

    # draw an empty box
    def draw_empty(self, surface):

        pygame.gfxdraw.filled_circle(
            surface,
            int(self.rect.x + self.rect.width / 2),
            int(self.rect.y + self.rect.height / 2),
            30,
            (243, 244, 250, 0),
        )

    # draw a red box (player 1)
    def draw_red(self, surface):

        if self.y == self.rect.y:

            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.rect.y + self.rect.height / 2),
                35,
                (223, 59, 15),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 35,(223, 59, 15))

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.rect.y + self.rect.height / 2),
                25,
                (254, 91, 47),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 20, (254, 91, 47))

        else:

            # draw a red circle
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                35,
                (223, 59, 15),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.y + self.rect.height/2), 35,(223, 59, 15))

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                25,
                (254, 91, 47),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.y + self.rect.height/2), 20, (254, 91, 47))

    # draw a yellow box (player 2)
    def draw_yellow(self, surface):

        if self.y == self.rect.y:

            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.rect.y + self.rect.height / 2),
                35,
                (61, 120, 255),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 35, (61, 120, 255))

            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.rect.y + self.rect.height / 2),
                25,
                (111, 153, 250),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.rect.y + self.rect.height/2), 25, (111, 153, 250))

        else:

            # draw a red circle
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                35,
                (61, 120, 255),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.y + self.rect.height/2), 35, (61, 120, 255))

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                25,
                (111, 153, 250),
            )
            # pygame.gfxdraw.aacircle(surface, int(self.rect.x + self.rect.width/2), int(self.y + self.rect.height/2), 25, (111, 153, 250))

    def animate(self):

        if self.y < self.rect.y:
            self.y += 1