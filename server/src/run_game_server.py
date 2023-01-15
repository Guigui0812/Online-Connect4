import socket
import game_server

# Choses intéressantes à faire : 
# - joindre une base de données pour stocker les données des joueurs (victoires, compte etc...)
# - faire un système de classement pour les joueurs (pour afficher les meilleurs joueurs)
# - faire un système de statistiques pour les joueurs (pour afficher les statistiques des joueurs)
# - faire un système de sauvegarde pour les joueurs (pour sauvegarder les parties des joueurs)
# - Mettre en place le match nul

# build le server : docker build -t connect4_server:v1 .
# run le server : docker run -dp 12345:12345 --name Connect4Server connect4_server:v1

host, port = '0.0.0.0', 12345
player_number = 1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
print("server is listening on port", port)

while True:

    server_socket.listen() # the server listen for connections
    print("server is listening for connections")

    connection, address = server_socket.accept()
    print("connection from", address)

    game_server.ClientThread.number_of_clients += 1
    
    if game_server.ClientThread.number_of_clients % 2 == 1:
        game_server.Game.number_of_games.append(game_server.Game())

    client_thread = game_server.ClientThread(connection, game_server.Game.number_of_games[-1], player_number)
    player_number += 1
    client_thread.start()

    if player_number > 2:
        player_number = 1

#server_socket.close()