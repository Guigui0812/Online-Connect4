import pygame
import menu
import game

class MainMenu:

    # Constructor
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

    # Draw the menu
    def __draw_menu(self):

        self.screen.fill('#C2C5CD')

        # Draw the title
        text = self.font.render(self.title, True, (223, 59, 15))
        text_rect = text.get_rect(center=(self.width/2, self.height/2 - 100))
        self.screen.blit(text, text_rect)   

        # Draw the buttons
        for button in self.buttons:
            button.draw(self.screen)

        pygame.display.update()

    # Run the menu
    def run_menu(self):

        pygame.display.set_caption('Puissance 4')
        
        # Main loop
        while self.running:
                      
            self.__draw_menu()
            
            # Event handling
            mouse_position = pygame.mouse.get_pos()

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