import os
import pygame
from pages.Game.Components.GameComponent import GameComponent
from AppSettings import AppSettings
import pages.Game.Components.LabelComponent as Label


class PotComponent(GameComponent):
    """
    A class that represents a pot.

    It is a GameComponent, so it inherits from it the _draw() method.

    Class-level attributes:
        POT_WIDTH (int): The width of the pot.
        POT_HEIGHT (int): The height of the pot.
        POT_FILE_NAME (str): The name of the pot file.

    Attributes:
        window (pygame.Surface): The window where the pot is drawn.
        pot_coordinates (tuple): The coordinates of the pot.
        stones_coordinates (tuple): The coordinates of the stones
                                    inside the pot.
        stones (list): The list of stones contained in the pot.
        score_label_x (int): The x-coordinate of the score label.
        score_label_y (int): The y-coordinate of the score label.
        score_label_text (str): The text of the score label.
        score_label (LabelComponent): The score label.
        color (tuple): The color of the score label.
        pot (pygame.Surface): The image of the pot.
    """
    POT_WIDTH = 400
    POT_HEIGHT = 400
    POT_FILE_NAME = 'player_pot.png'

    def __init__(self, window, pot_coordinates, images_path):
        """
        The constructor initializing the attributes of the class.

        It sets the window, the pot coordinates and the stones coordinates.
        It also initializes the score label.

        :param window: the pygame window of the parent
        :param pot_coordinates: the coordinates of the pot
        :param images_path: the path of the images
        """
        super().__init__()
        self.window = window
        self.pot_coordinates = pot_coordinates
        self.stones = list()

        self.score_label_x = (self.pot_coordinates[0]
                              + self.POT_WIDTH // 2)
        if pot_coordinates[1] < self.window.get_height() // 2:
            self.score_label_y = (self.pot_coordinates[1]
                                  + self.POT_HEIGHT - 70)
            # 70 is the offset of the label from the pot
            self.score_label_text = "Player 1 Score: "
            self.color = AppSettings.colors['orange_h2']
        else:
            self.score_label_y = self.pot_coordinates[1] + 45
            # 45 is the offset of the label from the pot
            self.score_label_text = "Player 2 Score: "
            self.color = AppSettings.colors['orange_h6']

        self.score_label = (Label
                            .LabelComponent(self.window,
                                            (self.score_label_x,
                                             self.score_label_y),
                                            self.score_label_text,
                                            36,
                                            AppSettings.colors['white'],
                                            True,
                                            self.color))

        self.pot = pygame.image.load(os.path.join
                                     (images_path,
                                      self.POT_FILE_NAME))
        self.pot = pygame.transform.scale(self.pot,
                                          (self.POT_WIDTH,
                                           self.POT_HEIGHT))

        self.stones_coordinates = (self.pot_coordinates[0] + 150,
                                   self.pot_coordinates[1] + 150)
        # 150 is the offset of the stones from the pot to the center

    def _draw(self):
        """The method that draws the pot and the score."""
        self.window.blit(self.pot, self.pot_coordinates)
        for stone in self.stones:
            stone._draw()

        self.score_label.set_text(self.score_label_text
                                  + str(len(self.stones)))
        self.score_label._draw()

    def add_stone(self, stone):
        """
        Adds a stone to the pot coming from another pot.
        :param stone: the stone to be added
        :return: None
        """
        self.stones.append(stone)

    def get_score(self):
        """
        Returns the score of the pot as the number of stones in the pot.
        :return: the score of the pot
        """
        return len(self.stones)
