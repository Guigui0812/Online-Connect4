import pygame
import menu
import game

# Class that handles the main menu
class MainMenu:

    # Constructor
    def __init__(self, screen, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.surface.Surface((self.width, self.height), pygame.SRCALPHA)
        self.title = "Puissance 4"
        start_button = menu.Button('Multijoueur local', (width / 2 - 150, height / 2), self.surface)
        online_button = menu.Button('Multijoueur en ligne', (width / 2 - 150, height / 2 + 80), self.surface)
        self.buttons = [start_button, online_button]
        self.screen = screen
        self.running = True 
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 40)
        self.menu_song = pygame.mixer.Sound('../assets/sounds/main_menu_song.wav')
        
    # Draw the menu
    def __draw_menu(self):

        # Fill the background
        self.screen.fill('#F3F4FA')

        # Draw the title
        text = self.font.render(self.title, True, (223, 59, 15))
        text_rect = text.get_rect(center=(self.width/2, self.height/2 - 100))
        self.surface.blit(text, text_rect)   

        # Draw the buttons
        for button in self.buttons:
            button.draw()

    # Handle the events
    def __event_handler(self, mouse_position):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(self.buttons[0].rect.collidepoint(mouse_position)):
                    self.menu_song.stop()
                    new_game = game.SoloGame(self.screen, self.width, self.height)
                    new_game.start_game()

                if(self.buttons[1].rect.collidepoint(mouse_position)):
                    self.menu_song.stop()
                    new_game = menu.(self.screen, self.width, self.height)
                    new_game.start_game()

    # Run the menu
    def run_menu(self):

        # Set the title of the window
        pygame.display.set_caption('Puissance 4 - Menu')

        # Load the background image of the menu
        background = pygame.transform.scale(pygame.image.load("../assets/images/menu_background.png"), (self.width, self.height))
        background.set_alpha(25)

        # Player a song in the background of the menu 
        self.menu_song.play(-1)

        # Main loop
        while self.running:
                      
            # if the song is stopped, play it again
            if not pygame.mixer.get_busy():
                self.menu_song.play(-1)

            # Draw the menu
            self.__draw_menu()

            # Update the screen
            self.screen.blit(background, (0, 0))
            self.screen.blit(self.surface, (0, 0))
            pygame.display.update()

            # Event handling
            mouse_position = pygame.mouse.get_pos()
            self.__event_handler(mouse_position)