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