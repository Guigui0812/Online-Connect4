import pygame

class Button:

    def __init__(self, txt, position, screen):
        self.string = txt
        self.position = position
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 25)
        self.screen = screen
        self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (300, 60))

    def draw(self):

        # Draw the button rect
        pygame.draw.rect(self.screen, (61, 120, 255), self.rect, border_radius = 30) 

        # Write text and center it
        text = self.font.render(self.string, True, '#F3F4FA')
        text_rect = text.get_rect(center = self.rect.center)
        self.screen.blit(text, text_rect)

    def check_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_position()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False