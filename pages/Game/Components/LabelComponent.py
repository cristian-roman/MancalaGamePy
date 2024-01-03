import time

import pygame

from pages.Game.Components.GameComponent import GameComponent


class LabelComponent(GameComponent):

    def __init__(self, window,
                 position,
                 text, size,
                 color,
                 has_background=False,
                 background_color=None,
                 background_shape=None):
        super().__init__()
        self.text_surface = None
        self.text_rect = None
        self.window = window
        self.position = position
        self.text = text
        self.size = size
        self.color = color
        self.has_background = has_background
        self.background_color = background_color
        self.background_shape = background_shape

    def set_text(self, text):
        self.text = text

    def _draw(self):
        self.text_surface = pygame.font.Font(None, self.size).render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.position)
        if self.has_background:
            background_rect = pygame.Rect(self.text_rect.x - 10, self.text_rect.y - 5,
                                          self.text_rect.width + 20, self.text_rect.height + 10)
            if self.background_shape == 'ellipse':
                pygame.draw.ellipse(self.window, self.background_color, background_rect)
            else:
                pygame.draw.rect(self.window, self.background_color, background_rect)
        self.window.blit(self.text_surface, self.text_rect)