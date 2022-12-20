import pygame as pg 
import classes

pg.init()

WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

pg.display.set_caption('Menu principal')
menuBool= False
gameBool = False

menu = classes.Main_Menu(screen, WIDTH, HEIGHT)
menu.run_menu()