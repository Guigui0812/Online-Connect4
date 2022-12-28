import pygame as pg
import game
import pickle

class OnlineGame(game.Game):

    # Constructor
    def __init__(self, screen):
        game.Game.__init__(self, screen)
        self._connection = game.Connection()
        self.active_player = 1
        
    # game loop
    def start_game(self):

        # Connect to the server
        self._connection.connect()

        # Get the player number from the server
        self._connection.send_string("get_player_nb")
        data = self._connection.receive_string()
        self._player_number = int(data)
        print("player number: ", self._player_number)

        print("waiting for server to be ready")
        # Wait for the server to be ready
        while data != "server_ready":
            
            self._connection.send_string("client_ready")
            data = self._connection.receive_string()

            # créer écran de chargement

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
        
        print("server ready")
        # Start the game
        while self._end == False:

            # Faire dans la classe connexion pour plus de propreté

            self._connection.send_string("check_win")
            data = self._connection.receive_string()
            if data != "no_win":
                if data == ("Player " + str(self._player_number)+ " win") :
                    self._end = True
                    print("You win")
                    # Display the winner _screen
                else: 
                    self._end = True
                    print("You loose")
                    # Display the loser _screen

            # Ask the server for who's turn it is
            self._connection.send_string("get_active_player")
            actualPlayer = int(self._connection.receive_string())
            
            if actualPlayer != self.active_player:

                self.active_player = actualPlayer
                # Ask the server for the grid and update it
                self._connection.send_string("get_grid")
                serialized_server_grid = self._connection.receive_data() 
                lastGrid = pickle.loads(serialized_server_grid)   
                self._grid.box_status_matrix = pickle.loads(lastGrid["matrix"])
                self._grid.max_column_stacking = pickle.loads(lastGrid["max_column_stacking"])

            # Fill the _screen with the background color depending on the self.self._player_number
            if self.active_player == 1:
                self._screen.fill('#FA6565')
            else:
                self._screen.fill('#FAD065')

            self._grid.draw(self._screen)
            pg.display.update()

            # Event loop
            for event in pg.event.get():
                if event.type == pg.QUIT:

                    # Close the connection (finir)
                    #self._connection.send_string("close_connection")
                    pg.quit()

                if self.active_player == self._player_number:

                    if event.type == pg.MOUSEBUTTONDOWN:  

                        mouseX, mouseY = pg.mouse.get_pos()

                        if self._grid.set_box(mouseX, mouseY, self._player_number) == True: 
                                                    
                            self._connection.send_data(self._grid.get_serialized_matrix())
                            data = self._connection.receive_string()   

                            self._connection.send_string("check_win")
                            data = self._connection.receive_string()