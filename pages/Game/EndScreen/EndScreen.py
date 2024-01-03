import os

import pygame

from AppSettings import AppSettings
from pages.ViewModel import ViewModel


class EndScreen(ViewModel):
    path_to_background_image = os.path.join('images', 'Game', 'EndScreen', 'end_screen.png')

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pygame.image.load(self.path_to_background_image)
        self.image = pygame.transform.scale(self.image, (AppSettings.board_height, AppSettings.board_width))
        self.image_coordinates = (self.window.get_width() // 2 - AppSettings.board_width // 2,
                                  self.window.get_height() // 2 - AppSettings.board_height // 2 + 50)

    def _load_view(self):
        self.window.blit(self.image, self.image_coordinates)
        pygame.display.update()

    def _listen_for_events(self):
        pass

    def loop(self):
        self._load_view()
        self._listen_for_events()
