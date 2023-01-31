import pygame

import menu
import game

class OnlineSettings():

    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.running = True
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 25)
        self.title = 'Paramètres de la partie en ligne'
        self.buttons = [
            menu.Button('Retour', (self.width/2 - 150, self.height/2 + 100), self.screen),
            menu.Button('Jouer', (self.width/2 - 150, self.height/2), self.screen)
        ]
        self.textboxes = [
            menu.TextBox('Adresse IP', (self.width/2 - 150, self.height/2 - 200), self.screen),
            menu.TextBox('Port', (self.width/2 - 150, self.height/2 - 300), self.screen),
            menu.TextBox('Pseudo', (self.width/2 - 150, self.height/2 - 400), self.screen)
        ]

    def __draw_menu(self):
        self.screen.fill('#F3F4FA')

        text = self.font.render(self.title, True, (223, 59, 15))
        text_rect = text.get_rect(center=(self.width/2, self.height/2 - 200))
        self.screen.blit(text, text_rect)

        for button in self.buttons:
            button.draw()

    def __event_handler(self, mouse_position):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            if(event.type == pygame.MOUSEBUTTONDOWN):
                if(self.buttons[0].rect.collidepoint(mouse_position)):
                    self.running = False

                if(self.buttons[1].rect.collidepoint(mouse_position)):
                    self.running = False
                    new_game = game.OnlineGame(self.screen, self.width, self.height)
                    new_game.start_game()

                if(self.buttons[2].rect.collidepoint(mouse_position)):
                    self.running = False
                    new_game = game.OnlineGame(self.screen, self.width, self.height)
                    new_game.start_game()

    def run_online_settings(self):
        pygame.display.set_caption('Puissance 4 - Paramètres de la partie en ligne')

        while self.running:
            mouse_position = pygame.mouse.get_pos()

            self.__draw_menu()
            self.__event_handler(mouse_position)

            pygame.display.update()

