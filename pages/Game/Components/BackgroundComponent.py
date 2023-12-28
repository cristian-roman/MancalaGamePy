import os

import pygame

from pages.Game.Components.GameComponent import GameComponent


class BackgroundComponent(GameComponent):

    background_file_name = 'background.jpeg'

    def __init__(self, window: pygame.Surface, images_path):
        super().__init__()
        self.window = window

        self.background = pygame.image.load(os.path.join(images_path, self.background_file_name))
        self.background = pygame.transform.scale(self.background, (self.window.get_width(), self.window.get_height()))

    def _draw(self):
        self.window.blit(self.background, (0, 0))
