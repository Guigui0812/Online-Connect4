import pygame as pg 
import menu

pg.init()

WIDTH = 600
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

icon = pg.transform.scale(pg.image.load("../assets/icon.png"), (32, 32))
pg.display.set_icon(icon)

menu = menu.MainMenu(screen, WIDTH, HEIGHT)
menu.run_menu()

pg.quit()