import pygame


class AppSettings:
    name = "Mancala Game"
    width = 1280
    height = 720
    colors = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'light_gray': (200, 200, 200),
        'green': (0, 255, 0),
        'orange_h4': (230, 115, 0),
        'orange_h2': (179, 89, 0),
        'no_color': (0, 0, 0, 0)
    }

    font = None

    @staticmethod
    def init(font):
        AppSettings.font = font
