import os

import pygame
from pages.Game.Components.GameComponent import GameComponent


class StoneSystem(GameComponent):
    stone_images_path = os.path.join('images', 'Game', 'Stones')

    def __init__(self, window: pygame.Surface, pit_coordinates):
        self.window = window
        self.pit_coordinates = pit_coordinates

        self.stone_1 = pygame.image.load(os.path.join(self.stone_images_path, 'stone_1.png'))
        self.stone_1 = pygame.transform.scale(self.stone_1, (150, 150))

        self.stone_2 = pygame.image.load(os.path.join(self.stone_images_path, 'stone_2.png'))
        self.stone_2 = pygame.transform.scale(self.stone_2, (75, 75))

        self.stone_3 = pygame.image.load(os.path.join(self.stone_images_path, 'stone_3.png'))
        self.stone_3 = pygame.transform.scale(self.stone_3, (150, 150))

    def _draw(self):
        self.window.blit(self.stone_1, self.pit_coordinates[0])
        self.window.blit(self.stone_2, self.pit_coordinates[1])
        self.window.blit(self.stone_3, self.pit_coordinates[2])
