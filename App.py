import pygame
from pages.UI.UI import UI
from ViewTree import ViewTree
from AppSettings import AppSettings


class App:

    """
    This class is responsible for the entry point of the game.

    It contains the init() method, that initializes the game.

    It also contains the __main_loop() method, that is the main loop of the game.
    This function is to be replaced of any loop that is in the top of the ViewTree.
    """
    window = None

    @staticmethod
    def init():
        """
        This method initializes the game.
        It sets the font of the game.
        It pushes the UI view to the ViewTree.
        :return: None
        """
        pygame.init()
        font = pygame.font.Font(None, 30)
        AppSettings.init(font)

        App.window \
            = pygame.display.set_mode((AppSettings.width,
                                       AppSettings.height),
                                      pygame.HWSURFACE |
                                      pygame.DOUBLEBUF |
                                      pygame.RESIZABLE |
                                      pygame.SRCALPHA)
        pygame.display.set_caption(AppSettings.name)

        ViewTree.init(UI(App.window))
        App.__main_loop()

    @staticmethod
    def __main_loop():
        """
        This method is the main loop of the game.

        It is to be replaced of any loop that
        is in the top of the ViewTree.
        In the beginning it is replaced by the loop() method
        of the UI class.
        :return: None
        """
        while True:
            ViewTree.get_current_view()._loop()

