import os.path
import sys

import pygame

from AppSettings import AppSettings
from models.ViewModel import ViewModel
from ViewTree import ViewTree


class Game(ViewModel):
    game_images_path = os.path.join('images', 'Game')

    table_width = 800
    table_height = 500

    pit_width = 400
    pit_height = 400

    def __init__(self, window: pygame.Surface):
        self.window = window

        self.bg_image_path = os.path.join(self.game_images_path, 'background.png')
        self.bg_image = pygame.image.load(self.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.window.get_width(), self.window.get_height()))

        self.board_path = os.path.join(self.game_images_path, 'board.png')
        self.board = pygame.image.load(self.board_path)
        self.board = pygame.transform.scale(self.board, (self.table_width, self.table_height))

        self.player_pot = os.path.join(self.game_images_path, 'player_pot.png')
        self.player_pot = pygame.image.load(self.player_pot)
        self.player_pot = pygame.transform.scale(self.player_pot, (self.pit_width, self.pit_height))

    def _load_view(self):
        self.window.blit(self.bg_image, (0, 0))

        board_x = self.window.get_width() // 2 - self.table_width // 2 + 10
        board_y = self.window.get_height() // 2 - self.table_height // 2
        self.window.blit(self.board, (board_x, board_y))

        left_pot_x = self.window.get_width() // 2 - self.table_width // 2 - self.pit_width + 95
        left_pot_y = self.window.get_height() // 2 - self.table_height // 2 + 40
        self.window.blit(self.player_pot, (left_pot_x, left_pot_y))

        right_pot_x = self.window.get_width() // 2 + self.table_width // 2 - 75
        right_pot_y = self.window.get_height() // 2 - self.table_height // 2 + 40
        self.window.blit(self.player_pot, (right_pot_x, right_pot_y))

        pygame.display.update()

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def loop(self):
        self._listen_for_events()
        self._load_view()
        pygame.display.update()
