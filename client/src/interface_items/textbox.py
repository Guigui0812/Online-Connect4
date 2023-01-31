import pygame

# Class that corresponds to a text box
class TextBox():

    # Constructor
    def __init__(self, text, position, surface):
        self.text = text
        self.position = position
        self.surface = surface
        self.font = pygame.font.Font('../assets/fonts/Sugar Snow.ttf', 25)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.rect = pygame.rect.Rect((self.position[0], self.position[1]), (300, 40))
        self.clicked = False
        self.already_clicked = False

    def set_text(self, text):

        # Set the text
        self.text = text

        # Update the text surface
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))

    def handle_events(self, event):

        # Handle the events
        if event.type == pygame.KEYDOWN:

            if self.clicked:

                if not self.already_clicked:
                    self.set_text('')
                    self.already_clicked = True

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

        if event.type == pygame.MOUSEBUTTONDOWN:

            # If the mouse button is pressed
            if event.button == 1:

                # If the mouse is over the text box
                if self.rect.collidepoint(event.pos):

                    # Set the text box as clicked
                    self.clicked = True
                    print(self.clicked)

                else:
                    # Set the text box as not clicked
                    self.clicked = False
                    print(self.clicked)

    # Check if the text box is focused
    def is_focused(self):
        # Return the clicked variable
        return self.clicked

    # Draw the text box
    def draw(self):

        # Draw the button rect
        if self.clicked:
            pygame.draw.rect(self.surface, (61, 120, 255), self.rect, 2, border_radius = 4)
        else:
            pygame.draw.rect(self.surface, (254, 91, 47), self.rect, 2, border_radius = 4)

        # Write text and center it
        text = self.font.render(self.text, True, (121, 129, 146))
        text_rect = text.get_rect(center = self.rect.center)

        # Draw the text
        self.surface.blit(text, text_rect)

