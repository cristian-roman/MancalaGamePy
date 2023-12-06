import pygame


class AppSettings:
    name = "Mancala Game"
    width = 800
    height = 600
    colors = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'light_gray': (200, 200, 200),
    }

    font = None

    @staticmethod
    def init(font):
        AppSettings.font = font
