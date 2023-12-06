import os
import sys

import pygame

from models.ViewModel import ViewModel
from AppSettings import AppSettings
from models.Game import Game
from ViewTree import ViewTree


class UI(ViewModel):
    button_width = 100
    button_height = 50
    ui_images_path = os.path.join('images', 'UI')

    def __init__(self, window: pygame.Surface):
        self.window = window

        self.bg_image_path = os.path.join(self.ui_images_path, 'background.jpeg')
        self.button_bg_image_path = os.path.join(self.ui_images_path, 'button-bg.jpeg')

        self.ui_bg_image = pygame.image.load(self.bg_image_path)
        self.ui_bg_image = pygame.transform.scale(self.ui_bg_image, (self.window.get_width(), self.window.get_height()))

        self.button_bg_image = pygame.image.load(self.button_bg_image_path)
        self.button_bg_image = pygame.transform.scale(self.button_bg_image, (self.button_width, self.button_height))

        self.play_button_rect = pygame.Rect(self.window.get_width() // 2 - self.button_width,
                                            self.window.get_height() // 3 * 2,
                                            self.button_width, self.button_height)

        self.quit_button_rect = pygame.Rect(self.window.get_width() // 2,
                                            self.window.get_height() // 3 * 2,
                                            100, 50)

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button_rect.collidepoint(event.pos):
                    ViewTree.push_view(Game(self.window))
                elif self.quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

    def __display_text_centered(self, text, color, rect):
        text_surface = AppSettings.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=rect.center)
        self.window.blit(text_surface, text_rect)

    def _load_view(self):
        self.window.blit(self.ui_bg_image, (0, 0))

        if self.play_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.window.blit(self.button_bg_image, (self.play_button_rect.x, self.play_button_rect.y - 5))
            self.__display_text_centered("Play", AppSettings.colors['black'], self.play_button_rect)
        else:
            self.window.blit(self.button_bg_image, (self.play_button_rect.x, self.play_button_rect.y))
            self.__display_text_centered("Play", AppSettings.colors['light_gray'], self.play_button_rect)

        if self.quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.window.blit(self.button_bg_image, (self.quit_button_rect.x, self.quit_button_rect.y - 5))
            self.__display_text_centered("Quit", AppSettings.colors['black'], self.quit_button_rect)
        else:
            self.window.blit(self.button_bg_image, (self.quit_button_rect.x, self.quit_button_rect.y))
            self.__display_text_centered("Quit", AppSettings.colors['light_gray'], self.quit_button_rect)

    def loop(self):
        self._listen_for_events()
        self._load_view()
        pygame.display.update()
