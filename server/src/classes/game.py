import classes

# Représente une partie
class Game:

    games = []

    def __init__(self):
        self.grid = classes.Grid()
        self.active_player = 1
        self.end = False
        self.nbOfPlayers = 0

    def game_ready(self):
        if self.nbOfPlayers == 2:
            return True
        else:
            return False

    def check_win(self):

        if self.grid.check_win(self.active_player) == True:
            self.end = True
            return True
        else:
            return False