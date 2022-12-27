import threading
import socket
import pickle


class Client_Thread(threading.Thread):

    nbClient = 0

# objet player pour gérer les joueurs (nom, couleur, victoires, défaite, égalité, etc...)
# objet game pour gérer la partie (grille, tour, fin de partie, victoire, etc...) (max 2 joueurs dans la même session de jeu)
# session terminée quand la partie est finie et que les joueurs ne veulent pas rejouer

    def __init__(self, conn, game, gameID):
        threading.Thread.__init__(self)
        self.conn = conn
        self.game = game
        self.gameID = gameID
        self.game.nbOfPlayers += 1

    def run(self):

        while True:

            data = self.conn.recv(1024)

            try:
                data = data.decode("utf8")

                if data == "get_player_nb":
                    self.send(str(self.gameID))

                elif data == "client_ready":
                    if self.game.game_ready():
                        self.send("server_ready")
                    else:
                        self.send("server_not_ready")

                elif data == "get_grid":
                    # get the serialized grid object
                    self.conn.sendall(self.game.grid.getSerialized())

                # get the active player
                elif data == "get_active_player":
                    self.send(str(self.game.active_player))

            except:
                # update the grid
                data = pickle.loads(data)

                

                self.send("grid_updated")
                self.game.grid.matrix = pickle.loads(data["matrix"])
                self.game.grid.listRowCpt = pickle.loads(data["listRowCpt"])

                # change the active player
                if self.game.active_player == 1:
                    self.game.active_player = 2
                else:
                    self.game.active_player = 1

    # methods that allows server to respond to client's requests

    def send(self, data):
        data = data.encode("utf8")
        self.conn.sendall(data)
