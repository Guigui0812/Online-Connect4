import pygame as pg
import numpy as np

import classes

class Box:
    
        def __init__(self, x, y, width, height):
            self.rect = pg.rect.Rect((x, y), (width, height))

        def draw_empty(self, screen):
            pg.draw.circle(screen, "#9C9FA8", (self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2), 30)

        def draw_red(self, screen):
            pg.draw.circle(screen, "#EA2A10", (self.rect.x + self.rect.width/2, self.rect.y + self.rect.height/2), 30)