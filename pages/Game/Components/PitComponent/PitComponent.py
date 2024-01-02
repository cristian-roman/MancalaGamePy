import random

import pygame

from AppSettings import AppSettings
from pages.Game.Components.GameComponent import GameComponent
from pages.Game.Components.PitComponent.StoneComponent import StoneComponent
from pages.Game.Components.LabelComponent import LabelComponent


class PitComponent(GameComponent):
    pit_width = 102
    pit_height = 155

    def __init__(self, window, pit_coordinates, pit_index):
        self.window = window
        self.pit_coordinates = pit_coordinates
        self.pit_index = pit_index
        self.is_highlighted = False
        self.highlight_width = 4

        self.generator_number = random.randint(1, 5)
        self.stones = list()
        for i in range(4):
            self.__init_stone()

        if self.pit_coordinates[1] < self.window.get_height() // 2:
            label_y = self.pit_coordinates[1] - 20
        else:
            label_y = self.pit_coordinates[1] + self.pit_height + 20

        self.label = LabelComponent(self.window, (self.pit_coordinates[0] + self.pit_width // 2,
                                                  label_y),
                                    str(len(self.stones)), 50, AppSettings.colors['white'],
                                    True, AppSettings.colors['orange_h4'], 'ellipse')

    def __init_stone(self):
        self.generator_number = (self.generator_number + 1) % 5 + 1
        self.stones.append(StoneComponent(self.window, self.pit_coordinates, self.generator_number))

    def highlight(self):
        self.is_highlighted = True

    def delete_highlight(self):
        self.is_highlighted = False

    def __draw_ellipse(self):
        zone = pygame.Rect(self.pit_coordinates[0], self.pit_coordinates[1],
                           self.pit_width, self.pit_height)
        pygame.draw.ellipse(self.window, AppSettings.colors['orange_h4'], zone, self.highlight_width)

    def __erase_ellipse(self):
        ellipse_surface = pygame.Surface((self.pit_width, self.pit_height), pygame.SRCALPHA)
        pygame.draw.ellipse(ellipse_surface, AppSettings.colors['no_color'],
                            (0, 0, self.pit_width, self.pit_height))
        self.window.blit(ellipse_surface, self.pit_coordinates)

    def _draw(self):
        self.label._draw()
        for stone in self.stones:
            stone._draw()
        if self.is_highlighted:
            self.__draw_ellipse()
        else:
            self.__erase_ellipse()

    def is_mouse_hovering(self, mouse_position):
        self.highlight_width = 4
        zone = pygame.Rect(self.pit_coordinates[0], self.pit_coordinates[1],
                           self.pit_width, self.pit_height)
        return zone.collidepoint(mouse_position)

    def treat_hovering(self):
        if not self.is_highlighted:
            return
        self.highlight_width = 10
        self._draw()
        pygame.display.update()

