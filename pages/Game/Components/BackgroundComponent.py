import os
import pygame
from pages.Game.Components.GameComponent import GameComponent


class BackgroundComponent(GameComponent):
    """
    A class that represents the background of the game.

    It is a GameComponent, so it inherits from it the _draw() method.

    Class-level attributes:
        BACKGROUND_FILE_NAME (str): The name of the background file.

    Attributes:
        window (pygame.Surface): The window where the background is drawn.
        background (pygame.Surface): The image of the background.
    """
    BACKGROUND_FILE_NAME = 'background.jpeg'

    def __init__(self, window: pygame.Surface, images_path):
        """
        The constructor initializing the attributes of the class.
        :param window:  the pygame window from parent
        :param images_path:   the path of the images
        """
        super().__init__()
        self.window = window

        self.background = pygame.image.load(os.path.join
                                            (images_path,
                                             self.BACKGROUND_FILE_NAME))
        self.background = (
            pygame.transform.scale(self.background,
                                   (self.window.get_width(),
                                    self.window.get_height())))

    def _draw(self):
        """The method that draws the background."""
        self.window.blit(self.background, (0, 0))
