import os
import sys
import pygame
from ViewTree import ViewTree
from pages.Game.Game import Game
from pages.UI.Components.ButtonComponent import ButtonComponent
from pages.ViewModel import ViewModel


class UI(ViewModel):
    """
    This class is responsible for the entry UI of the game.

    It inherits from ViewModel, so it is a page that inherits:
        - the _loop() method
        - the _load_view() method
        - the _listen_for_events() method

    The loop method includes the _load_view()
    and _listen_for_events() methods.

    Class-level attributes:
        BUTTON_WIDTH (int): The width of the buttons.
        BUTTON_HEIGHT (int): The height of the buttons.
        UI_IMAGE_PATH (str): The path of the images of the UI.

    Attributes:
        window (pygame.Surface): The window where the UI is drawn.
        bg_image_path (str): The path of the background image of the UI.
        bg_button_image_path (str): The path of the background image
                                    of the buttons.
        ui_bg_image (pygame.Surface):   The background image of the UI
                                        as a pygame object.
        first_x_coordinate (int): The x coordinate of the first button.
        first_y_coordinate (int): The y coordinate of the first button.
        play_pvp_button (ButtonComponent): The button that allows the user
                                           to play player vs player.
        play_pve_button (ButtonComponent): The button that allows the user
                                           to play player vs computer.
        quit_button (ButtonComponent): The button that allows the user to quit.
    """
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 50
    UI_IMAGE_PATH = os.path.join('images', 'UI')

    def __init__(self, window: pygame.Surface):
        """
        The constructor initializing the attributes of the class.
        :param window: pygame window coming from App, initially
        """
        super().__init__()
        self.window = window

        self.bg_image_path \
            = os.path.join(self.UI_IMAGE_PATH, 'background.jpeg')
        self.bg_button_image_path \
            = os.path.join(self.UI_IMAGE_PATH, 'button-bg.jpeg')

        self.ui_bg_image = pygame.image.load(self.bg_image_path)
        self.ui_bg_image \
            = pygame.transform.scale(self.ui_bg_image,
                                     (self.window.get_width(),
                                      self.window.get_height()))

        self.first_x_coordinate = (self.window.get_width() // 2
                                   - self.BUTTON_WIDTH * 2
                                   + 25)
        self.first_y_coordinate = (self.window.get_height()
                                   // 3
                                   * 2
                                   + 100)

        self.play_pvp_button \
            = ButtonComponent(self.window, "Play pvp",
                              (self.first_x_coordinate,
                               self.first_y_coordinate),
                              (self.BUTTON_WIDTH,
                               self.BUTTON_HEIGHT),
                              self.bg_button_image_path)

        self.play_pve_button \
            = ButtonComponent(self.window, "Play pve",
                              (self.first_x_coordinate
                               + self.BUTTON_WIDTH
                               + 50,  # 50 is the distance between the buttons
                               self.first_y_coordinate),
                              (self.BUTTON_WIDTH,
                               self.BUTTON_HEIGHT),
                              self.bg_button_image_path)

        self.quit_button \
            = ButtonComponent(self.window,
                              "Quit",
                              (self.first_x_coordinate
                               + self.BUTTON_WIDTH
                               * 2
                               + 100,
                               self.first_y_coordinate),
                              (self.BUTTON_WIDTH, self.BUTTON_HEIGHT),
                              self.bg_button_image_path)

    def _listen_for_events(self):
        """
        This method listens for events such as:
            - QUIT: if the user wants to quit the game
            - MOUSEBUTTONDOWN: if the user clicks on a button
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (self.play_pvp_button
                        .button_rect
                        .collidepoint(event.pos)):
                    ViewTree.push_view(Game(self.window))
                elif (self.play_pve_button
                        .button_rect
                        .collidepoint(event.pos)):
                    game_view = Game(self.window)
                    game_view.set_pve()
                    ViewTree.push_view(game_view)
                elif (self.quit_button.button_rect
                        .collidepoint(event.pos)):
                    pygame.quit()
                    sys.exit()

    def _load_view(self):
        """
        Displays the UI.
        It draws the background and the buttons.
        :return: None
        """
        self.window.blit(self.ui_bg_image, (0, 0))
        self.play_pvp_button._draw()
        self.play_pve_button._draw()
        self.quit_button._draw()

    def _loop(self):
        """
        This function loops the UI page.
        It calls the _load_view() and _listen_for_events() methods.
        """
        self._listen_for_events()
        self._load_view()
        pygame.display.update()
