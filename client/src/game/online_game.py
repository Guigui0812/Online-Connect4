import pygame
import game
import json
import threading

# Handle the online game mode
class OnlineGame(game.Game):

    # Initialize the game
    def __init__(self, screen, width, height, ip, port, player_name):
        game.Game.__init__(self, screen, width, height)
        self._connection = game.Connection(ip, port)
        self._player_number = 1
        self.display_thread = threading.Thread(target=self._display)
        self._player_name = player_name
        self.clock = pygame.time.Clock()

    # Event of setting a coin in the grid
    def _set_coin_event(self, mouse_x):

        if self._grid.set_box(mouse_x, self._player_number, self._screen, self.layers[0]) == True:

            self._connection.send_string(self._grid.get_serialized_matrix())
            self._connection.receive_string()

            data_to_send =  {"message_type": "game_request", "request_type": "check_win"}
            data_to_send = json.dumps(data_to_send)
            self._connection.send_string(data_to_send)

            self._connection.receive_string()

    # Event handler
    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end = True

            if self._active_player == self._player_number:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    self._set_coin_event(mouseX)
              
    # Check if the game is over
    def _check_win(self):

        data_to_send =  {"message_type": "game_request", "request_type": "check_win"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        data = self._connection.receive_string()

        if data == "Player 1 win" or data == "Player 2 win":

            self._end = True
            self.game_song.stop()
            self.display_thread.join()

            if data == "Player 1 win":
                end_screen = game.EndScreen(
                    self._screen, self.width, self.height,1)
                end_screen.display()
            elif data == "Player 2 win":
                end_screen = game.EndScreen(
                    self._screen, self.width, self.height,2)
                end_screen.display()

    # Update the grid
    def __update_grid(self):

        data_to_send = {"message_type": "game_request", "request_type": "get_grid"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        data = self._connection.receive_string()
        
        lastGrid = json.loads(data)

        self._grid.box_status_matrix = lastGrid["box_status_matrix"]
        self._grid.max_column_stacking = lastGrid["max_column_stacking"]

    # Ask the server for who's turn it is
    def __check_active_player(self):

        data_to_send = {"message_type": "game_request", "request_type": "get_active_player"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        actualPlayer = self._connection.receive_string()

        if actualPlayer == "1" or actualPlayer == "2":
            actualPlayer = int(actualPlayer)

        if actualPlayer != self._active_player:
            self._active_player = actualPlayer
            self.__update_grid()

    # Wait for the server to be ready
    def __wait_for_server(self):

        print("waiting for server to be ready")

        waiting_screen = game.WaitingScreen(self._screen, self.width, self.height)
        waiting_screen.start()

        server_ready = False

        # Wait for the server to be ready
        while server_ready == False:

            data_to_send =  {"message_type": "game_request", "request_type": "client_ready"}
            data_to_send = json.dumps(data_to_send)
            self._connection.send_string(data_to_send)

            data = self._connection.receive_string()
            print(data)

            if data == "server_ready":
                server_ready = True

        waiting_screen.stop()
        print("server ready")

    # Get the player number from the server and set the playername on it
    def __get_player_number(self):

        data_to_send =  {"message_type": "game_request", "request_type": "set_player_nb_and_name oui"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        data = self._connection.receive_string()

        if data == "1" or data == "2":
            self._player_number = int(data)

    # Display the game
    def _display(self):

        while self._end == False:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self._draw(mouse_x)
            self._render()
            pygame.display.update()
            self.clock.tick(60)

    # End the game
    def _end_game(self):

        data_to_send =  {"message_type": "game_request", "request_type": "game_end"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        data = self._connection.receive_string()

        if data == "game_closed":         
            # Disconnect from the server
            self._connection.close()
            self.display_thread.join()

            print("game closed")  
            
    # Game loop
    def start_game(self):

        pygame.display.set_caption("Puissance 4 - Online Game")

        # Connect to the server
        if self._connection.connect():

            # Get the player number from the server
            self.__get_player_number()

            # Wait for the server to be ready
            self.__wait_for_server()

            # Set a song for the game
            self.game_song.play(-1)

            # Start the display thread
            self.display_thread.start()

            # Start the game loop
            while self._end == False:

                # loop at a fixed rate of 60 frames per second
                self.clock.tick(60)

                if self._connection.check_alive() == True:

                    # Check if the game is over
                    self._check_win()
                    
                    # Check who's turn it is
                    self.__check_active_player()

                    # Event loop
                    self._event_handler()

                else:
                    self._end = True
                    print("Game ended unexpectedly")
                    
            # End the game
            self._end_game()