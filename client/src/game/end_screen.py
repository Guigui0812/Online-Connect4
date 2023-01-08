import pygame

class EndScreen():

    def __init__(self, screen, width, height, winner):
        self._screen = screen
        self._running = True
        self._text = ""
        self.width = width
        self.height = height
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 30)
        self.font_light = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 16)
        self.title_color = 0
        self.end_song = pygame.mixer.Sound('../assets/sounds/end_game_song.wav')

        if winner == 1:
            self.title_color = (223, 59, 15)
            self._text = "Le joueur 1 est le vainqueur !"
        else:
            self.title_color = (61, 120, 255)
            self._text = "Le joueur 2 est le vainqueur !"

    def display(self):

        self.end_song.play(-1)

        while self._running == True:
            
            # Fill the screen with a color
            self._screen.fill('#F3F4FA')

            # Text to display
            text = self.font.render(self._text, True, self.title_color)
            text_rect = text.get_rect(center=(self.width/2, self.height/2))
            
            info_text = self.font_light.render("Appuyez sur espace pour revenir au menu", True, "#8E8E8E")
            info_rect = info_text.get_rect(center=(self.width/2, self.height - 50))

            # Display the text
            self._screen.blit(text, text_rect)    
            self._screen.blit(info_text, info_rect)    
            pygame.display.update()
            
            for event in pygame.event.get():
                # if the window is closed, quit the game
                if event.type == pygame.QUIT:
                    self._running = False
                    pygame.quit()

                # if space is pressed, go back to the menu
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.end_song.stop()
                        self._running = False