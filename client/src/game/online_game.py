import pygame
import game
import pickle
import menu
import threading

# Handle the online game mode
class OnlineGame(game.Game):

    def __init__(self, screen, width, height):
        game.Game.__init__(self, screen, width, height)
        self._connection = game.Connection()
        self._active_player = 1

    # Event of setting a coin in the grid
    def _set_coin_event(self, mouse_x):

        if self._grid.set_box(mouse_x, self._player_number, self._screen, self.layers[0]) == True:

            self._connection.send_data(self._grid.get_serialized_matrix())
            data = self._connection.receive_string()

            self._connection.send_string("check_win")
            data = self._connection.receive_string()

    # Event handler
    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__disconnect()
                pygame.quit()

            if self._active_player == self._player_number:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    self._set_coin_event(mouseX)

    # Handle disconnection
    def __disconnect(self):

        self._connection.send_string("close_connection")
        data = self._connection.receive_string()

        if data == "client_network_closed":
            self._connection.close()
            self._end = True
            print("Disconnected")

    def __check_client_alive(self):

        self._connection.send_string("check_client_alive")
        data = self._connection.receive_string()

        if data == "client_lost":
            self._end = True
            self._connection.close()
            print("Other player disconnected")
            return False

        return True

    # Check if the game is over
    def __check_win(self):

        self._connection.send_string("check_win")
        data = self._connection.receive_string()
        if data != "no_win":
            if data == ("Player " + str(self._player_number) + " win"):
                self._end = True
                print("You win")
                # Display the winner _screen
            else:
                self._end = True
                print("You loose")
                # Display the loser _screen

    # Update the grid
    def __update_grid(self):

        # Ask the server for the grid and update it
        self._connection.send_string("get_grid")
        serialized_server_grid = self._connection.receive_data()
        lastGrid = pickle.loads(serialized_server_grid)
        self._grid.box_status_matrix = pickle.loads(lastGrid["box_status_matrix"])
        self._grid.max_column_stacking = pickle.loads(lastGrid["max_column_stacking"])

    # Ask the server for who's turn it is
    def __check__active_player(self):

        self._connection.send_string("get_active_player")
        actualPlayer = int(self._connection.receive_string())

        if actualPlayer != self._active_player:
            self._active_player = actualPlayer
            self.__update_grid()

    # Wait for the server to be ready
    def __wait_for_server(self):

        print("waiting for server to be ready")

        waiting_screen = menu.WaitingScreen(self._screen, self.width, self.height)
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

    # Get the player number from the server
    def __get_player_number(self):

        # Get the player number from the server
        self._connection.send_string("get_player_nb")
        data = self._connection.receive_string()
        self._player_number = int(data)
        print("player number: ", self._player_number)

    def _display(self):
    
        clock = pygame.time.Clock()

        while self._end == False:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self._draw(mouse_x)
            self._render()
            pygame.display.update()
            clock.tick(60)

    # Game loop
    def start_game(self):

        # Connect to the server
        if self._connection.connect():

            # Get the player number from the server
            self.__get_player_number()

            # Wait for the server to be ready
            self.__wait_for_server()

            x = threading.Thread(target=self._display)
            x.start()

            # Start the game loop
            while self._end == False:

                # Ask the server if the other client is ready
                if self.__check_client_alive():

                    # Check if the game is over
                    self.__check_win()

                    # Check who's turn it is
                    self.__check__active_player()

                    # Get the mouse position
                    #mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Update the _screen
                    #self._draw(mouse_x)
                    #self._render()
                    #pygame.display.update()

                    # Event loop
                    self._event_handler()
