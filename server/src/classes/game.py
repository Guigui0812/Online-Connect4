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
        