import os

import pygame
from AppSettings import AppSettings


class ButtonComponent:
    def __init__(self, window, text, coordinates, size, background_image_path, display_centered=True, text_color=AppSettings.colors['light_gray'], hover_text_color=AppSettings.colors['black']):
        self.window = window
        self.text = text
        self.coordinates = coordinates
        self.size = size
        self.display_centered = display_centered
        self.background_image_path = background_image_path
        self.background_image = pygame.image.load(self.background_image_path)
        self.background_image = pygame.transform.scale(self.background_image, self.size)
        self.button_rect = pygame.Rect(coordinates[0], coordinates[1], size[0], size[1])
        self.text_color = text_color
        self.hover_text_color = hover_text_color
        self.first = True

    def _draw(self):
        if self.button_rect.collidepoint(pygame.mouse.get_pos()) or self.first is True:
            self.window.blit(self.background_image, (self.button_rect.x, self.button_rect.y - 5))
            self.__display_text(self.text, self.hover_text_color, self.button_rect)
            self.first = False
        else:
            self.window.blit(self.background_image, self.button_rect)
            self.__display_text(self.text, self.text_color, self.button_rect)

    def __display_text(self, text, color, rect):
        if self.display_centered:
            self.__display_text_centered(text, color, rect)
        else:
            self.__display_text_normal(text, color, rect)

    def __display_text_centered(self, text, color, rect):
        text_surface = AppSettings.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.window.blit(text_surface, text_rect)

    def __display_text_normal(self, text, color, rect):
        text_surface = AppSettings.font.render(text, True, color)
        self.window.blit(text_surface, rect)
