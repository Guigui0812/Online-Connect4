import pygame as pg
import game
import pickle

class Online_Game(game.Game):

    def __init__(self, screen):
        game.Game.__init__(self, screen)
        self._connection = game.Connection()
        
    def start_game(self):

        # Connect to the server
        self._connection.connect()

        # Get the player number from the server
        self._connection.sendStr("get_player_nb")
        data = self._connection.receiveStr()
        self._playerNb = int(data)

        # Wait for the server to be ready
        while data != "server_ready":
            print("waiting for server to be ready")
            self._connection.sendStr("client_ready")
            data = self._connection.receiveStr()

            # créer écran de chargement

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
        
        # Start the game
        while self._gameOver == False:

            # Ask the server for the grid and update it
            self._connection.sendStr("get_grid")
            serializedLastGrid = self._connection.receive() 
            lastGrid = pickle.loads(serializedLastGrid)   
            self._grid.stateMatrix = pickle.loads(lastGrid["matrix"])
            self._grid.lastBox = lastGrid["lastBox"]

            # Ask the server for who's turn it is
            self._connection.sendStr("get_active_player")
            data = self._connection.receiveStr()
            activePlayer = int(data)

            # if activePlayer == self._playerNb:


            # If it's the player's turn



            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()