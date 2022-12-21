import pygame as pg
import numpy as np

import classes

# Represents a box in the grid (just visual)
class Box:
    
        # constructor
        def __init__(self, x, y, width, height):
            self.rect = pg.rect.Rect((x, y), (width, height))

        # draw an empty box
        def draw_empty(self, screen):
            pg.draw.circle(screen, "#DCDEE8", (self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2), 30)

        # draw a red box (player 1)
        def draw_red(self, screen):
            pg.draw.circle(screen, "#EA2A10", (self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2), 30)

        # draw a yellow box (player 2)
        def draw_yellow(self, screen):
            pg.draw.circle(screen, "#E3A509", (self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2), 30)