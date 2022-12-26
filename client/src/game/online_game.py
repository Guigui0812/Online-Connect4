import pygame as pg
import game
import pickle

class Online_Game(game.Game):

    # Constructor
    def __init__(self, screen):
        game.Game.__init__(self, screen)
        self._connection = game.Connection()
        
    # game loop
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

            # Faire ça dans la classe connection
            # Ask the server for the grid and update it
            self._connection.sendStr("get_grid")
            serializedLastGrid = self._connection.receiveBinary() 
            lastGrid = pickle.loads(serializedLastGrid)   
            self._grid.stateMatrix = pickle.loads(lastGrid["matrix"])
            self._grid.listRowCpt = pickle.loads(lastGrid["listRowCpt"])

            # Ask the server for who's turn it is
            self._connection.sendStr("get_active_player")
            data = self._connection.receiveStr()
            activePlayer = int(data)

            # Fill the _screen with the background color depending on the self.self._playerNb
            if activePlayer == 1:
                self._screen.fill('#FA6565')
            else:
                self._screen.fill('#FAD065')

            self._grid.draw(self._screen)
            pg.display.update()

            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:

                    # Close the connection (finir)
                    self._connection.sendStr("close_connection")
                    pg.quit()

                if activePlayer == self._playerNb:
                    if event.type == pg.MOUSEBUTTONDOWN:  

                        mouseX, mouseY = pg.mouse.get_pos()

                        if self._grid.set_box(mouseX, mouseY, self._playerNb) == True: 
                            
                            # Send the grid to the server            
                            self._connection.sendBinary(self._grid.getSerialized())                           
                            data = self._connection.receiveStr()