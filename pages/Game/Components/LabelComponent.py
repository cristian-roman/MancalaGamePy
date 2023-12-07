import time

import pygame

from pages.Game.Components.GameComponent import GameComponent
from AppSettings import AppSettings


class LabelComponent(GameComponent):

    def __init__(self, window, position, text, color, has_background=False, background_color=None):
        super().__init__()
        self.text_surface = None
        self.text_rect = None
        self.window = window
        self.position = position
        self.text = text
        self.color = color
        self.has_background = has_background
        self.background_color = background_color

    def _draw(self):
        self.text_surface = AppSettings.font.render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.position)
        if self.has_background:
            background_rect = pygame.Rect(self.text_rect.x - 10, self.text_rect.y - 5,
                                          self.text_rect.width + 20, self.text_rect.height + 10)
            pygame.draw.rect(self.window, self.background_color, background_rect)
        self.window.blit(self.text_surface, self.text_rect)

    def animate_scaling(self):
        clock = pygame.time.Clock()
        frame_rate = 15  # Adjust the frame rate as needed
        delta_time = 1.0 / frame_rate

        for i in range(10):
            scale_factor = 1.0 + i * 0.01
            scaled_text = pygame.transform.scale(self.text_surface,
                                                 (int(self.text_rect.width * scale_factor),
                                                  int(self.text_rect.height * scale_factor)))
            scaled_rect = scaled_text.get_rect(center=self.text_rect.center)

            background_rect = pygame.Rect(scaled_rect.x - 10, scaled_rect.y - 5,
                                          scaled_rect.width + 20, scaled_rect.height + 10)

            pygame.draw.rect(self.window, AppSettings.colors['orange_h2'], background_rect)
            self.window.blit(scaled_text, scaled_rect)
            pygame.display.update()

            clock.tick(frame_rate)
            time.sleep(delta_time)

        for i in range(10):
            scale_factor = 1.1 - i * 0.01
            scaled_text = pygame.transform.scale(self.text_surface,
                                                 (int(self.text_rect.width * scale_factor),
                                                  int(self.text_rect.height * scale_factor)))
            scaled_rect = scaled_text.get_rect(center=self.text_rect.center)

            background_rect = pygame.Rect(scaled_rect.x - 10, scaled_rect.y - 5,
                                          scaled_rect.width + 20, scaled_rect.height + 10)

            pygame.draw.rect(self.window, AppSettings.colors['orange_h2'], background_rect)
            self.window.blit(scaled_text, scaled_rect)
            pygame.display.update()

            clock.tick(frame_rate)
            time.sleep(delta_time)
