import numpy as np
import pickle

ROW_COUNT = 6
COLUMN_COUNT = 7

# Represents the grid of the game
class Grid:

    def __init__(self):

        # Create a 2D list of 0
        self.box_status_matrix = np.zeros((ROW_COUNT,COLUMN_COUNT))
        self.max_column_stacking = [5, 5, 5, 5, 5, 5, 5]

    def get_serialized_box_status_matrix(self):

        # dictionary that will be serialized
        DictOfserializedObject = { "box_status_matrix" : pickle.dumps(self.box_status_matrix), "max_column_stacking" : pickle.dumps(self.max_column_stacking) }

        # serialize the dictionary
        serializedObject = pickle.dumps(DictOfserializedObject)
        # return the serialized object
        return serializedObject

    # Check if the game is over
    def check_win(self, player):

        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r][c+1] == player and self.box_status_matrix[r][c+2] == player and self.box_status_matrix[r][c+3] == player:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r+1][c] == player and self.box_status_matrix[r+2][c] == player and self.box_status_matrix[r+3][c] == player:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r+1][c+1] == player and self.box_status_matrix[r+2][c+2] == player and self.box_status_matrix[r+3][c+3] == player:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r-1][c+1] == player and self.box_status_matrix[r-2][c+2] == player and self.box_status_matrix[r-3][c+3] == player:
                    return True