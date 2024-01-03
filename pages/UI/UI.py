import os
import sys

import pygame

from pages.ViewModel import ViewModel
from AppSettings import AppSettings
from pages.Game.Game import Game
from ViewTree import ViewTree
from pages.UI.Components.ButtonComponent import ButtonComponent


class UI(ViewModel):
    button_width = 100
    button_height = 50
    ui_images_path = os.path.join('images', 'UI')

    def __init__(self, window: pygame.Surface):
        super().__init__()
        self.window = window

        self.bg_image_path = os.path.join(self.ui_images_path, 'background.jpeg')
        self.bg_button_image_path = os.path.join(self.ui_images_path, 'button-bg.jpeg')

        self.ui_bg_image = pygame.image.load(self.bg_image_path)
        self.ui_bg_image = pygame.transform.scale(self.ui_bg_image, (self.window.get_width(), self.window.get_height()))

        self.play_button = ButtonComponent(self.window, "Play",
                                           (self.window.get_width() // 2 - self.button_width,
                                            self.window.get_height() // 3 * 2),
                                           (self.button_width, self.button_height),
                                           self.bg_button_image_path)

        self.quit_button = ButtonComponent(self.window, "Quit",
                                           (self.window.get_width() // 2, self.window.get_height() // 3 * 2),
                                           (self.button_width, self.button_height),
                                           self.bg_button_image_path)

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.button_rect.collidepoint(event.pos):
                    ViewTree.push_view(Game(self.window))
                elif self.quit_button.button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def _load_view(self):
        self.window.blit(self.ui_bg_image, (0, 0))
        self.play_button._draw()
        self.quit_button._draw()

    def loop(self):
        self._listen_for_events()
        self._load_view()
        pygame.display.update()
