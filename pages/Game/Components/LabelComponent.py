import pygame
from pages.Game.Components.GameComponent import GameComponent


class LabelComponent(GameComponent):
    """
    A class that helps with drawing text on the screen.

    It is a GameComponent, so it inherits from it the _draw() method.

    Attributes:
        window (pygame.Surface): The window where the label is drawn.
        position (tuple): The position of the label.
        text (str): The text of the label.
        size (int): The size of the label.
        color (tuple): The color of the label.
        has_background (bool):  True if the label has a background,
                                False otherwise.
        background_color (tuple): The color of the background of the label.
        background_shape (str): The shape of the background of the label.
    """

    def __init__(self, window,
                 position,
                 text, size,
                 color,
                 has_background=False,
                 background_color=None,
                 background_shape=None):
        """
        The constructor initializing the attributes of the class.
        :param window: the pygame window
        :param position: the position of the label
        :param text: the text of the label
        :param size: the font size of the label
        :param color: the color of the label
        :param has_background:  True if the label has a background,
                                False otherwise
        :param background_color: the color of the background of the label
        :param background_shape: the shape of the background of the label
        """
        super().__init__()
        self.text_surface = None
        self.text_rect = None
        self.window = window
        self.position = position
        self.text = text
        self.size = size
        self.color = color
        self.has_background = has_background
        self.background_color = background_color
        self.background_shape = background_shape

    def set_text(self, text):
        """Sets the text of the label."""
        self.text = text

    def set_background_color(self, color):
        """Sets the background color of the label."""
        self.background_color = color

    def _draw(self):
        """The method that draws the label."""
        self.text_surface = (pygame.font.Font(None, self.size)
                             .render(self.text, True, self.color))
        self.text_rect = (self.text_surface
                          .get_rect(center=self.position))
        if self.has_background:
            background_rect = pygame.Rect(self.text_rect.x - 10,
                                          self.text_rect.y - 5,
                                          self.text_rect.width + 20,
                                          self.text_rect.height + 10)
            # offsets that make the background a bit bigger than the text
            if self.background_shape == 'ellipse':
                pygame.draw.ellipse(self.window,
                                    self.background_color,
                                    background_rect)
            else:
                pygame.draw.rect(self.window,
                                 self.background_color,
                                 background_rect)
        self.window.blit(self.text_surface, self.text_rect)
