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

    # Event loop
    def _event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                self.__disconnect()
                pygame.quit()

            if self.active_player == self._player_number:

                if event.type == pygame.MOUSEBUTTONDOWN:

                    mouseX, mouseY = pygame.mouse.get_pos()

                    if self._grid.set_box(mouseX, mouseY, self._player_number) == True:

                        self._client_network.send_data(self._grid.get_serialized_matrix())
                        data = self._client_network.receive_string()

                        self._client_network.send_string("check_win")
                        data = self._client_network.receive_string()

    # Handle disconnection
    def __disconnect(self):

        self._client_network.send_string("close_client_network")
        data = self._client_network.receive_string()

        if data == "client_network_closed":
            self._client_network.close()
            self._end = True
            print("Disconnected")

    def __check_client_alive(self):

        self._client_network.send_string("check_client_alive")
        data = self._client_network.receive_string()

        if data == "client_lost":
            self._end = True
            self._client_network.close()
            print("Other player disconnected")
            return False

        return True

    # Check if the game is over
    def __check_win(self):

        self._client_network.send_string("check_win")
        data = self._client_network.receive_string()
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
        self._client_network.send_string("get_grid")
        serialized_server_grid = self._client_network.receive_data()
        lastGrid = pickle.loads(serialized_server_grid)
        self._grid.box_status_matrix = pickle.loads(lastGrid["box_status_matrix"])
        self._grid.max_column_stacking = pickle.loads(lastGrid["max_column_stacking"])

    # Ask the server for who's turn it is
    def __check_active_player(self):

        self._client_network.send_string("get_active_player")
        actualPlayer = int(self._client_network.receive_string())

        if actualPlayer != self.active_player:
            self.active_player = actualPlayer
            self.__update_grid()

    # Draw the grid
    def _draw_grid(self):

        # Fill the screen with the color depending on the player
        if self.active_player == 1:
            self._screen.fill("#FA6565")
        else:
            self._screen.fill("#58A4FF")

        self._grid.draw(self._screen)
        pygame.display.update()

    # Wait for the server to be ready
    def __wait_for_server(self):

        print("waiting for server to be ready")

        waiting_screen = menu.WaitingScreen(self._screen, self.width, self.height)
        waiting_screen.start()

        server_ready = False

        # Wait for the server to be ready
        while server_ready == False:

            self._client_network.send_string("client_ready")
            data = self._client_network.receive_string()

            if data == "server_ready":
                server_ready = True

        waiting_screen.stop()
        print("server ready")

    # Get the player number from the server
    def __get_player_number(self):

        # Get the player number from the server
        self._client_network.send_string("get_player_nb")
        data = self._client_network.receive_string()
        self._player_number = int(data)
        print("player number: ", self._player_number)

    # Game loop
    def start_game(self):

        # Connect to the server
        if self._client_network.connect():

            # Get the player number from the server
            self.__get_player_number()

            # Wait for the server to be ready
            self.__wait_for_server()

            # Start the game loop
            while self._end == False:

                # Ask the server if the other client is ready
                if self.__check_client_alive():

                    # Check if the game is over
                    self.__check_win()

                    # Check who's turn it is
                    self.__check_active_player()

                    # Draw the game
                    self._draw_grid()

                    # Event loop
                    self._event_handler()
