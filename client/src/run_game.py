import pygame as pg 
import menu

pg.init()

WIDTH = 600
HEIGHT = 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

programIcon = pg.transform.scale(pg.image.load("../assets/icon.png"), (32, 32))
pg.display.set_icon(programIcon)
menuBool= False
gameBool = False

menu = menu.Main_Menu(screen, WIDTH, HEIGHT)
menu.run_menu()