import pygame
import game
import pickle
import menu

class OnlineGame(game.Game):

    # Constructor
    def __init__(self, screen, width, height):
        game.Game.__init__(self, screen, width, height)
        self._client_network = game.Network()
        self.active_player = 1
        
    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    # game loop
    def start_game(self):

        # Connect to the server
        self._client_network.connect()

        # Get the player number from the server
        self._client_network.send_string("get_player_nb")
        data = self._client_network.receive_string()
        self._player_number = int(data)
        print("player number: ", self._player_number)

        print("waiting for server to be ready")

        waiting_screen = menu.WaitingScreen(self._screen, self.width, self.height)
        waiting_screen.start()
        # Wait for the server to be ready
        while data != "server_ready":
            
            self._client_network.send_string("client_ready")
            data = self._client_network.receive_string()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
        
        waiting_screen.stop()

        print("server ready")
        # Start the game
        while self._end == False:

            # Faire dans la classe connexion pour plus de propreté

            self._client_network.send_string("check_win")
            data = self._client_network.receive_string()
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
            self._client_network.send_string("get_active_player")
            actualPlayer = int(self._client_network.receive_string())
            
            if actualPlayer != self.active_player:

                self.active_player = actualPlayer
                # Ask the server for the grid and update it
                self._client_network.send_string("get_grid")
                serialized_server_grid = self._client_network.receive_data() 
                lastGrid = pickle.loads(serialized_server_grid)   
                self._grid.box_status_matrix = pickle.loads(lastGrid["box_status_matrix"])
                self._grid.max_column_stacking = pickle.loads(lastGrid["max_column_stacking"])

            # Fill the _screen with the background color depending on the self.self._player_number
            if self.active_player == 1:
                self._screen.fill('#FA6565')
            else:
                self._screen.fill('#58A4FF')

            self._grid.draw(self._screen)
            pygame.display.update()

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    # Close the connection (finir)
                    #self._client_network.send_string("close_client_network")
                    pygame.quit()

                if self.active_player == self._player_number:

                    if event.type == pygame.MOUSEBUTTONDOWN:  

                        mouseX, mouseY = pygame.mouse.get_pos()

                        if self._grid.set_box(mouseX, mouseY, self._player_number) == True: 
                                                    
                            self._client_network.send_data(self._grid.get_serialized_matrix())
                            data = self._client_network.receive_string()   

                            self._client_network.send_string("check_win")
                            data = self._client_network.receive_string()