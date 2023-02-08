import pygame
import interface_items
import game
import menus

class OnlineSettings():

    def __init__(self, screen, width, height):
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

        self.config_handler = menus.Config()
        default_ip = self.config_handler.get_value('NETWORK', 'ip')
        default_port = self.config_handler.get_value('NETWORK', 'port')
        default_pseudo = self.config_handler.get_value('PLAYER', 'name')

        self.textboxes = [
            interface_items.TextBox(default_ip, (self.width/2 - 150, self.height/2 - 100), self.screen),
            interface_items.TextBox(default_port, (self.width/2 - 150, self.height/2 - 40), self.screen),
            interface_items.TextBox(default_pseudo, (self.width/2 - 150, self.height/2 + 20), self.screen)
        ]

    def __draw_menu(self):

        self.screen.fill('#F3F4FA')

        text = self.font.render(self.title, True, (61, 120, 255))
        text_rect = text.get_rect(center=(self.width/2, self.height/2 - 200))
        self.screen.blit(text, text_rect)

        for button in self.buttons:
            button.draw()

        for textbox in self.textboxes:
            textbox.draw()

    def __event_handler(self, mouse_position):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(self.buttons[0].rect.collidepoint(mouse_position)):
                    self.running = False

                if(self.buttons[1].rect.collidepoint(mouse_position)):

                    try:

                        self.config_handler.set_value('NETWORK', 'ip', self.textboxes[0].text)
                        self.config_handler.set_value('NETWORK', 'port', self.textboxes[1].text)
                        self.config_handler.set_value('PLAYER', 'name', self.textboxes[2].text)

                        self.running = False
                        
                        new_game = game.OnlineGame(self.screen, self.width, self.height, self.textboxes[0].text, self.textboxes[1].text, self.textboxes[2].text)
                        new_game.start_game()
                    
                    except Exception as e:
                        print(e)
                        self.running = False

            for textbox in self.textboxes:
                textbox.handle_events(event)

    def run_online_settings(self):

        pygame.display.set_caption('Puissance 4 - Paramètres de la partie en ligne')

        while self.running:

            mouse_position = pygame.mouse.get_pos()
            self.__draw_menu()
            self.__event_handler(mouse_position)
            pygame.display.update()

