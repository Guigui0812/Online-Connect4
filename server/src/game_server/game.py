import game_server
import time

# Represents a game session on the server
class Game:

    # Number of currently running game sessions
    number_of_games = []

    # Contains all game session informations
    def __init__(self):
        self.grid = game_server.Grid()
        self.active_player = 1
        self.end = False
        self.number_of_players = 0
        self.player_left = False
        self.number_of_turns = 0
        self.game_start_time = 0
        self.game_end_time = 0
        self.player1_name = ""
        self.player2_name = ""

    # Method that checks if the condition to begin a game is fulfilled
    def game_ready(self):
        if self.number_of_players == 2:
            self.game_start_time = time.time()
            return True
        else:
            return False

    # Method that check if the game is win
    def check_win(self):
        if self.grid.check_win(self.active_player) == True:
            self.end = True
            self.game_end_time = time.time()
            return True
        else:
            return False
