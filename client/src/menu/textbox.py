import pygame

# Class that corresponds to a text box
class TextBox():

    # Constructor
    def __init__(self, text, position, surface):
        self.text = text
        self.position = position
        self.surface = surface
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 20)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (300, 60))

    def set_text(self, text):

        # Set the text
        self.text = text

        # Update the text surface
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))

        # Update the text box position
        self.rect = self.text_surface.get_rect(center=self.position)

    def events_handler(self, event):

        # Handle the events
        if event.type == pygame.KEYDOWN:

            # If the key pressed is a letter
            if event.unicode.isalpha():

                # Add the letter to the text
                self.set_text(self.text + event.unicode)

            # If the key pressed is a number
            if event.unicode.isdigit():

                # Add the number to the text
                self.set_text(self.text + event.unicode)

            # If the key pressed is a space
            if event.key == pygame.K_SPACE:

                # Add a space to the text
                self.set_text(self.text + ' ')

            # If the key pressed is a backspace
            if event.key == pygame.K_BACKSPACE:

                # Remove the last character of the text
                self.set_text(self.text[:-1])

    # Draw the text box
    def draw(self):
        
        # Draw the button rect
        pygame.draw.rect(self.screen, (61, 120, 255), self.rect, border_radius = 30) 

        # Write text and center it
        text = self.font.render(self.string, True, '#F3F4FA')
        text_rect = text.get_rect(center = self.rect.center)

        # Draw the text
        self.screen.blit(text, text_rect)

