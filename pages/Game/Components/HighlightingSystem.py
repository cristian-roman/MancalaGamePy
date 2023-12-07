import pygame

from AppSettings import AppSettings
from pages.Game.Components.GameComponent import GameComponent


class HighlightingSystem(GameComponent):
    pit_width = 102
    pit_height = 155
    space_between_pits = 116.5
    height_between_rows = 261

    def __init__(self, window: pygame.Surface, left_top_most_pit_coordinates: tuple):
        self.highlighted_pits = None
        self.pits_coordinates = None
        self.window = window
        self.__generate_pits_coordinates(left_top_most_pit_coordinates)

    def __generate_pits_coordinates(self, left_top_most_pit_coordinates):
        self.pits_coordinates = list()
        self.pits_coordinates.append(left_top_most_pit_coordinates)

        for i in range(1, 6):
            next_pit_coordinates = (left_top_most_pit_coordinates[0] + self.space_between_pits * i,
                                    left_top_most_pit_coordinates[1])

            self.pits_coordinates.append(next_pit_coordinates)

        for i in range(6):
            next_pit_coordinates = (left_top_most_pit_coordinates[0] + self.space_between_pits * i,
                                    left_top_most_pit_coordinates[1] + self.height_between_rows)
            self.pits_coordinates.append(next_pit_coordinates)

    def set_highlighted_pits(self, highlighted_pits: list):
        self.highlighted_pits = highlighted_pits

    def _draw(self):
        if self.highlighted_pits is not None:
            for pit in self.highlighted_pits:
                zone = pygame.Rect(self.pits_coordinates[pit][0], self.pits_coordinates[pit][1],
                                   self.pit_width, self.pit_height)
                pygame.draw.ellipse(self.window, AppSettings.colors['orange_h4'], zone, 4)
