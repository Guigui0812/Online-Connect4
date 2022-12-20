import pygame as pg
import numpy as np

import classes

ROW_COUNT = 6
COLUMN_COUNT = 7

class Grid:

    def __init__(self):
        # Création d'une matrice 6x7
        self.matrix = np.zeros((ROW_COUNT,COLUMN_COUNT))     