import os.path
import sys
import time

import pygame

from AppSettings import AppSettings
from pages.ViewModel import ViewModel
from pages.Game.Components import BoardComponent as Board
from pages.Game.Components import BackgroundComponent as Bg
from pages.Game.Components import LabelComponent as Label
from ViewTree import ViewTree


class Game(ViewModel):
    game_images_path = os.path.join('images', 'Game')

    def __init__(self, window: pygame.Surface):
        super().__init__()
        self.window = window

        self.bg = Bg.BackgroundComponent(self.window, self.game_images_path)
        self.board = Board.BoardComponent(self.window, self.game_images_path)

    def __draw_player_turn_label(self, player_turn):

        player_turn_label = Label.LabelComponent(self.window,
                                                 (self.window.get_width() // 2,
                                                  (self.window.get_height() // 2 - self.board.board_height // 2) // 2),
                                                 f"Player {player_turn} turn", AppSettings.colors['white'],
                                                 True,
                                                 AppSettings.colors['orange_h2'])

        player_turn_label._draw()
        player_turn_label.animate_scaling()

    def __draw_player_label(self, player, score):
        if player == 1:
            x = self.board.left_pot_coordinates[0] + self.board.pot_width // 2
            y = self.board.left_pot_coordinates[1] + self.board.pot_height - 50
            player1_label = Label.LabelComponent(self.window, (x, y), f"Player 1 Score: {score}",
                                                 AppSettings.colors['white'], True,
                                                 AppSettings.colors['orange_h2'])
            player1_label._draw()
        else:
            x = self.board.right_pot_coordinates[0] + self.board.pot_width // 2
            y = self.board.right_pot_coordinates[1] + self.board.pot_height - 50
            player2_label = Label.LabelComponent(self.window, (x, y), f"Player 2 Score: {score}",
                                                 AppSettings.colors['white'], True,
                                                 AppSettings.colors['orange_h2'])
            player2_label._draw()

    def _load_view(self):
        self.bg._draw()
        self.board._draw()

        # Call the function to draw player labels
        self.__draw_player_label(1, 0)
        self.__draw_player_label(2, 0)

        oval_rect = pygame.Rect(self.board.board_coordinates[0] + 57, self.board.board_coordinates[1] + 47, 102, 155)
        pygame.draw.ellipse(self.window, AppSettings.colors['orange_h4'], oval_rect, 4)

        self.__draw_player_turn_label(1)

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
