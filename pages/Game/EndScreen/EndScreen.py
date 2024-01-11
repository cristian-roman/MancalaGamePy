import os
import sys
import pygame
from ViewTree import ViewTree
from pages.UI.Components.ButtonComponent import ButtonComponent
from pages.ViewModel import ViewModel
from AppSettings import AppSettings


class EndScreen(ViewModel):
    """
    This class is responsible for the end screen of the game.

    It inherits from ViewModel, so it is a page that inherits:
        - the loop() method
        - the _load_view() method
        - the _listen_for_events() method

    The loop method includes the _load_view()
    and _listen_for_events() methods.

    Class-level attributes:
        BUTTON_DEFAULT_WIDTH (int): The default width of the buttons.
        BUTTON_DEFAULT_HEIGHT (int): The default height of the buttons.

    Attributes:
        window (pygame.Surface): The window where the end screen is drawn.
        play_again_button (ButtonComponent): The button that allows the user
                                             to play again.
        quit_button (ButtonComponent): The button that allows the user to quit.
    """
    BUTTON_DEFAULT_WIDTH = 125
    BUTTON_DEFAULT_HEIGHT = 62

    button_bg_image_path = os.path.join('images',
                                        'Game',
                                        'EndScreen',
                                        'bg_button.png')

    def __init__(self, window):
        """
        The constructor initializing the attributes of the class.
        :param window: pygame window coming from previous view
        """
        super().__init__()
        self.window = window

        self.play_again_button \
            = ButtonComponent(self.window,
                              "Play again",
                              (self.window.get_width() // 2
                               - self.BUTTON_DEFAULT_WIDTH,
                               self.window.get_height() // 3 * 2),
                              (self.BUTTON_DEFAULT_WIDTH,
                               self.BUTTON_DEFAULT_HEIGHT),
                              self.button_bg_image_path,
                              AppSettings.colors['white'],
                              AppSettings.colors['light_gray'])
        self.quit_button \
            = ButtonComponent(self.window,
                              "Quit",
                              (self.window.get_width() // 2,
                               self.window.get_height() // 3 * 2),
                              (self.BUTTON_DEFAULT_WIDTH,
                               self.BUTTON_DEFAULT_HEIGHT),
                              self.button_bg_image_path,
                              AppSettings.colors['white'],
                              AppSettings.colors['light_gray'])

    def _load_view(self):
        """
        Loads the end screen.
        It draws the buttons and updates the display.
        """
        self.play_again_button._draw()
        self.quit_button._draw()
        pygame.display.update()

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (self.play_again_button.button_rect
                        .collidepoint(event.pos)):
                    ViewTree.pop_view()
                    ViewTree.pop_view()
                elif (self.quit_button.button_rect
                        .collidepoint(event.pos)):
                    pygame.quit()
                    sys.exit()

    def _loop(self):
        self._load_view()
        self._listen_for_events()
