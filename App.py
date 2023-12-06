import pygame

from models.UI import UI
from ViewTree import ViewTree
from AppSettings import AppSettings


class App:

    window = None
    view_tree = None

    @staticmethod
    def init():
        pygame.init()
        font = pygame.font.Font(None, 30)
        AppSettings.init(font)

        App.window = pygame.display.set_mode((AppSettings.width, AppSettings.height))
        pygame.display.set_caption(AppSettings.name)
        App.view_tree = ViewTree(UI(App.window))

        App.__main_loop()

    @staticmethod
    def __main_loop():
        while True:
            App.view_tree.get_current_view().loop()

