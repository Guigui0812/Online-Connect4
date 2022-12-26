import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

# Represents the grid of the game
class Grid:

    def __init__(self):
        # Create a matrix of 0
        self.matrix = np.zeros((ROW_COUNT,COLUMN_COUNT)) 