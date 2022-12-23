import socket
import threading

# Ici, en fonction de la valeur qu'aura la data, on pourra faire des actions différentes :
# - si data == "getGrid", on envoie la grille au client qui l'a demandé
# - si data == "getPlayers", on envoie la liste des joueurs au client qui l'a demandé
# - si data == "setPlayerCoin", on place la pièce du joueur sur la grille aux bonnes coordonnées

class GameNetworkTread(threading.Thread):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.socket.bind((self.host, self.port))
        print("server is running on", self.host, self.port)

        while True:
            self.socket.listen() # the server listen for connections
            print("server is listening for connections")
            connection, address = self.socket.accept()
            print("connection from", address)
            data = connection.recv(1024)
            data = data.decode("utf8")
            print(data)
            connection.sendall(b"Hello, world!")

        connection.close()
        socker.close()