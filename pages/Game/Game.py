import os.path
import sys

import pygame

from AppSettings import AppSettings
from pages.Game.Components import BackgroundComponent as Bg
from pages.Game.Components import BoardComponent as Board
from pages.Game.Components import LabelComponent as Label
from pages.Game.Components import HighlightingSystem as Highlighting
from pages.ViewModel import ViewModel
from pages.Game.Components import StoneSystem as Stone


class Game(ViewModel):
    game_images_path = os.path.join('images', 'Game')

    def __init__(self, window: pygame.Surface):
        super().__init__()
        self.window = window

        self.bg = Bg.BackgroundComponent(self.window, self.game_images_path)
        self.board = Board.BoardComponent(self.window, self.game_images_path)

        pit_1_coordinates = (self.board.board_coordinates[0] + 57, self.board.board_coordinates[1] + 47)
        self.highlighting = Highlighting.HighlightingSystem(self.window, pit_1_coordinates)

        self.stones = Stone.StoneSystem(self.window, self.highlighting.pits_coordinates)

    def __draw_player_turn_label(self, player_turn):

        player_turn_label = Label.LabelComponent(self.window,
                                                 (self.window.get_width() // 2,
                                                  (self.window.get_height() // 2 - self.board.board_height // 2) // 2),
                                                 f"Player {player_turn} turn",
                                                 72,
                                                 AppSettings.colors['white'],
                                                 True, background_color=AppSettings.colors['orange_h2'])

        indication = Label.LabelComponent(self.window,
                                          (self.window.get_width() // 2,
                                           (self.window.get_height() // 2 - self.board.board_height // 2) // 2 + 50),
                                          "Click on one of your pits (highlighted in orange) to move",
                                          36,
                                          AppSettings.colors['white'])

        player_turn_label._draw()
        indication._draw()
        player_turn_label.animate_scaling()

    def __draw_player_score_label(self, player, score):
        if player == 1:
            x = self.board.left_pot_coordinates[0] + self.board.pot_width // 2
            y = self.board.left_pot_coordinates[1] + self.board.pot_height - 70
            player1_label = Label.LabelComponent(self.window, (x, y), f"Player 1 Score: {score}", 36,
                                                 AppSettings.colors['white'], True,
                                                 AppSettings.colors['orange_h2'])
            player1_label._draw()
        else:
            x = self.board.right_pot_coordinates[0] + self.board.pot_width // 2
            y = self.board.right_pot_coordinates[1] + 45
            player2_label = Label.LabelComponent(self.window, (x, y), f"Player 2 Score: {score}", 36,
                                                 AppSettings.colors['white'], True,
                                                 AppSettings.colors['orange_h2'])
            player2_label._draw()

    def _load_view(self):
        self.bg._draw()
        self.board._draw()

        self.__draw_player_score_label(1, 0)
        self.__draw_player_score_label(2, 0)

        self.stones._draw()

        self.highlighting.set_highlighted_pits([0, 1, 2, 3, 4, 5])
        self.highlighting._draw()

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
