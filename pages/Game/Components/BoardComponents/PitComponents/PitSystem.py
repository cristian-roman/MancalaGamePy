import pygame
from pages.Game.Components.BoardComponents.PitComponents.PitComponent import PitComponent


class PitSystem:
    """
    A class that controls all the highlighting of the pits
    and the movement of the stones.

    Class-level attributes:
        SPACE_BETWEEN_PITS (float): The space between two pits.
        HEIGHT_BETWEEN_PITS (float): The height between two pits.
        FIRST_PIT_X_OFFSET (float):
            The offset of the first pit on the x-axis.
        FIRST_PIT_Y_OFFSET (float):
            The offset of the first pit on the y-axis.

    Attributes:
        window (pygame.Surface): The window where the pits are drawn.
        left_pot (PitComponent): The left pot.
        right_pot (PitComponent): The right pot.
        pits (list): The list of pits.
        moving_stones (bool): True if the stones are moving, False otherwise.
    """
    SPACE_BETWEEN_PITS = 116.5
    HEIGHT_BETWEEN_PITS = 261
    FIRST_PIT_X_OFFSET = 57
    FIRST_PIT_Y_OFFSET = 47

    def __init__(self, window, board_coordinates, left_pot, right_pot):
        """
        :param window:  the pygame window
                        that contains the elements to be drawn
        :param board_coordinates:   the coordinates of the board
                                    from board component
        :param left_pot: player 1's pot component
        :param right_pot: player 2's pot component
        """
        self.window = window
        self.pits = list()
        self.left_pot = left_pot
        self.right_pot = right_pot
        self.pits.append(left_pot)
        self.__generate_pits(board_coordinates)
        self.moving_stones = False

    def __generate_pits(self, board_coordinates):
        """Generates the pits and adds them to the list of pits."""
        first_pit_coordinates = (board_coordinates[0]
                                 + self.FIRST_PIT_X_OFFSET,
                                 board_coordinates[1]
                                 + self.FIRST_PIT_Y_OFFSET)

        self.pits.append(PitComponent(self.window,
                                      first_pit_coordinates,
                                      1))
        for i in range(1, 6):
            next_pit_coordinates = (first_pit_coordinates[0] + self.SPACE_BETWEEN_PITS * i,
                                    first_pit_coordinates[1])
            self.pits.append(PitComponent(self.window, next_pit_coordinates, i + 1))
        self.pits.append(self.right_pot)
        j = 8
        for i in range(5, -1, -1):
            next_pit_coordinates = (first_pit_coordinates[0] + self.SPACE_BETWEEN_PITS * i,
                                    first_pit_coordinates[1] + self.HEIGHT_BETWEEN_PITS)
            self.pits.append(PitComponent(self.window, next_pit_coordinates, j))
            j += 1

    def set_highlighted_pits(self, player_turn):
        """
        Sets the highlighted pits for the current player.
        And deletes the highlighted pits for the other player.


        :param: player_turn (int): The current player's turn.

        Returns:
            None
        """
        if player_turn == 1:
            for i in range(1, 7):
                if len(self.pits[i].stones) != 0:
                    self.pits[i].highlight()
                else:
                    self.pits[i].delete_highlight()
            for i in range(8, 14):
                self.pits[i].delete_highlight()
        else:
            for i in range(8, 14):
                if len(self.pits[i].stones) != 0:
                    self.pits[i].highlight()
                else:
                    self.pits[i].delete_highlight()
            for i in range(1, 7):
                self.pits[i].delete_highlight()

    def draw(self):
        """Draws the pits and the pots."""
        for pit in self.pits:
            pit._draw()

    def treat_hovering(self, mouse_position, player_turn):
        """
        Treats the hovering of the mouse on the pits.
        If the mouse is hovering on a pit,
        the pit is highlighted.
        Else, the pit is not highlighted.

        :param mouse_position:
        :param player_turn:
        :return:    the index of the pit that is hovered
                    or None if no pit is hovered
        """
        to_return = None
        if player_turn == 1:
            for i in range(1, 7):
                if self.pits[i].is_mouse_hovering(mouse_position):
                    self.pits[i].treat_hovering()
                    to_return = i
        else:
            for i in range(8, 14):
                if self.pits[i].is_mouse_hovering(mouse_position):
                    self.pits[i].treat_hovering()
                    to_return = i
        return to_return

    def move_stones(self, pit_index, player_turn):
        """
        Moves the stones from the pit with the given index
        to the next pits.

        :param pit_index:
        :param player_turn:
        :return: a list with all pits where the stones were moved
        """
        self.moving_stones = True
        destination_list = list()
        number_of_stones = len(self.pits[pit_index].stones)
        for i in range(number_of_stones):
            stone = self.pits[pit_index].stones.pop()
            destination = self.__get_destination(pit_index, i, player_turn)
            destination_list.append(destination)
            if destination == 0 or destination == 7:
                is_in_pot = True
                if destination == 0:
                    coordinates = self.left_pot.stones_coordinates
                else:
                    coordinates = self.right_pot.stones_coordinates
            else:
                is_in_pot = False
                coordinates = self.pits[destination].pit_coordinates
            stone.move_animate(coordinates, is_in_pot)
            self.pits[destination].add_stone(stone)
        self.moving_stones = False
        return destination_list

    @staticmethod
    def __get_destination(pit_index, i, player_turn):
        """
        Calculates the destination of a stone from a pit
        according to the player's turn
        and the number of the current stone that is being moved (i-th).
        """
        destination = pit_index - i - 1
        if destination < 0:
            destination += 14

        if player_turn == 1:
            if destination == 7:
                destination = 8
        else:
            if destination == 0:
                destination = 13

        return destination

    @staticmethod
    def is_last_destination_player_pot(destination, player_turn):
        """
        A query that checks if the last destination
        is a player's pot or not (a pit).

        :param destination: the last index from the list of destinations
        :param player_turn: current player's turn
        :return:    True if the last destination is a player's pot,
                    False otherwise.
        """
        return (destination == 0 and player_turn == 1
                or destination == 7 and player_turn == 2)

    @staticmethod
    def is_last_destination_player_pit(destination, player_turn):
        """
        A query that checks if the last destination
        is a player's pit or not (a pot).

        :param destination: the last index from the list of destinations
        :param player_turn:  current player's turn
        :return:    True if the last destination is a player's pit,
                    False otherwise.
        """
        if player_turn == 1:
            return destination in range(1, 7)
        else:
            return destination in range(8, 14)

    def move_all_to_player_pot(self, pit_index, player_turn):
        """
        Moves all the stones from the pit with the given index
        to the player's pot.
        :param pit_index: the index of the pit from the list of this class
        :param player_turn: the current player's turn
        :return: None
        """
        self.moving_stones = True
        number_of_stones = len(self.pits[pit_index].stones)
        if player_turn == 1:
            pot = self.left_pot
        else:
            pot = self.right_pot

        for i in range(number_of_stones):
            stone = self.pits[pit_index].stones.pop()
            stone.move_animate(pot.stones_coordinates, True)
            pot.add_stone(stone)
        self.moving_stones = False

    def was_pit_empty(self, last_destination):
        """
        A query that checks if the last destination
        was an empty pit or not.
        :param last_destination: the last index from the list of destinations
        :return:    True if the last destination was an empty pit,
                    False otherwise.
        """
        return len(self.pits[last_destination].stones) == 1

    def is_game_over(self):
        """
        A query that checks if the game is over or not.
        :return:    1 if player 1 won,
                    2 if player 2 won,
                    False if the game is not over.
        """
        answer = None
        for i in range(1, 7):
            if len(self.pits[i].stones) != 0:
                answer = False

        if answer is None:
            return 1

        for i in range(8, 14):
            if len(self.pits[i].stones) != 0:
                return False
        return 2
