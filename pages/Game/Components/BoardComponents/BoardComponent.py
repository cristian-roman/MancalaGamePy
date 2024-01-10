import os

import pygame
from AppSettings import AppSettings
from pages.Game.Components.GameComponent import GameComponent
from pages.Game.Components.BoardComponents.PotComponent import PotComponent


class BoardComponent(GameComponent):
    """
    A class that represents the board.

    It is a GameComponent, so it inherits from it the _draw() method.

    Class-level attributes:
        BOARD_FILE_NAME (str): The name of the board file.
        POT_FILE_NAME (str): The name of the pot file.
        Y_OFFSET (int): The offset on the y-axis.
        LEFT_POT_X_OFFSET (int): The offset of the left pot on the x-axis.
        LEFT_POT_Y_OFFSET (int): The offset of the left pot on the y-axis.
        RIGHT_POT_X_OFFSET (int): The offset of the right pot on the x-axis.
        RIGHT_POT_Y_OFFSET (int): The offset of the right pot on the y-axis.

    Attributes:
        window (pygame.Surface): The window where the board is drawn.
        board (pygame.Surface): The image of the board.
        board_coordinates (tuple): The coordinates of the board.
        left_pot (PotComponent): The left pot.
        right_pot (PotComponent): The right pot.
    """

    BOARD_FILE_NAME = 'board.png'
    POT_FILE_NAME = 'player_pot.png'
    Y_OFFSET = 50
    LEFT_POT_X_OFFSET = 100
    LEFT_POT_Y_OFFSET = -80
    RIGHT_POT_X_OFFSET = -100
    RIGHT_POT_Y_OFFSET = 100

    def __init__(self, window: pygame.Surface, images_path):
        """
        The constructor initializing the attributes of the class.
        :param window: pygame window from parent
        :param images_path: the path of the images
        """
        super().__init__()
        self.window = window

        self.board = pygame.image.load(os.path.join(images_path,
                                                    self.BOARD_FILE_NAME))
        self.board = pygame.transform.scale(self.board,
                                            (AppSettings.board_width,
                                             AppSettings.board_height))
        board_x = (self.window.get_width() // 2
                   - AppSettings.board_width // 2)
        board_y = (self.window.get_height() // 2
                   - AppSettings.board_height // 2 + self.Y_OFFSET)
        self.board_coordinates = (board_x, board_y)

        self.left_pot = PotComponent(window,
                                     (self.board_coordinates[0]
                                      - PotComponent.pot_width
                                      + self.LEFT_POT_X_OFFSET,
                                      self.board_coordinates[1]
                                      + self.LEFT_POT_Y_OFFSET),
                                     images_path)
        self.right_pot = PotComponent(window,
                                      (self.board_coordinates[0]
                                       + AppSettings.board_width
                                       + self.RIGHT_POT_X_OFFSET,
                                       self.board_coordinates[1]
                                       + AppSettings.board_height
                                       - PotComponent.pot_height
                                       + self.RIGHT_POT_Y_OFFSET),
                                      images_path)

    def _draw(self):
        """Draws the board: the image of the board and the pots."""
        self.window.blit(self.board, (self.board_coordinates[0], self.board_coordinates[1]))
        self.left_pot._draw()
        self.right_pot._draw()
