import pygame
from AppSettings import AppSettings
from pages.Game.Components import GameComponent


class ButtonComponent(GameComponent):
    """
    This class is responsible for the button component.
    It is used to create buttons
    with the preferences defined in the constructor.

    It is a GameComponent, so it inherits from it the _draw() method.

    Attributes:
        window (pygame.Surface): The window where the button is drawn.
        text (str): The text of the button.
        coordinates (tuple): The coordinates of the button.
        size (tuple): The size of the button.
        background_image_path (str):    The path of the background image
                                        of the button.
        display_centered (bool):    True
                                    if the text of the button
                                    is displayed centered,
                                    False otherwise.
        button_rect (pygame.Rect):  The rectangle of the button.
        text_color (tuple): The color of the text of the button.
        hover_text_color (tuple): The color of the text of the button when hovered.
    """

    def __init__(self,
                 window,
                 text,
                 coordinates,
                 size,
                 background_image_path,
                 display_centered=True,
                 text_color=AppSettings.colors['light_gray'],
                 hover_text_color=AppSettings.colors['black']):
        """
        This constructor initializes the attributes of the class.

        :param window: the pygame window of the initiator
        :param text: the text on the button
        :param coordinates: where to draw the button
        :param size: the size of the button
        :param background_image_path:   the path
                                        of the background image of the button
        :param display_centered:    True if the text of the button
                                    is displayed centered,
                                    False for normal display
        :param text_color: the color of the text of the button
        :param hover_text_color:    the color of the text of the button
                                    when hovered
        """
        self.window = window
        self.text = text
        self.coordinates = coordinates
        self.size = size
        self.display_centered = display_centered
        self.background_image_path = background_image_path
        self.background_image \
            = pygame.image.load(self.background_image_path)
        self.background_image \
            = pygame.transform.scale(self.background_image, self.size)
        self.button_rect \
            = pygame.Rect(coordinates[0], coordinates[1], size[0], size[1])
        self.text_color = text_color
        self.hover_text_color = hover_text_color
        self.first = True

    def _draw(self):
        """
        This method draws the button.
        If the mouse is on the button,
        the text is displayed with the hover color
        :return: None
        """
        if (self.button_rect.collidepoint(pygame.mouse.get_pos())
                or self.first is True):
            self.window.blit(self.background_image,
                             (self.button_rect.x, self.button_rect.y - 5))
            self.__display_text(self.text,
                                self.hover_text_color,
                                self.button_rect)
            self.first = False
        else:
            self.window.blit(self.background_image, self.button_rect)
            self.__display_text(self.text,
                                self.text_color,
                                self.button_rect)

    def __display_text(self, text, color, rect):
        """
        This method controls how the text is displayed
        according to the display_centered attribute.
        """
        if self.display_centered:
            self.__display_text_centered(text, color, rect)
        else:
            self.__display_text_normal(text, color, rect)

    def __display_text_centered(self, text, color, rect):
        """This method displays the text centered."""
        text_surface = AppSettings.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.window.blit(text_surface, text_rect)

    def __display_text_normal(self, text, color, rect):
        """This method displays the text normally."""
        text_surface = AppSettings.font.render(text, True, color)
        self.window.blit(text_surface, rect)
