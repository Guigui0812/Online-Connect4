import pygame
import menus

# Initialize pygame
pygame.init()

# Set the size of the window
WIDTH = 600
HEIGHT = 600

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the title of the window
icon = pygame.transform.scale(pygame.image.load("../assets/images/icon.png"), (32, 32))
pygame.display.set_icon(icon)

# Run the menu
menu = menus.MainMenu(screen, WIDTH, HEIGHT)
menu.run_menu()

# Quit pygame
pygame.quit()