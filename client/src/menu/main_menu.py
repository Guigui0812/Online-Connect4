import pygame as pg
import menu
import game

class MainMenu:

    def __init__(self, screen, widht, height):
        start_button = menu.Button('Jouer', (widht / 2 - 130, height / 2 - 20), screen)
        online_button = menu.Button('Online', (widht / 2 - 130, height / 2 + 30), screen)
        self.buttons = [start_button, online_button]
        self.screen = screen
        self.running = True

    def __draw_menu(self):

        for button in self.buttons:
            button.draw(self.screen)

    def run_menu(self):

        pg.display.set_caption('Menu principal')
        
        while self.running:

            mouse_position = pg.mouse.get_pos()
            self.screen.fill('#898A9C')
            self.__draw_menu()
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                if(event.type == pg.MOUSEBUTTONDOWN):
                    if(self.buttons[0].rect.collidepoint(mouse_position)):
                        new_game = game.SoloGame(self.screen)
                        new_game.start_game()

                    if(self.buttons[1].rect.collidepoint(mouse_position)):
                        new_game = game.OnlineGame(self.screen)
                        new_game.start_game()