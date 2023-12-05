import pygame
import sys
from UI import UI


class App:
    name = "Mancala Game"
    width = 800
    height = 600
    window = None

    @staticmethod
    def init():
        pygame.init()
        App.window = pygame.display.set_mode((App.width, App.height))
        pygame.display.set_caption(App.name)

        App.__main_loop()

    @staticmethod
    def __main_loop():
        while True:
            App.__listen_for_events()
            bg_image = pygame.transform.scale(UI.get_background_image(), (App.width, App.height))
            App.window.blit(bg_image, (0, 0))
            pygame.display.flip()

    @staticmethod
    def __listen_for_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
