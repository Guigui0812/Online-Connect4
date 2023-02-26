import socket
import game_server
import sys
import signal

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
running = True

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
print("server is listening on port", port)

# Gracefully close the server
def handle_signal(signum, frame):

    running = False

    print("Closing all client...")

    # Kill all threads
    for client in game_server.ClientThread.clients:
        client.close()
    
    print("Closing server socket...")

    server_socket.close()

    print("Exiting gracefully...")

    sys.exit(0)

# Handle signals to close the server properly
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)

# Main loop
while running:

    server_socket.listen() # the server listen for connections

    # accept the connection
    connection, address = server_socket.accept()

    # if there is a new connection, we create a new thread for it
    game_server.ClientThread.number_of_clients += 1
    
    if game_server.ClientThread.number_of_clients % 2 == 1:
        game_server.Game.number_of_games.append(game_server.Game())

    game_server.ClientThread.clients.append(game_server.ClientThread(connection, game_server.Game.number_of_games[-1], player_number))
    player_number += 1

    # Start new thread 
    game_server.ClientThread.clients[len(game_server.ClientThread.clients) - 1].start()

    if player_number > 2:
        player_number = 1