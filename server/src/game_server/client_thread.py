import threading
import pickle
import sys


class ClientThread(threading.Thread):

    number_of_clients = 0

    # objet player pour gérer les joueurs (nom, couleur, victoires, défaite, égalité, etc...)
    # objet game pour gérer la partie (grille, tour, fin de partie, victoire, etc...) (max 2 joueurs dans la même session de jeu)
    # session terminée quand la partie est finie et que les joueurs ne veulent pas rejouer

    def __init__(self, connection, game, session_identifier):
        threading.Thread.__init__(self)
        self.connection = connection
        self.game = game
        self.session_identifier = session_identifier
        self.game.number_of_players += 1

    def __handle_string_format_request(self, data):

        data = data.decode("utf8")

        if data == "get_player_nb":
            self.send(str(self.session_identifier))

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

        elif data == "close_client_network":
            self.game.player_left = True
            self.send("client_network_closed")

        elif data == "check_client_alive":

            if self.game.player_left == False:
                self.send("client_ok")
            else:
                self.send("client_lost")
                self.connection.close()
                sys.exit()
                
        elif data == "game_end":
            self.send("game_closed")
            self.connection.close()
            sys.exit()

    def __handle_dictionary_format_request(self, data):

        self.send("grid_updated")
        self.game.grid.box_status_matrix = pickle.loads(data["box_status_matrix"])
        self.game.grid.max_column_stacking = pickle.loads(data["max_column_stacking"])

        if self.game.check_win() == False:

            # change the active player
            if self.game.active_player == 1:
                self.game.active_player = 2
            else:
                self.game.active_player = 1

    def run(self):

        while True:

            data = self.connection.recv(1024)

            try:
                # if the data is a string
                self.__handle_string_format_request(data)

            except:

                # deserialize the data
                data = pickle.loads(data)

                # if is a dictionary process it
                if type(data) == dict:
                    self.__handle_dictionary_format_request(data)

    def send(self, data):
        data = data.encode("utf8")
        self.connection.sendall(data)
