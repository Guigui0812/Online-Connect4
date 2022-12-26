import classes

# Représente une partie
class Game:

    games = []

    def __init__(self):
        self.grid = classes.Grid()
        self.active_player = 1
        self.end = False
        