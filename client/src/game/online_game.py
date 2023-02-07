import pygame
import game
import pickle
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

    # Event of setting a coin in the grid
    def _set_coin_event(self, mouse_x):

        if self._grid.set_box(mouse_x, self._player_number, self._screen, self.layers[0]) == True:

            self._connection.send_data(self._grid.get_serialized_matrix())
            self._connection.receive_string()
            self._connection.send_string("check_win")
            self._connection.receive_string()

    # Event handler
    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_song.stop()
                self.__disconnect()
                pygame.quit()

            if self._active_player == self._player_number:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    self._set_coin_event(mouseX)

    # Handle disconnection
    def __disconnect(self):

        self._connection.send_string("close_client_network")
        data = self._connection.receive_string()

        if data == "client_network_closed":
            self._connection.close()
            self._end = True
            self.display_thread.join()
            print("Disconnected")

    """
    # Check if the other player is still connected
    def __check_client_alive(self):

        self._connection.send_string("check_client_alive")
        data = self._connection.receive_string()

        if data == "client_lost":
            self._end = True
            self._connection.close()
            print("Other player disconnected")
            return False

        return True

    """
    

    # Check if the game is over
    def _check_win(self):

        self._connection.send_string("check_win")
        data = self._connection.receive_string()

        if data != "no_win":

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

        # Ask the server for the grid and update it
        self._connection.send_string("get_grid")
        serialized_server_grid = self._connection.receive_data()
        lastGrid = pickle.loads(serialized_server_grid)
        self._grid.box_status_matrix = pickle.loads(
            lastGrid["box_status_matrix"])
        self._grid.max_column_stacking = pickle.loads(
            lastGrid["max_column_stacking"])

    # Ask the server for who's turn it is
    def __check_active_player(self):

        self._connection.send_string("get_active_player")
        actualPlayer = int(self._connection.receive_string())

        if actualPlayer != self._active_player:
            self._active_player = actualPlayer
            self.__update_grid()

    # Wait for the server to be ready
    def __wait_for_server(self):

        print("waiting for server to be ready")

        waiting_screen = game.WaitingScreen(
            self._screen, self.width, self.height)
        waiting_screen.start()

        server_ready = False

        # Wait for the server to be ready
        while server_ready == False:

            self._connection.send_string("client_ready")
            data = self._connection.receive_string()

            if data == "server_ready":
                server_ready = True

        waiting_screen.stop()
        print("server ready")

    # Get the player number from the server and set the playername on it
    def __get_player_number(self):
        self._connection.send_string("set_player_nb_and_name oui")
        data = self._connection.receive_string()
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
    def _end_game_connection(self):
        try:
            # Disconnect from the server
            self.__disconnect()
        except:
            # Check if the other client is still connected before disconnecting
            self._connection.send_string("check_client_alive")
            self._connection.receive_string()
            self._connection.close()

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

                # Ask the server if the other client is ready
                if self._connection.check_alive():

                    # Check if the game is over
                    self._check_win()

                    # Check who's turn it is
                    self.__check_active_player()

                    # Event loop
                    self._event_handler()
            
            self._end_game_connection()