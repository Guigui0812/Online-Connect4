import threading
import pickle

class ClientThread(threading.Thread):

    number_of_clients = 0

# objet player pour gérer les joueurs (nom, couleur, victoires, défaite, égalité, etc...)
# objet game pour gérer la partie (grille, tour, fin de partie, victoire, etc...) (max 2 joueurs dans la même session de jeu)
# session terminée quand la partie est finie et que les joueurs ne veulent pas rejouer

    def __init__(self, connection, game, sessionIdentifier):
        threading.Thread.__init__(self)
        self.connection = connection
        self.game = game
        self.sessionIdentifier = sessionIdentifier
        self.game.number_of_players += 1

    def run(self):

        while True:

            data = self.connection.recv(1024)

            try:
                data = data.decode("utf8")

                if data == "get_player_nb":
                    self.send(str(self.sessionIdentifier))

                elif data == "client_ready":
                    if self.game.game_ready():
                        self.send("server_ready")
                    else:
                        self.send("server_not_ready")

                elif data == "get_grid":
                    # get the serialized grid object
                    self.connection.sendall(self.game.grid.get_serialized_box_status_matrix())

                # get the active player
                elif data == "get_active_player":
                    self.send(str(self.game.active_player))

                elif data == "check_win":

                    if self.game.end == True:                    
                        if self.game.active_player == 1:
                            self.send("Player 1 win")
                        else:
                            self.send("Player 2 win")
                    else:
                        self.send("no_win")

            except:
                # update the grid
                data = pickle.loads(data)

                # if is a dictionary process it
                if type(data) == dict:
            
                    self.send("grid_updated")
                    self.game.grid.box_status_matrix = pickle.loads(data["box_status_matrix"])
                    self.game.grid.max_column_stacking = pickle.loads(data["max_column_stacking"])

                    if self.game.check_win() == False:
                        # change the active player
                        if self.game.active_player == 1:
                            self.game.active_player = 2
                        else:
                            self.game.active_player = 1
    
    # send a string to the client
    def send(self, data):
        data = data.encode("utf8")
        self.connection.sendall(data)
