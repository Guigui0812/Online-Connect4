import pygame
import interface_items
import game
import menus

# Class to handle the online settings menu
class OnlineSettings():

    # Constructor
    def __init__(self, screen, width, height, music):

        # Set the attributes
        self.screen = screen
        self.width = width
        self.height = height
        self.running = True
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 30)
        self.title = 'Parametres de la partie en ligne'
        self.buttons = [
            interface_items.Button('Retour', (self.width/2 - 270, self.height - 100), self.screen),
            interface_items.Button('Jouer', (self.width/2 + 20, self.height - 100), self.screen)
        ]
        self.music = music

        # Load the elements of the config file in the textboxes
        self.config_handler = menus.Config()
        default_ip = self.config_handler.get_value('NETWORK', 'ip')
        default_port = self.config_handler.get_value('NETWORK', 'port')
        default_pseudo = self.config_handler.get_value('PLAYER', 'name')

        self.textboxes = [
            interface_items.TextBox(default_ip, (self.width/2 - 150, self.height/2 - 100), self.screen),
            interface_items.TextBox(default_port, (self.width/2 - 150, self.height/2 - 40), self.screen),
            interface_items.TextBox(default_pseudo, (self.width/2 - 150, self.height/2 + 20), self.screen)
        ]

    # draw the network menu
    def __draw_menu(self):

        self.screen.fill('#F3F4FA')

        # Set the text
        text = self.font.render(self.title, True, (61, 120, 255))
        text_rect = text.get_rect(center=(self.width/2, self.height/2 - 200))
        self.screen.blit(text, text_rect)

        # Draw the buttons
        for button in self.buttons:
            button.draw()

        # Draw the textboxes
        for textbox in self.textboxes:
            textbox.draw()

    # Loop event
    def __event_handler(self, mouse_position):

        for event in pygame.event.get():

            # Close event
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            # Mouse click event
            if(event.type == pygame.MOUSEBUTTONDOWN):

                # If the return button is clicked then return to the main menu
                if(self.buttons[0].rect.collidepoint(mouse_position)):
                    self.running = False

                # if the play button is clicked then start the online game
                if(self.buttons[1].rect.collidepoint(mouse_position)):

                    # Try to start an online game with the settings contained in the textboxes
                    try:
                        self.config_handler.set_value('NETWORK', 'ip', self.textboxes[0].text)
                        self.config_handler.set_value('NETWORK', 'port', self.textboxes[1].text)
                        self.config_handler.set_value('PLAYER', 'name', self.textboxes[2].text)

                        self.running = False
                        
                        self.music.stop()
                        new_game = game.OnlineGame(self.screen, self.width, self.height, self.textboxes[0].text, self.textboxes[1].text, self.textboxes[2].text)
                        new_game.start_game()
                    
                    except Exception as e:
                        print(e)
                        self.running = False

            # Text event
            for textbox in self.textboxes:
                textbox.handle_events(event)

    # Run the menu
    def run_online_settings(self):

        # Set the window title
        pygame.display.set_caption('Puissance 4 - Paramètres de la partie en ligne')

        # While the menu is running, draw the menu and handle the events
        while self.running:
            mouse_position = pygame.mouse.get_pos()
            self.__draw_menu()
            self.__event_handler(mouse_position)
            pygame.display.update()

