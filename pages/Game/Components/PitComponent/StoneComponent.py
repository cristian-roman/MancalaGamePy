import os
import random

import pygame

from AppSettings import AppSettings
from pages.Game.Components.GameComponent import GameComponent


class StoneComponent(GameComponent):
    stone_images_path = os.path.join('images', 'Game', 'Stones')

    offsets = {
        1: (-30, -25),
        2: (-4, 42),
        3: (-28, 1),
        4: (-40, -45),
        5: (-39, 2),
    }

    sizes = {
        1: (150, 150),
        2: (75, 75),
        3: (100, 100),
        4: (150, 150),
        5: (150, 150),
    }

    def __init__(self, window, pit_coordinates, stone_index):
        super().__init__()
        self.stone_index = stone_index
        self.window = window

        self.stone = pygame.image.load(os.path.join(self.stone_images_path, f'stone_{stone_index}.png'))
        self.stone = pygame.transform.scale(self.stone, self.sizes[stone_index])
        self.stone = pygame.transform.rotate(self.stone, random.randint(0, 360))

        self.stone_coordinates = (pit_coordinates[0] + self.offsets[stone_index][0] + random.randint(-1, 1),
                                  pit_coordinates[1] + self.offsets[stone_index][1] + random.randint(-1, 1))

    def move_animate(self, new_coordinates):
        new_stone_coordinates = (new_coordinates[0] + self.offsets[self.stone_index][0] + random.randint(-1, 1),
                                 new_coordinates[1] + self.offsets[self.stone_index][1] + random.randint(-1, 1))
        self.__animate_move(new_stone_coordinates)

    def __delete_old_stone(self, old_coordinates):
        transparent_surface = pygame.Surface(self.stone.get_size(), pygame.SRCALPHA)
        transparent_surface.fill(AppSettings.colors['no_color'])
        transparent_surface.blit(self.stone, (0, 0))
        self.window.blit(transparent_surface, old_coordinates)

    def __animate_move(self, new_stone_coordinates):

        speed = 20

        multiplier_x = 1
        if new_stone_coordinates[0] < self.stone_coordinates[0]:
            multiplier_x = -1

        multiplier_y = 1
        if new_stone_coordinates[1] < self.stone_coordinates[1]:
            multiplier_y = -1

        step_x = (new_stone_coordinates[0] - self.stone_coordinates[0]) // speed * multiplier_x
        step_y = (new_stone_coordinates[1] - self.stone_coordinates[1]) // speed * multiplier_y

        for i in range(speed - 1):
            self.stone_coordinates = (self.stone_coordinates[0] + step_x,
                                      self.stone_coordinates[1] + step_y)
            self._draw()
            pygame.display.update()

        self.stone_coordinates = new_stone_coordinates
        self._draw()
        pygame.display.update()

    def _draw(self):
        self.window.blit(self.stone, self.stone_coordinates)
