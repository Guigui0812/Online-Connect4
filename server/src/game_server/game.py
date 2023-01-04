import game_server

# Représente une partie
class Game:

    number_of_games = []

    def __init__(self):
        self.grid = game_server.Grid()
        self.active_player = 1
        self.end = False
        self.number_of_players = 0
        self.player_left = False

    def game_ready(self):
        if self.number_of_players == 2:
            return True
        else:
            return False

    def check_win(self):
        if self.grid.check_win(self.active_player) == True:
            self.end = True
            return True
        else:
            return False
