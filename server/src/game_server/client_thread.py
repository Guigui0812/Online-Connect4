import threading
import json
import re
import time
import sys 

class ClientThread(threading.Thread):

    # Number of client currently connected to the server
    number_of_clients = 0

    # List of all the clients connected to the server
    clients = []

    # objet player pour gérer les joueurs (nom, couleur, victoires, défaite, égalité, etc...)
    # objet game pour gérer la partie (grille, tour, fin de partie, victoire, etc...) (max 2 joueurs dans la même session de jeu)
    # session terminée quand la partie est finie et que les joueurs ne veulent pas rejouer

    # Constructor of the client thread
    def __init__(self, connection, game, session_identifier):
        threading.Thread.__init__(self)
        self.connection = connection
        self.game = game
        self.session_identifier = session_identifier
        self.game.number_of_players += 1
        self.timer = time.time()
        self.connected = True

    # Method to send data to the client
    def send(self, data):
        print("sending data to client: " + data)
        data = data.encode("utf8")
        self.connection.sendall(data)

    # Management of the strings request type
    def __handle_string_format_request(self, data):

        message = data 
        data = data["request_type"]
        print(data)

        # Send the client his player number
        if "set_player_nb_and_name" == data:
            
            if (self.session_identifier == 1):      
                self.game.player1_name = message["player_name"]
            else:
                self.game.player2_name = message["player_name"]

            self.send(str(self.session_identifier))

        # Send the state of the server (ready or not)
        elif data == "client_ready":
            if self.game.game_ready():
                self.send("server_ready")
            else:
                self.send("server_not_ready")

        # send the grid to the client so that it can update his one
        elif data == "get_grid":
            print("sending grid to client")
            # get the serialized grid object
            self.send(self.game.grid.get_serialized_matrix())

        # get the active player in the current game session
        elif data == "get_active_player":
            self.send(str(self.game.active_player))

        # The server check if the current game is win
        elif data == "check_win":

            # if the game is ended, there's a winner
            if self.game.end == True:
                if self.game.active_player == 1:

                    # send a json message to the client to display the winner
                    json_message = {"message_type" : "win", "winner" : self.game.player1_name}
                    self.send(json.dumps(json_message))               
                else:
                    json_message = {"message_type" : "win", "winner" : self.game.player1_name}
                    self.send(json.dumps(json_message))
            else:

                # if the game is not ended, there's no winner
                json_message = {"message_type" : "no_win"}
                self.send(json.dumps(json_message))
        
        # Instruction to handle the end of the game and finish it
        elif data == "game_end":

            self.send("game_closed")
            time.sleep(3)
            self.player_left = True
            self.connected = False

    # Method to handle the keep alive request
    def __handle_keep_alive(self):
        
        # If the player is still connected, we reset the timer
        if self.game.player_left == False and self.game.end == False:      
            self.timer = time.time()
            self.send("keep_alive")
        else:
            self.send("player_lost")
            print("player lost")

    # Manages the "none-string" request (it's just dictionnaries in our case)
    def __handle_dictionary_format_request(self, lastGrid):

        # When we receive a dictionnary, it's the updated grid of the client --> Deserialization
        self.send("grid_updated")
        self.game.number_of_turns = self.game.number_of_turns+1

        self.game.grid.box_status_matrix = lastGrid["box_status_matrix"]
        self.game.grid.max_column_stacking = lastGrid["max_column_stacking"]

        # Handle the player change
        if self.game.check_win() == False:
        
            # change the active player
            if self.game.active_player == 1 and self.game.end == False:
                self.game.active_player = 2
            elif self.game.active_player == 2 and self.game.end == False:
                self.game.active_player = 1

    # Close the client thread and the connection
    def close(self):
        print("Closing client thread")
        self.connection.close()
        sys.exit()

    # Run methods of the client thread
    def run(self):

        # Loop to handle the client requests
        while self.connected:

            # Check if it receives a data, and try to handle it via the string method, if not it's a dictionnary
            data = self.connection.recv(2048)
            
            # If the data is not empty, it's a request
            if data != b'':

                # Display the received data for logging purpose
                print(data)

                # Try to decode the data and load it as a json object
                try:
                    data = data.decode("utf8")
                    data = json.loads(data)
                    
                    if data["message_type"] == "game_request":
                        self.__handle_string_format_request(data)
                    elif data["message_type"] == "keep_alive":
                        self.__handle_keep_alive()
                    elif data["message_type"] == "grid":
                        self.__handle_dictionary_format_request(data)

                # If the data is not handled, it's probably because it's truncated or unhandled
                except:
                    print("error : data not handled or truncated : ", data)                   
                
            # Check if the client is still connected with a timer, if not, close the client thread
            current_time = time.time()
            if current_time - self.timer > 15:
                print("player lost, game ended")
                self.connected = False
                self.game.player_left = True
                self.close()

        self.close()