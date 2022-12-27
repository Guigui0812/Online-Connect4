import numpy as np
import pickle

ROW_COUNT = 6
COLUMN_COUNT = 7

# Represents the grid of the game
class Grid:

    def __init__(self):

        # Create a 2D list of 0
        self.matrix = np.zeros((ROW_COUNT,COLUMN_COUNT))
        self.listRowCpt = [5, 5, 5, 5, 5, 5, 5]

    def getSerialized(self):

        # dictionary that will be serialized
        DictOfserializedObject = { "matrix" : pickle.dumps(self.matrix), "listRowCpt" : pickle.dumps(self.listRowCpt) }

        # serialize the dictionary
        serializedObject = pickle.dumps(DictOfserializedObject)
        # return the serialized object
        return serializedObject

    # Check if the game is over
    def check_win(self, player):

        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if self.matrix[r][c] == player and self.matrix[r][c+1] == player and self.matrix[r][c+2] == player and self.matrix[r][c+3] == player:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if self.matrix[r][c] == player and self.matrix[r+1][c] == player and self.matrix[r+2][c] == player and self.matrix[r+3][c] == player:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if self.matrix[r][c] == player and self.matrix[r+1][c+1] == player and self.matrix[r+2][c+2] == player and self.matrix[r+3][c+3] == player:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if self.matrix[r][c] == player and self.matrix[r-1][c+1] == player and self.matrix[r-2][c+2] == player and self.matrix[r-3][c+3] == player:
                    return True