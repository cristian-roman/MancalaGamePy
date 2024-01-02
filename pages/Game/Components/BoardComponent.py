import os

import pygame
from pages.Game.Components.GameComponent import GameComponent
from pages.Game.Components.PotComponent import PotComponent


class BoardComponent(GameComponent):
    board_file_name = 'board.png'
    board_width = 800
    board_height = 500

    pot_file_name = 'player_pot.png'

    def __init__(self, window: pygame.Surface, images_path):
        super().__init__()
        self.window = window

        self.board = pygame.image.load(os.path.join(images_path, self.board_file_name))
        self.board = pygame.transform.scale(self.board, (self.board_width, self.board_height))
        board_x = self.window.get_width() // 2 - self.board_width // 2
        board_y = self.window.get_height() // 2 - self.board_height // 2 + 50
        self.board_coordinates = (board_x, board_y)

        self.left_pot = PotComponent(window,
                                     (self.board_coordinates[0] - PotComponent.pot_width + 100, self.board_coordinates[1] - 80),
                                     images_path)
        self.right_pot = PotComponent(window,
                                      (self.board_coordinates[0] + self.board_width - 100, self.board_coordinates[1] + self.board_height + 100),
                                      images_path)

    def _draw(self):
        self.window.blit(self.board, (self.board_coordinates[0], self.board_coordinates[1]))
        self.left_pot._draw()
        self.right_pot._draw()
