import random

import pygame

from AppSettings import AppSettings
from pages.Game.Components.GameComponent import GameComponent
from pages.Game.Components.PitComponent.StoneComponent import StoneComponent


class PitComponent(GameComponent):
    pit_width = 102
    pit_height = 155

    def __init__(self, window, pit_coordinates):
        self.window = window
        self.pit_coordinates = pit_coordinates

        self.generator_number = random.randint(1, 5)
        self.stones = list()
        for i in range(4):
            self.__init_stone()

    def __init_stone(self):
        self.generator_number = (self.generator_number + 1) % 5 + 1
        self.stones.append(StoneComponent(self.window, self.pit_coordinates, self.generator_number))

    def highlight(self):
        zone = pygame.Rect(self.pit_coordinates[0], self.pit_coordinates[1],
                           self.pit_width, self.pit_height)
        pygame.draw.ellipse(self.window, AppSettings.colors['orange_h4'], zone, 4)

    def _draw(self):
        for stone in self.stones:
            stone._draw()
