import os

import pygame
from pages.Game.Components.GameComponent import GameComponent


class BoardComponent(GameComponent):
    board_file_name = 'board.png'
    board_width = 800
    board_height = 500

    pot_file_name = 'player_pot.png'
    pot_width = 400
    pot_height = 400

    def __init__(self, window: pygame.Surface, images_path):
        super().__init__()
        self.left_pot_coordinates = None
        self.right_pot_coordinates = None
        self.board_coordinates = None
        self.window = window

        self.board = pygame.image.load(os.path.join(images_path, self.board_file_name))
        self.board = pygame.transform.scale(self.board, (self.board_width, self.board_height))
        self.pot = pygame.image.load(os.path.join(images_path, self.pot_file_name))
        self.pot = pygame.transform.scale(self.pot, (self.pot_width, self.pot_height))

    def _draw(self):
        board_x = self.window.get_width() // 2 - self.board_width // 2
        board_y = self.window.get_height() // 2 - self.board_height // 2
        self.board_coordinates = (board_x, board_y)
        self.window.blit(self.board, (board_x, board_y))

        left_pot_x = board_x - self.pot_width + 100
        left_pot_y = board_y - 80
        self.left_pot_coordinates = (left_pot_x, left_pot_y)
        self.window.blit(self.pot, (left_pot_x, left_pot_y))

        right_pot_x = board_x + self.board_width - 100
        right_pot_y = board_y + self.board_height - self.pot_height + 100
        self.right_pot_coordinates = (right_pot_x, right_pot_y)
        self.window.blit(self.pot, (right_pot_x, right_pot_y))
