import pygame as pg
import numpy as np
import pickle

import game

ROW_COUNT = 6
COLUMN_COUNT = 7

# Represents the grid of the game
class Grid:

    def __init__(self):
        # Create a matrix of 0
        self.box_status_matrix = np.zeros((ROW_COUNT,COLUMN_COUNT))   

        # Create a matrix of boxes  
        self.visual_matrix = np.full((ROW_COUNT, COLUMN_COUNT), None)

        # Set up the boxes
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.visual_matrix[i][j] = game.Box(55 + j * 70, 120 + i * 70, 70, 70)

        self.max_column_stacking = [5, 5, 5, 5, 5, 5, 5]

    # Draw the grid in the given screen
    def draw(self, screen):

        self.rect = pg.rect.Rect((45, 110), (510, 440))
        pg.draw.rect(screen, "#798192", self.rect, 0, 30) 
       
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if(self.box_status_matrix[i][j] == 0):
                    self.visual_matrix[i][j].draw_empty(screen)
                elif (self.box_status_matrix[i][j] == 1):
                    self.visual_matrix[i][j].draw_red(screen)
                elif (self.box_status_matrix[i][j] == 2):
                    self.visual_matrix[i][j].draw_yellow(screen)

    # Set a box in the grid if it's empty (!= 0)
    def set_box(self, x, y, player):

            for j in range(COLUMN_COUNT):
                if self.visual_matrix[self.max_column_stacking[j]][j].rect.x < x < self.visual_matrix[self.max_column_stacking[j]][j].rect.x + self.visual_matrix[self.max_column_stacking[j]][j].rect.width :
                    if self.box_status_matrix[self.max_column_stacking[j]][j] == 0:                        
                        self.box_status_matrix[self.max_column_stacking[j]][j] = player
                        self.max_column_stacking[j] -= 1
                        return True

    def get_serialized_matrix(self):

        # dictionary that will be serialized
        DictOfserializedObject = { "box_status_matrix" : pickle.dumps(self.box_status_matrix), "max_column_stacking" : pickle.dumps(self.max_column_stacking) }

        # serialize the dictionary
        serializedObject = pickle.dumps(DictOfserializedObject)
        # return the serialized object
        return serializedObject

    # Check if the game is over
    def check_win(self, player):

        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r][c+1] == player and self.box_status_matrix[r][c+2] == player and self.box_status_matrix[r][c+3] == player:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r+1][c] == player and self.box_status_matrix[r+2][c] == player and self.box_status_matrix[r+3][c] == player:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r+1][c+1] == player and self.box_status_matrix[r+2][c+2] == player and self.box_status_matrix[r+3][c+3] == player:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if self.box_status_matrix[r][c] == player and self.box_status_matrix[r-1][c+1] == player and self.box_status_matrix[r-2][c+2] == player and self.box_status_matrix[r-3][c+3] == player:
                    return True
                    