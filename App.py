import pygame

from pages.UI import UI
from ViewTree import ViewTree
from AppSettings import AppSettings


class App:

    window = None

    @staticmethod
    def init():
        pygame.init()
        font = pygame.font.Font(None, 30)
        AppSettings.init(font)

        App.window = pygame.display.set_mode((AppSettings.width, AppSettings.height))
        pygame.display.set_caption(AppSettings.name)

        ViewTree.init(UI(App.window))
        App.__main_loop()

    @staticmethod
    def __main_loop():
        while True:
            ViewTree.get_current_view().loop()

