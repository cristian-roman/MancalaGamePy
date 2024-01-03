import sys

import pygame

from ViewTree import ViewTree
from pages.UI.Components.ButtonComponent import ButtonComponent
from pages.ViewModel import ViewModel


class EndScreen(ViewModel):
    button_width = 125
    button_height = 62

    def __init__(self, window):
        super().__init__()
        self.window = window

        self.play_again_button = ButtonComponent(self.window, "Play again",
                                                 (self.window.get_width() // 2 - self.button_width,
                                                  self.window.get_height() // 3 * 2),
                                                 (self.button_width, self.button_height))
        self.quit_button = ButtonComponent(self.window, "Quit",
                                           (self.window.get_width() // 2, self.window.get_height() // 3 * 2),
                                           (self.button_width, self.button_height))

    def _load_view(self):
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
                    ViewTree.pop_view()
                    ViewTree.pop_view()
                elif self.quit_button.button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def loop(self):
        self._load_view()
        self._listen_for_events()
