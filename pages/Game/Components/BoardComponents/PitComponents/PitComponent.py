import random
import pygame
from AppSettings import AppSettings
from pages.Game.Components.GameComponent import GameComponent
from pages.Game.Components.BoardComponents.PitComponents.StoneComponent import StoneComponent
from pages.Game.Components.LabelComponent import LabelComponent


class PitComponent(GameComponent):
    """A class that represents a container where stones are stored.
    It is a GameComponent, so it inherits from it the _draw() method.

    Class-level attributes:
        PIT_WIDTH (int): The width of the pit.
        PIT_HEIGHT (int): The height of the pit.
        DEFAULT_STONE_NUMBER (int):
            The default number of stones contained in the pit.
        DEFAULT_HIGHLIGHT_WIDTH (int):
            The default width of the ellipse that highlights the pit.
        DEFAULT_LABEL_SIZE (int):
            The default size of the label
            that shows the number of stones contained in the pit.

    Attributes:
        window (pygame.Surface): The window where the pit is drawn.
        pit_coordinates (tuple): The coordinates of the pit.
        pit_index (int): The index of the pit on the table.
    """
    PIT_WIDTH = 102
    PIT_HEIGHT = 155
    DEFAULT_STONE_NUMBER = 4
    DEFAULT_HIGHLIGHT_WIDTH = 4
    DEFAULT_LABEL_SIZE = 50

    def __init__(self, window, pit_coordinates, pit_index):
        """
        The constructor initializing the attributes of the class.

        It sets the window, the pit coordinates and the pit index
        and initializes the stones contained in the pit.
        It also initializes the label
        that shows the number of stones contained in the pit.

        Args:
            window (pygame.Surface): The window where the pit is drawn.
            pit_coordinates (tuple): The coordinates of the pit.
            pit_index (int): The index of the pit.
        """
        self.window = window
        self.pit_coordinates = pit_coordinates
        self.pit_index = pit_index
        self.is_highlighted = False
        self.highlight_width = self.DEFAULT_HIGHLIGHT_WIDTH

        self.generator_number = random.randint(1, 5)
        self.stones = list()
        for i in range(self.DEFAULT_STONE_NUMBER):
            self.__init_stone()

        if self.pit_coordinates[1] < self.window.get_height() // 2:
            label_y = self.pit_coordinates[1] - 20
            self.background_color = AppSettings.colors['orange_h4']
        else:
            label_y = self.pit_coordinates[1] + self.PIT_HEIGHT + 20
            self.background_color = AppSettings.colors['orange_h6']

        self.label = LabelComponent(self.window,
                                    position=(self.pit_coordinates[0] + self.PIT_WIDTH // 2,
                                              label_y),
                                    text=str(self.DEFAULT_STONE_NUMBER),
                                    size=self.DEFAULT_LABEL_SIZE,
                                    color=AppSettings.colors['white'],
                                    has_background=True,
                                    background_color=self.background_color,
                                    background_shape='ellipse')

    def __init_stone(self):
        """Initialize the stone with a random number"""
        self.generator_number = (self.generator_number + 1) % 5 + 1
        self.stones.append(StoneComponent(self.window,
                                          self.pit_coordinates,
                                          self.generator_number))

    def is_mouse_hovering(self, mouse_position):
        """
        Check if the mouse is hovering the pit
        by checking if the mouse position is in the zone defined by
        pit coordinates and size.
        It sets the highlight width to default value
        for the cases when the mouse is not hovering the pit.
        :param mouse_position:
        :return: True if the mouse is hovering the pit, False otherwise.
        """
        self.highlight_width = self.DEFAULT_HIGHLIGHT_WIDTH
        zone = pygame.Rect(self.pit_coordinates[0],
                           self.pit_coordinates[1],
                           self.PIT_WIDTH,
                           self.PIT_HEIGHT)
        return zone.collidepoint(mouse_position)

    def treat_hovering(self):
        """
        Sets the highlight width to 10
        and redraw the pit if the pit is not highlighted.
        """
        if not self.is_highlighted:
            return
        self.highlight_width = 10
        self._draw()
        pygame.display.update()

    def add_stone(self, stone):
        """Add a stone that was picked from another pit
        to the current pit."""
        self.stones.append(stone)

    def highlight(self):
        """Sets the is_highlighted attribute to True."""
        self.is_highlighted = True

    def delete_highlight(self):
        """Sets the is_highlighted attribute to False."""
        self.is_highlighted = False

    def _draw(self):
        """
        Draw the pit with its stones
        and the label that shows the number of stones
        contained in the pit.
        If the pit is highlighted,
        draw the ellipse that highlights the pit.
        Else, erase the ellipse that highlights the pit.
        """
        self.label.set_text(str(len(self.stones)))
        self.label._draw()
        for stone in self.stones:
            stone._draw()
        if self.is_highlighted:
            self.__draw_ellipse()
        else:
            self.__erase_ellipse()

    def __draw_ellipse(self):
        """
        Draw the ellipse that highlights the pit
        in the zone defined by pit coordinates and size
        with the highlight width
        and the background color defined in constructor
        """
        zone = pygame.Rect(self.pit_coordinates[0],
                           self.pit_coordinates[1],
                           self.PIT_WIDTH,
                           self.PIT_HEIGHT)
        pygame.draw.ellipse(self.window,
                            self.background_color,
                            zone,
                            self.highlight_width)

    def __erase_ellipse(self):
        """Erase the ellipse that highlights the pit
        by drawing a transparent ellipse in the same zone."""
        ellipse_surface = pygame.Surface((self.PIT_WIDTH,
                                          self.PIT_HEIGHT),
                                         pygame.SRCALPHA)
        pygame.draw.ellipse(ellipse_surface,
                            AppSettings.colors['no_color'],
                            (0, 0, self.PIT_WIDTH, self.PIT_HEIGHT))
        self.window.blit(ellipse_surface, self.pit_coordinates)
