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
    """
    A class that represents the game.
    It inherits from ViewModel, so it is a page that inherits:
        - the loop() method
        - the _load_view() method
        - the _listen_for_events() method

    The loop method includes the _load_view()
    and _listen_for_events() methods.

    Class-level attributes:
        GAME_IMAGES_PATH (str): The path of the images.

    Attributes:
        is_game_over (bool): True if the game is over, False otherwise.
        window (pygame.Surface): The window where the game is drawn.
        bg (BackgroundComponent): The background of the game.
        board (BoardComponent): The board of the game.
        pits_system (PitSystem): The pit system of the game.
        player_turn (int): The player whose turn it is.
        player_turn_label (LabelComponent): The label that indicates
                                            whose turn it is.
        indication (LabelComponent): The label that indicates
                                     how to play.
        pve (bool): True if the game is player vs computer, False otherwise.
        player_turn (int): The player whose turn it is.
        first_load (bool): True if it is the first load of the game,
                           False otherwise.
    """
    GAME_IMAGES_PATH = os.path.join('images', 'Game')

    def __init__(self, window: pygame.Surface):
        """
        The constructor initializing the attributes of the class.

        :param window: the pygame window from previous view
        """
        super().__init__()
        self.is_game_over = False
        self.window = window

        self.bg = Bg.BackgroundComponent(self.window,
                                         self.GAME_IMAGES_PATH)
        self.board = Board.BoardComponent(self.window,
                                          self.GAME_IMAGES_PATH)

        self.pits_system = PitSystem(self.window,
                                     self.board.board_coordinates,
                                     self.board.left_pot,
                                     self.board.right_pot)

        self.player_turn = random.randint(1, 2)
        self.player_turn_label = (
            Label.LabelComponent(self.window,
                                 (self.window.get_width() // 2,
                                  (self.window.get_height() // 2
                                   - AppSettings.board_height // 2) // 2),
                                 f"Player {self.player_turn} turn",
                                 72,
                                 AppSettings.colors['white'],
                                 True,
                                 AppSettings.colors['orange_h2']))

        self.indication = (
            Label.LabelComponent(self.window,
                                 (self.window.get_width() // 2,
                                  (self.window.get_height() // 2
                                   - AppSettings.board_height // 2) // 2
                                  + 50),
                                 "Click on one of your pits "
                                 "(highlighted in orange) to move",
                                 36,
                                 AppSettings.colors['white']))

        self.pve = False
        self.player_turn = random.randint(1, 2)
        self.first_load = True

    def set_pve(self):
        """Sets the game mode to player vs computer."""
        self.pve = True

    def __draw_player_turn_label(self):
        """Draws the player turn label."""
        if self.player_turn == 1:
            (self.player_turn_label
             .set_background_color(AppSettings.colors['orange_h2']))
        else:
            (self.player_turn_label
             .set_background_color(AppSettings.colors['orange_h6']))

        self.player_turn_label._draw()

    def _load_view(self):
        """
        Loads the view by drawing the background, the board,
        the pots and the pits with stones.
        """
        self.bg._draw()
        self.board._draw()

        if not self.is_game_over:
            self.indication._draw()
            if self.pve and self.player_turn == 2:
                self.player_turn_label.set_text("Computer turn")
            else:
                (self.player_turn_label
                 .set_text(f"Player {self.player_turn} turn"))
            if self.pits_system.moving_stones is False:
                self.pits_system.set_highlighted_pits(self.player_turn)
            self.pits_system.draw()

        self.__draw_player_turn_label()
        pygame.display.update()

        if (self.first_load
                and self.pve is True
                and self.player_turn == 2):
            self.first_load = False
            pygame.time.delay(1000)

    def _listen_for_events(self):
        """
        Listens for events and treats them.

        The events are:
            - pygame.QUIT: quits the game
            - hovering over a pit: highlights the pit
            - clicking on a pit: moves the stones of the pit
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if self.pve and self.player_turn == 2:
            random_index = random.randint(8, 13)
            pos = self.pits_system.pits[random_index].pit_coordinates
            self.pit_index = (self.pits_system
                              .treat_hovering(pos, self.player_turn))
        else:
            self.pit_index = (self.pits_system
                              .treat_hovering(pygame.mouse.get_pos(),
                                              self.player_turn))

        if (self.pit_index is not None
                and pygame.mouse.get_pressed()[0]
                or (self.pve is True and self.player_turn == 2)):

            if len(self.pits_system.pits[self.pit_index].stones) == 0:
                return

            destination_list = (self.pits_system
                                .move_stones(self.pit_index,self.player_turn))
            last_destination = destination_list[-1]
            if not (self.pits_system.
                    is_last_destination_player_pot(last_destination,
                                                   self.player_turn)):

                if (self.pits_system.
                        is_last_destination_player_pit(last_destination,
                                                       self.player_turn)
                        and self.pits_system.was_pit_empty(last_destination)):
                    (self.pits_system
                     .move_all_to_player_pot(last_destination,
                                             self.player_turn))
                    opposite_pit_index = 14 - last_destination
                    (self.pits_system
                     .move_all_to_player_pot(opposite_pit_index, self.player_turn))

                self.player_turn = 1 if self.player_turn == 2 else 2

            player_finished = self.pits_system.is_game_over()

            if player_finished is not False:
                if player_finished == 1:
                    for i in range(8, 14):
                        self.pits_system.move_all_to_player_pot(i, 2)
                else:
                    for i in range(1, 7):
                        self.pits_system.move_all_to_player_pot(i, 1)

                winner = self.__get_winner()
                if winner == 1:
                    self.player_turn_label.set_text("Player 1 won!")
                elif winner == 2:
                    self.player_turn_label.set_text("Player 2 won!")
                else:
                    self.player_turn_label.set_text("It's a tie!")
                self.is_game_over = True
                self._load_view()

            self.pit_index = None

    def _loop(self):
        """
        The loop of the game.
        Loads the view and listens for events.
        """
        self._load_view()
        self._listen_for_events()
        if self.is_game_over:
            ViewTree.push_view(EndScreen(self.window))

    def __get_winner(self):
        """
        A query that returns the winner of the game.
        :return: 1 if player 1 has more stone stones in his pot,
                    2 if player 2 has more stone stones in his pot,
                    0 if it's a tie.
        """
        if (self.board.left_pot.get_score()
                > self.board.right_pot.get_score()):
            return 1
        elif (self.board.left_pot.get_score()
              < self.board.right_pot.get_score()):
            return 2
        else:
            return 0
