import pygame
import menu

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = pygame.transform.scale(pygame.image.load("../assets/images/icon.png"), (32, 32))
pygame.display.set_icon(icon)

menu = menu.MainMenu(screen, WIDTH, HEIGHT)
menu.run_menu()

pygame.quit()