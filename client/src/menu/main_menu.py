import pygame as pg
import menu
import solo

class Main_Menu:

    def __init__(self, screen, widht, height):
        self.gameOver = False
        start_button = menu.Button('Jouer', (widht / 2 - 130, height / 2 - 20), screen)
        exit_button = menu.Button('Quitter', (widht / 2 - 130, height / 2 + 30), screen)
        self.buttons = [start_button, exit_button]
        self.screen = screen

    def __draw_menu(self):

        for button in self.buttons:
            button.draw(self.screen)

    def run_menu(self):

        pg.display.set_caption('Menu principal')
        
        while True:

            mousePos = pg.mouse.get_pos()
            self.screen.fill('#898A9C')
            self.__draw_menu()
            pg.display.update()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if(event.type == pg.MOUSEBUTTONDOWN):
                    if(self.buttons[0].rect.collidepoint(mousePos)):
                        game = solo.Game(self.screen)
                        game.startGame()

                    if(self.buttons[1].rect.collidepoint(mousePos)):
                        pg.quit()