import pygame as pg
import numpy as np

import solo

ROW_COUNT = 6
COLUMN_COUNT = 7

# Represents the grid of the game
class Grid:

    def __init__(self):
        # Create a matrix of 0
        self.stateMatrix = np.zeros((ROW_COUNT,COLUMN_COUNT))   

        # Create a matrix of boxes  
        self.visualMatrix = np.full((ROW_COUNT, COLUMN_COUNT), None)

        # Set up the boxes
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                self.visualMatrix[i][j] = solo.Box(55 + j * 70, 120 + i * 70, 70, 70)

        self.listRowCpt = [5, 5, 5, 5, 5, 5, 5]

    # Draw the grid in the given screen
    def draw(self, screen):

        self.rect = pg.rect.Rect((55, 120), (490, 420))
        pg.draw.rect(screen, "#2B3FE8", self.rect, 0, 5) 
       
        for i in range(ROW_COUNT):
            for j in range(COLUMN_COUNT):
                if(self.stateMatrix[i][j] == 0):
                    self.visualMatrix[i][j].draw_empty(screen)
                elif (self.stateMatrix[i][j] == 1):
                    self.visualMatrix[i][j].draw_red(screen)
                elif (self.stateMatrix[i][j] == 2):
                    self.visualMatrix[i][j].draw_yellow(screen)

    # Set a box in the grid if it's empty (!= 0)
    def set_box(self, x, y, player):

            for j in range(COLUMN_COUNT):
                if self.visualMatrix[self.listRowCpt[j]][j].rect.x < x < self.visualMatrix[self.listRowCpt[j]][j].rect.x + self.visualMatrix[self.listRowCpt[j]][j].rect.width :
                    if self.stateMatrix[self.listRowCpt[j]][j] == 0:
                        
                        self.stateMatrix[self.listRowCpt[j]][j] = player
                        self.listRowCpt[j] -= 1
                        return True
    
    # Check if the game is over
    def check_win(self, player):

        # Check horizontal locations for win
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT):
                if self.stateMatrix[r][c] == player and self.stateMatrix[r][c+1] == player and self.stateMatrix[r][c+2] == player and self.stateMatrix[r][c+3] == player:
                    return True

        # Check vertical locations for win
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT-3):
                if self.stateMatrix[r][c] == player and self.stateMatrix[r+1][c] == player and self.stateMatrix[r+2][c] == player and self.stateMatrix[r+3][c] == player:
                    return True

        # Check positively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(ROW_COUNT-3):
                if self.stateMatrix[r][c] == player and self.stateMatrix[r+1][c+1] == player and self.stateMatrix[r+2][c+2] == player and self.stateMatrix[r+3][c+3] == player:
                    return True

        # Check negatively sloped diaganols
        for c in range(COLUMN_COUNT-3):
            for r in range(3, ROW_COUNT):
                if self.stateMatrix[r][c] == player and self.stateMatrix[r-1][c+1] == player and self.stateMatrix[r-2][c+2] == player and self.stateMatrix[r-3][c+3] == player:
                    return True
                    