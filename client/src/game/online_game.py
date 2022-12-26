import pygame as pg
import game

class Online_Game(game.Game):

    def __init__(self, screen):
        game.Game.__init__(self, screen)
        self._connection = game.Connection()
        
    def start_game(self):
        self._connection.connect()
        self._connection.send("start_game")

        while self._gameOver == False:

            data = self._connection.receive()

            if data == "start_game":
                self._playerNb = 1
                break
            elif data == "join_game":
                self._playerNb = 2
                break