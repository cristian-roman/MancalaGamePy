import os.path
import random
import sys

import pygame

from ViewTree import ViewTree
from AppSettings import AppSettings
from pages.Game.Components import BackgroundComponent as Bg
from pages.Game.Components.BoardComponents import BoardComponent as Board
from pages.Game.Components import LabelComponent as Label
from pages.ViewModel import ViewModel
from pages.Game.Components.BoardComponents.PitComponents.PitSystem import PitSystem
from pages.Game.EndScreen.EndScreen import EndScreen


class Game(ViewModel):
    game_images_path = os.path.join('images', 'Game')

    def __init__(self, window: pygame.Surface):
        super().__init__()
        self.is_game_over = False
        self.window = window

        self.bg = Bg.BackgroundComponent(self.window, self.game_images_path)
        self.board = Board.BoardComponent(self.window, self.game_images_path)

        self.pits_system = PitSystem(self.window, self.board.board_coordinates, self.board.left_pot,
                                     self.board.right_pot)

        self.player_turn = random.randint(1, 2)
        self.player_turn_label = Label.LabelComponent(self.window,
                                                      (self.window.get_width() // 2,
                                                       (
                                                               self.window.get_height() // 2 - AppSettings.board_height // 2) // 2),
                                                      f"Player {self.player_turn} turn",
                                                      72,
                                                      AppSettings.colors['white'],
                                                      True, background_color=AppSettings.colors['orange_h2'])

        self.indication = Label.LabelComponent(self.window,
                                               (self.window.get_width() // 2,
                                                (
                                                        self.window.get_height() // 2 - AppSettings.board_height // 2) // 2 + 50),
                                               "Click on one of your pits (highlighted in orange) to move",
                                               36,
                                               AppSettings.colors['white'])

    def __draw_player_turn_label(self):
        if self.player_turn == 1:
            self.player_turn_label.set_background_color(AppSettings.colors['orange_h2'])
        else:
            self.player_turn_label.set_background_color(AppSettings.colors['orange_h6'])

        self.player_turn_label._draw()

    def _load_view(self):
        self.bg._draw()
        self.board._draw()

        if not self.is_game_over:
            self.indication._draw()
            self.player_turn_label.set_text(f"Player {self.player_turn} turn")
            if self.pits_system.moving_stones is False:
                self.pits_system.set_highlighted_pits(self.player_turn)
            self.pits_system.draw()

        self.__draw_player_turn_label()
        pygame.display.update()

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.pit_index = self.pits_system.treat_hovering(pygame.mouse.get_pos(), self.player_turn)

        if (pygame.mouse.get_pressed()[0]
                and self.pit_index is not None
                and len(self.pits_system.pits[self.pit_index].stones) != 0):

            destination_list = self.pits_system.move_stones(self.pit_index, self.player_turn)
            last_destination = destination_list[-1]
            if not self.pits_system.is_last_destination_player_pot(last_destination, self.player_turn):

                if (self.pits_system.is_last_destination_player_pit(last_destination, self.player_turn)
                        and self.pits_system.was_pit_empty(last_destination)):
                    self.pits_system.move_all_to_player_pot(last_destination, self.player_turn)
                    opposite_pit_index = 14 - last_destination
                    self.pits_system.move_all_to_player_pot(opposite_pit_index, self.player_turn)

                self.player_turn = 1 if self.player_turn == 2 else 2

            player_finished = self.pits_system.is_game_over()

            if player_finished is not False:
                if player_finished == 1:
                    for i in range(8, 14):
                        self.pits_system.move_all_to_player_pot(i, 2)
                else:
                    for i in range(1, 7):
                        self.pits_system.move_all_to_player_pot(i, 1)
                self.player_turn_label.set_text(f"Player {self.get_winner()} won!")
                self.is_game_over = True

            self.pit_index = None

    def loop(self):
        self._listen_for_events()
        self._load_view()
        if self.is_game_over:
            ViewTree.push_view(EndScreen(self.window))

    def get_winner(self):
        if self.board.left_pot.get_score() > self.board.right_pot.get_score():
            return 1
        elif self.board.left_pot.get_score() < self.board.right_pot.get_score():
            return 2
        else:
            return 0
