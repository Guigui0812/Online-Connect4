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

        # draw a white circle (empty box) to represent the box when it's empty
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

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.rect.y + self.rect.height / 2),
                25,
                (254, 91, 47),
            )

        else:

            # draw a red circle
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                35,
                (223, 59, 15),
            )

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                25,
                (254, 91, 47),
            )

    # draw a blue box (player 2)
    def draw_blue(self, surface):

        if self.y == self.rect.y:

            # draw a blue circle
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.rect.y + self.rect.height / 2),
                35,
                (61, 120, 255),
            )

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.rect.y + self.rect.height / 2),
                25,
                (111, 153, 250),
            )

        else:

            # draw a red circle
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                35,
                (61, 120, 255),
            )

            # draw an other circle inside the first one with the same color but a little bit darker
            pygame.gfxdraw.filled_circle(
                surface,
                int(self.rect.x + self.rect.width / 2),
                int(self.y + self.rect.height / 2),
                25,
                (111, 153, 250),
            )

    # animate the cicle to fall down when a player put a coin in it
    def animate(self):

        if self.y < self.rect.y:
            self.y += 5