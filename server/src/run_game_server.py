import socket
import game

# Ici, en fonction de la valeur qu'aura la data, on pourra faire des actions différentes :
# - si data == "getGrid", on envoie la grille au client qui l'a demandé
# - si data == "getPlayers", on envoie la liste des joueurs au client qui l'a demandé
# - si data == "setPlayerCoin", on place la pièce du joueur sur la grille aux bonnes coordonnées
# - données sous forme de dictionnaire (json) pour pouvoir envoyer plusieurs données en même temps
# - gérer le blocage des threads pour éviter les erreurs de concurrence
# - booléen de tour : si c'es le tour du joueur, on peut placer une pièce, sinon on ne peut pas (réponse négative au client)
# - booléen de fin de partie : si la partie est finie, on ne peut plus placer de pièce (réponse négative au client)
# - booléen de victoire : si le joueur a gagné, on ne peut plus placer de pièce (réponse négative au client)
# - gérer la déconnexion des joueurs (si un joueur se déconnecte, on fait un système de reconnexion)
# - Dans le client jouer un son quand on place une pièce
# - Dans le client, mettre une musique de fond

# Choses intéressantes à faire : 
# - joindre une base de données pour stocker les données des joueurs (victoires, compte etc...)
# - Docker-compose pour lancer le serveur et la base de données en même temps 
# - faire un système de chat pour les joueurs
# - faire un système de lobby pour les joueurs (pour attendre le premier joueur avec un système de session)
# - faire un système de classement pour les joueurs (pour afficher les meilleurs joueurs)
# - faire un système de statistiques pour les joueurs (pour afficher les statistiques des joueurs)
# - faire un système de sauvegarde pour les joueurs (pour sauvegarder les parties des joueurs)

# En réalité faudra deux serveurs : 
# - un serveur pour le chat
# - un serveur pour le jeu

host, port = 'localhost', 12345
player_number = 1

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("server is listening on port", port)

while True:
    socket.listen() # the server listen for connections
    print("server is listening for connections")

    connection, address = socket.accept()
    print("connection from", address)

    game.Client_Thread.number_of_clients += 1
    
    if game.Client_Thread.number_of_clients % 2 == 1:
        game.Game.games.append(game.Game())
    client_thread = game.Client_Thread(connection, game.Game.games[-1], player_number)
    player_number += 1
    client_thread.start()

    if player_number > 2:
        player_number = 1

connection.close()
socker.close()