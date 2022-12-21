import pygame as pg
import numpy as np

import classes

ROW_COUNT = 6
COLUMN_COUNT = 7

class Grid:

    def __init__(self):
        # Création d'une matrice 6x7
        self.stateMatrix = np.zeros((ROW_COUNT,COLUMN_COUNT))     
        self.visualMatrix = np.full((ROW_COUNT, COLUMN_COUNT), None)

        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.visualMatrix[i][j] = classes.Box(55 + j * 70, 120 + i * 70, 70, 70)

    def draw(self, screen):

        self.rect = pg.rect.Rect((55, 120), (490, 420))
        pg.draw.rect(screen, "#2B3FE8", self.rect, 0, 5) 
        print(self.stateMatrix)
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if(self.stateMatrix[i][j] == 0):
                    self.visualMatrix[i][j].draw_empty(screen)
                elif (self.stateMatrix[i][j] == 1):
                    self.visualMatrix[i][j].draw_red(screen)

    def set_box(self, x, y, player):

        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if self.visualMatrix[i][j].rect.collidepoint(x, y):
                    if self.stateMatrix[i][j] == 0:
                        self.stateMatrix[i][j] = player
                    