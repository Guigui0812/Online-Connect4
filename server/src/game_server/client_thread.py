import threading
import pickle
import re
import time

class ClientThread(threading.Thread):

    # Number of client currently connected
    number_of_clients = 0

    # List of all the clients
    clients = []

    # objet player pour gérer les joueurs (nom, couleur, victoires, défaite, égalité, etc...)
    # objet game pour gérer la partie (grille, tour, fin de partie, victoire, etc...) (max 2 joueurs dans la même session de jeu)
    # session terminée quand la partie est finie et que les joueurs ne veulent pas rejouer

    def __init__(self, connection, game, session_identifier):
        threading.Thread.__init__(self)
        self.connection = connection
        self.game = game
        self.session_identifier = session_identifier
        self.game.number_of_players += 1
        self.timer = time.time()

    # Management of the strings request type
    def __handle_string_format_request(self, data):

        data = data.decode("utf8")

        # Depending of the message, specfic actions are processed

        # Send the client his player number
        if "set_player_nb_and_name" in data:
            
            if (self.session_identifier == 1):
                player_name = re.split("\s", data)
                self.game.player1_name = player_name[1]
            else:
                player_name = re.split("\s", data)
                self.game.player2_name = player_name[1]

            self.send(str(self.session_identifier))

        elif data == "keep_alive" :
            self.timer = time.time()
            self.send("keep_alive")

        # Send the state of the server (ready or not)
        elif data == "client_ready":
            if self.game.game_ready():
                self.send("server_ready")
            else:
                self.send("server_not_ready")

        # send the grid to the client so that it can update his one
        elif data == "get_grid":
            # get the serialized grid object
            self.connection.sendall(self.game.grid.get_serialized_box_status_matrix())

        # get the active player in the current game session
        elif data == "get_active_player":
            self.send(str(self.game.active_player))

        # The server check if the current game is win
        elif data == "check_win":

            # if the game is ended, there's a winner
            if self.game.end == True:
                if self.game.active_player == 1:
                    self.send("Player 1 win")
                    
                else:
                    self.send("Player 2 win")
            else:
                self.send("no_win")

        # Signal to handle the closing of the app by the client
        elif data == "close_client_network":
            self.game.player_left = True
            self.send("client_network_closed")

        # Check if the client is alive, if it leaves the game, the server needs to close the connection
        elif data == "check_client_alive":

            if self.game.player_left == False:
                self.send("client_ok")
            else:
                print("Client left")
                self.send("client_lost")
                self.connection.close()
                self.join()
        
        # Instruction to handle the end of the game and finish it
        elif data == "game_end":
            self.send("game_closed")
            self.connection.close()
            self.join()

    # Manages the "none-string" request (it's just dictionnaries in our case)
    def __handle_dictionary_format_request(self, data):

        # When we receive a dictionnary, it's the updated grid of the client --> Deserialization
        self.send("grid_updated")
        self.game.number_of_turns = self.game.number_of_turns+1
        self.game.grid.box_status_matrix = pickle.loads(data["box_status_matrix"])
        self.game.grid.max_column_stacking = pickle.loads(data["max_column_stacking"])

        # Handle the player change
        if self.game.check_win() == False:
        
            # change the active player
            if self.game.active_player == 1 and self.game.end == False:
                self.game.active_player = 2
            elif self.game.active_player == 2 and self.game.end == False:
                self.game.active_player = 1

    def close(self):
        self.connection.close()
        self.join()

    # Run methods of the client thread
    def run(self):

        # infinite loop
        while True:

            current_time = time.time()
            if current_time - self.timer > 10:
                print("Client left")

            # Check if it receives a data, and tryto handle it via the string method, if not it's a dictionnary
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

    # Method to send "string" data to the client
    def send(self, data):
        data = data.encode("utf8")
        self.connection.sendall(data)