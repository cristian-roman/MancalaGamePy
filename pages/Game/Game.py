import os.path
import random
import sys

import pygame

from AppSettings import AppSettings
from pages.Game.Components import BackgroundComponent as Bg
from pages.Game.Components import BoardComponent as Board
from pages.Game.Components import LabelComponent as Label
from pages.ViewModel import ViewModel
from pages.Game.Components.PitComponent.PitSystem import PitSystem


class Game(ViewModel):
    game_images_path = os.path.join('images', 'Game')

    def __init__(self, window: pygame.Surface):
        super().__init__()
        self.window = window

        self.bg = Bg.BackgroundComponent(self.window, self.game_images_path)
        self.board = Board.BoardComponent(self.window, self.game_images_path)

        pit_1_coordinates = (self.board.board_coordinates[0] + 57, self.board.board_coordinates[1] + 47)
        self.pits_system = PitSystem(self.window, pit_1_coordinates)

        self.player_turn = random.randint(1, 2)

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

    def _load_view(self):
        self.bg._draw()
        self.board._draw()

        self.pits_system.set_highlighted_pits(self.player_turn)
        self.pits_system._draw()

        self.__draw_player_turn_label(self.player_turn)

        pygame.display.update()

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if self.__did_mouse_moved():
            self.pit_index = self.pits_system.treat_hovering(pygame.mouse.get_pos(), self.player_turn)

        if pygame.mouse.get_pressed()[0] and self.pit_index is not None:
            self.pits_system.move_stones(self.pit_index, self.board.left_pot, self.board.right_pot, self.player_turn)

    @staticmethod
    def __did_mouse_moved():
        return pygame.mouse.get_rel() != (0, 0)

    def loop(self):
        self._listen_for_events()
        self._load_view()
        pygame.display.update()
