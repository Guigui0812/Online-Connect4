import pygame as pg
import numpy as np

import classes

class Board:

    def __init__(self):
        self.matrix = np.zeros((6,7))     

    def print_board(self):
        print(self.matrix)