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

    # Display the player who is playing
    def _display_player(self):
        
        if self._active_player == 1:

            if self._player_number == 1:
                color = (254, 91, 47)
                title = "A vous  " + self._player_name
            else:
                color = (61, 120, 255)
                title = "Tour de l'adversaire"

        else:
            if self._player_number == 2:
                color = (61, 120, 255)
                title = "A vous " + self._player_name
            else:        
                color = (254, 91, 47)
                title = "Tour de l'adversaire"

        # text to display
        text = self.font.render(title, True, color)
        text_rect = text.get_rect(center=(self.width/2, 40))
        self._screen.blit(text, text_rect)  

    # Event of setting a coin in the grid
    def _set_coin_event(self, mouse_x):

        # if the player successfully set a coin in the grid
        if self._grid.set_box(mouse_x, self._player_number, self._screen, self.layers[0]) == True:

            # send the serialized grid to the server
            self._connection.send_string(self._grid.get_serialized_matrix())
            self._connection.receive_string()

            # check if the game is over with a game request "check_win"
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

        # check if the game is over with a game request "check_win"
        data_to_send =  {"message_type": "game_request", "request_type": "check_win"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        # receive the data from the server
        data = self._connection.receive_string()

        # transform the data into a dict
        message = json.loads(data)

        # if the game is over and a player won
        if message["message_type"] == "win":

            # stop the game, display the end screen and join the display thread
            self._end = True
            self.game_song.stop()
            self.display_thread.join()

            # display the end screen with the winner as parameter
            if self._player_number == 1:
                end_screen = game.EndScreen(
                    self._screen, self.width, self.height,1, message["winner"])
                end_screen.display()
            else:
                end_screen = game.EndScreen(
                    self._screen, self.width, self.height,2, message["winner"])
                end_screen.display()

    # Update the grid
    def __update_grid(self):

        # Request the grid to the server with a game request "get_grid"
        data_to_send = {"message_type": "game_request", "request_type": "get_grid"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        # receive the data from the server and transform it into a dict
        data = self._connection.receive_string()    
        lastGrid = json.loads(data)

        # update the grid with the data received from the server
        self._grid.box_status_matrix = lastGrid["box_status_matrix"]
        self._grid.max_column_stacking = lastGrid["max_column_stacking"]

    # Ask the server for who's turn it is
    def __check_active_player(self):

        # Check the active player with a game request "get_active_player"
        data_to_send = {"message_type": "game_request", "request_type": "get_active_player"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)
        actualPlayer = self._connection.receive_string()

        # if the data received is a string that contains a number, it's the player number
        if actualPlayer == "1" or actualPlayer == "2":
            actualPlayer = int(actualPlayer)

            # if the active player is different from the one we have, update the grid
            if actualPlayer != self._active_player:
                self._active_player = actualPlayer
                self.__update_grid()

    # Wait for the server to be ready
    def __wait_for_server(self):

        print("waiting for server to be ready")

        # Display the waiting screen
        waiting_screen = game.WaitingScreen(self._screen, self.width, self.height)
        waiting_screen.start()

        # set the server ready to false
        server_ready = False

        # Wait for the server to be ready
        while server_ready == False:

            # Ask the server if it's ready with a game request "client_ready"
            data_to_send =  {"message_type": "game_request", "request_type": "client_ready"}
            data_to_send = json.dumps(data_to_send)
            self._connection.send_string(data_to_send)

            data = self._connection.receive_string()
            print(data)

            # if the server is ready, set the server ready to true
            if data == "server_ready":
                server_ready = True

        # Stop the waiting screen
        waiting_screen.stop()
        print("server ready")

    # Get the player number from the server and set the playername on it
    def __get_player_number(self):

        # Ask the server for the player number with a game request "set_player_nb_and_name"
        data_to_send =  {"message_type": "game_request", "request_type": "set_player_nb_and_name", "player_name": self._player_name}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        data = self._connection.receive_string()

        # if the data received is a string that contains a number, it's the player number
        if data == "1" or data == "2":
            self._player_number = int(data)

    # Display the game
    def _display(self):

        # Display all the elements of the game
        while self._end == False:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self._draw(mouse_x)
            self._render()
            self._display_player()
            pygame.display.update()
            self.clock.tick(60)

    # End the game
    def _end_game(self):

        # Ask the server to end the game with a game request "game_end"
        data_to_send =  {"message_type": "game_request", "request_type": "game_end"}
        data_to_send = json.dumps(data_to_send)
        self._connection.send_string(data_to_send)

        data = self._connection.receive_string()

        # if the server closed the game, disconnect from the server and join the display thread
        if data == "game_closed":         

            # Stop the game song
            self.game_song.stop()

            # Disconnect from the server
            self._connection.close()
            self.display_thread.join()

            print("game closed")  
            
    # Game loop
    def start_game(self):

        # Set the caption of the window
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

                # Check if the connection is still alive
                if self._connection.check_alive() == True:

                    # Check if the game is over
                    self._check_win()
                    
                    # Check who's turn it is
                    self.__check_active_player()

                    # Event loop
                    self._event_handler()

                else:
                    self._end = True
                    print("The game ended unexpectedly")
                    
            # End the game
            self._end_game()