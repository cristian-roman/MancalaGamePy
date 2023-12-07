import time

import pygame

from pages.Game.Components.GameComponent import GameComponent
from AppSettings import AppSettings


class LabelComponent(GameComponent):

    def __init__(self, window, position, text, size, color, has_background=False, background_color=None):
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

    def _draw(self):
        self.text_surface = pygame.font.Font(None, self.size).render(self.text, True, self.color)
        self.text_rect = self.text_surface.get_rect(center=self.position)
        if self.has_background:
            background_rect = pygame.Rect(self.text_rect.x - 10, self.text_rect.y - 5,
                                          self.text_rect.width + 20, self.text_rect.height + 10)
            pygame.draw.rect(self.window, self.background_color, background_rect)
        self.window.blit(self.text_surface, self.text_rect)

    def __animate_scale(self, start_factor, step):
        clock = pygame.time.Clock()
        frame_rate = 15
        delta_time = 1.0 / frame_rate

        scale_factor = start_factor
        for i in range(10):
            scale_factor += step
            scaled_text = pygame.transform.scale(self.text_surface,
                                                 (int(self.text_rect.width * scale_factor),
                                                  int(self.text_rect.height * scale_factor)))
            scaled_rect = scaled_text.get_rect(center=self.text_rect.center)

            pygame.draw.rect(self.window, self.background_color, scaled_rect)

            self.window.blit(scaled_text, scaled_rect)
            pygame.display.update()

            clock.tick(frame_rate)
            time.sleep(delta_time)
        return scale_factor

    def animate_scaling(self):
        # Scale up
        end_factor = self.__animate_scale(1.0, 0.01)

        # Scale down
        self.__animate_scale(end_factor, -0.01)
