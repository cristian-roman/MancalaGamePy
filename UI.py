import os

import pygame


class UI:
    ui_images_path = os.path.join(os.path.join(os.path.dirname(__file__), 'images'), 'UI')
    background_image_path = os.path.join(ui_images_path, 'background.jpeg')

    background_image = None

    @staticmethod
    def get_background_image():
        if UI.background_image is None:
            UI.background_image = pygame.image.load(UI.background_image_path)
        return UI.background_image
