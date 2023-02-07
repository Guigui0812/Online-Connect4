import pygame
import menus

# Initialize pygame
pygame.init()

# Set the size of the window
WIDTH = 600
HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

icon = pygame.transform.scale(pygame.image.load("../assets/images/icon.png"), (32, 32))
pygame.display.set_icon(icon)

menu = menus.MainMenu(screen, WIDTH, HEIGHT)
menu.run_menu()

pygame.quit()