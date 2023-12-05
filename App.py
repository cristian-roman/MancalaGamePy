import pygame
import sys


class App:
    name = "Mancala Game"
    width = 800
    height = 600

    @staticmethod
    def init():
        pygame.init()
        pygame.display.set_mode((App.width, App.height))
        pygame.display.set_caption(App.name)

        App.__main_loop()

    @staticmethod
    def __main_loop():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
