import pygame as pg
import game

# Représente une partie
class Game():

    def __init__(self, screen, width, height):
        self._end = False
        self._screen = screen
        self._player_number = 1
        self._grid = game.Grid()     
        self.width = width
        self.height = height
        
    def __check_win(self):
        pass

    def start_game(self):
        pass