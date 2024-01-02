import os.path
import random
import sys

import pygame

from AppSettings import AppSettings
from pages.Game.Components import BackgroundComponent as Bg
from pages.Game.Components.BoardComponents import BoardComponent as Board
from pages.Game.Components import LabelComponent as Label
from pages.ViewModel import ViewModel
from pages.Game.Components.BoardComponents.PitComponents.PitSystem import PitSystem


class Game(ViewModel):
    game_images_path = os.path.join('images', 'Game')

    def __init__(self, window: pygame.Surface):
        super().__init__()
        self.window = window

        self.bg = Bg.BackgroundComponent(self.window, self.game_images_path)
        self.board = Board.BoardComponent(self.window, self.game_images_path)

        self.pits_system = PitSystem(self.window, self.board.board_coordinates)

        self.player_turn = random.randint(1, 2)
        self.player_turn_label = Label.LabelComponent(self.window,
                                                      (self.window.get_width() // 2,
                                                       (
                                                               self.window.get_height() // 2 - self.board.board_height // 2) // 2),
                                                      f"Player {self.player_turn} turn",
                                                      72,
                                                      AppSettings.colors['white'],
                                                      True, background_color=AppSettings.colors['orange_h2'])

        self.indication = Label.LabelComponent(self.window,
                                               (self.window.get_width() // 2,
                                                (
                                                        self.window.get_height() // 2 - self.board.board_height // 2) // 2 + 50),
                                               "Click on one of your pits (highlighted in orange) to move",
                                               36,
                                               AppSettings.colors['white'])

    def _load_view(self):
        self.bg._draw()
        self.board._draw()

        self.player_turn_label.set_text(f"Player {self.player_turn} turn")
        self.indication._draw()

        self.pits_system.set_highlighted_pits(self.player_turn)
        self.pits_system.draw()

        self.player_turn_label._draw()
        pygame.display.update()

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.pit_index = self.pits_system.treat_hovering(pygame.mouse.get_pos(), self.player_turn)
            if pygame.mouse.get_pressed()[0] and self.pit_index is not None:
                print("clicked")
                last_destination = self.pits_system.move_stones(self.pit_index, self.board.left_pot,
                                                                self.board.right_pot,
                                                                self.player_turn)

                if (last_destination == 'left_pot' and self.player_turn == 2 or
                        last_destination == 'right_pot' and self.player_turn == 1):
                    self.player_turn = 3 - self.player_turn

                elif last_destination != 'left_pot' and last_destination != 'right_pot' and (
                        self.pits_system.is_current_player_pit(last_destination, self.player_turn) and
                        len(self.pits_system.pits[last_destination].stones) == 1):
                    opposite_pit_index = abs(11 - self.pit_index)
                    print("opposite index of pit:", self.pit_index, "is", opposite_pit_index)

                    self.pits_system.move_all_to_player_pot(last_destination, self.board.left_pot,
                                                            self.board.right_pot,
                                                            self.player_turn)

                    self.pits_system.move_all_to_player_pot(opposite_pit_index, self.board.left_pot,
                                                            self.board.right_pot,
                                                            self.player_turn)
                else:
                    self.player_turn = 3 - self.player_turn

            if self.pits_system.is_game_over():
                self._load_view()
                self.indication.set_text(f"Player {self.get_winner()} won!")
                return

    def loop(self):
        self._listen_for_events()
        self._load_view()
        pygame.display.update()

    def get_winner(self):
        if self.board.left_pot.get_score() > self.board.right_pot.get_score():
            return 1
        elif self.board.left_pot.get_score() < self.board.right_pot.get_score():
            return 2
        else:
            return 0
