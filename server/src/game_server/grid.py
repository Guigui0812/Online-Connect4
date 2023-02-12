import json

ROW_COUNT = 6
COLUMN_COUNT = 7

# Represents the grid of the game
class Grid:

    # Constructor
    def __init__(self):

        # Create a 2D list of 0
        self.box_status_matrix = [[0 for j in range(COLUMN_COUNT)] for i in range(ROW_COUNT)]
        self.max_column_stacking = [5, 5, 5, 5, 5, 5, 5]

    # Serialize the grids to send it to the client with JSON
    def get_serialized_matrix(self):
    
        serialized_objects_dict = {
            "box_status_matrix": self.box_status_matrix,
            "max_column_stacking": self.max_column_stacking
        }
        
        json_serialized_objects_dict = json.dumps(serialized_objects_dict)
       
        return json_serialized_objects_dict

    # Check if the game is over
    def check_win(self, player):

        # Check horizontal locations for win
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if (
                    self.box_status_matrix[r][c] == player
                    and self.box_status_matrix[r][c + 1] == player
                    and self.box_status_matrix[r][c + 2] == player
                    and self.box_status_matrix[r][c + 3] == player
                ):
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if (
                    self.box_status_matrix[r][c] == player
                    and self.box_status_matrix[r + 1][c] == player
                    and self.box_status_matrix[r + 2][c] == player
                    and self.box_status_matrix[r + 3][c] == player
                ):
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if (
                    self.box_status_matrix[r][c] == player
                    and self.box_status_matrix[r + 1][c + 1] == player
                    and self.box_status_matrix[r + 2][c + 2] == player
                    and self.box_status_matrix[r + 3][c + 3] == player
                ):
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if (
                    self.box_status_matrix[r][c] == player
                    and self.box_status_matrix[r - 1][c + 1] == player
                    and self.box_status_matrix[r - 2][c + 2] == player
                    and self.box_status_matrix[r - 3][c + 3] == player
                ):
                    return True
