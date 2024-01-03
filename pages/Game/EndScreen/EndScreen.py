import os
import sys

import pygame

from AppSettings import AppSettings
from ViewTree import ViewTree
from pages.ViewModel import ViewModel
from pages.UI.Components.ButtonComponent import ButtonComponent


class EndScreen(ViewModel):
    button_width = 100
    button_height = 50
    path_to_background_image = os.path.join('images', 'Game', 'EndScreen', 'end_screen.png')

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.image = pygame.image.load(self.path_to_background_image)
        self.image = pygame.transform.scale(self.image, (AppSettings.board_height, AppSettings.board_width))
        self.image_coordinates = (self.window.get_width() // 2 - AppSettings.board_width // 2,
                                  self.window.get_height() // 2 - AppSettings.board_height // 2 + 50)

        self.play_again_button = ButtonComponent(self.window, "Play again",
                                                  (self.window.get_width() // 2 - self.button_width,
                                                   self.window.get_height() // 3 * 2),
                                                  (self.button_width, self.button_height))
        self.quit_button = ButtonComponent(self.window, "Quit",
                                            (self.window.get_width() // 2, self.window.get_height() // 3 * 2),
                                            (self.button_width, self.button_height))

    def _load_view(self):
        self.window.blit(self.image, self.image_coordinates)
        self.play_again_button._draw()
        self.quit_button._draw()
        pygame.display.update()

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_again_button.button_rect.collidepoint(event.pos):
                    from pages.Game.Game import Game
                    ViewTree.pop_view()
                    ViewTree.pop_view()
                    ViewTree.push_view(Game(self.window))
                elif self.quit_button.button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def loop(self):
        self._load_view()
        self._listen_for_events()
