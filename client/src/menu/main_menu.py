import pygame
import menu
import game

class MainMenu:

    def __init__(self, screen, width, height):
        self.title = "Puissance 4"
        start_button = menu.Button('Multijoueur local', (width / 2 - 150, height / 2), screen)
        online_button = menu.Button('Multijoueur en ligne', (width / 2 - 150, height / 2 + 80), screen)
        self.buttons = [start_button, online_button]
        self.screen = screen
        self.running = True
        self.width = width
        self.height = height
        self.font = pygame.font.Font('../assets/Sugar Snow.ttf', 40)

    def __draw_menu(self):

        text = self.font.render(self.title, True, (223, 59, 15))
        text_rect = text.get_rect(center=(self.width/2, self.height/2 - 100))
        self.screen.blit(text, text_rect)   

        for button in self.buttons:
            button.draw(self.screen)

    def run_menu(self):

        pygame.display.set_caption('Puissance 4')
        
        while self.running:

            mouse_position = pygame.mouse.get_pos()
            self.screen.fill('#C2C5CD')
            self.__draw_menu()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if(event.type == pygame.MOUSEBUTTONDOWN):
                    if(self.buttons[0].rect.collidepoint(mouse_position)):
                        new_game = game.SoloGame(self.screen, self.width, self.height)
                        new_game.start_game()

                    if(self.buttons[1].rect.collidepoint(mouse_position)):
                        new_game = game.OnlineGame(self.screen, self.width, self.height)
                        new_game.start_game()