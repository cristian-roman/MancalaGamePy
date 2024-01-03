from pages.Game.Components.BoardComponents.PitComponents.PitComponent import PitComponent


class PitSystem:
    space_between_pits = 116.5
    height_between_rows = 261

    def __init__(self, window, board_coordinates, left_pot, right_pot):
        self.window = window
        self.pits = list()
        self.left_pot = left_pot
        self.right_pot = right_pot
        self.pits.append(left_pot)
        self.__generate_pits(board_coordinates)
        self.moving_stones = False

    def __generate_pits(self, board_coordinates):

        first_pit_coordinates = (board_coordinates[0] + 57, board_coordinates[1] + 47)

        self.pits.append(PitComponent(self.window, first_pit_coordinates, 1))
        for i in range(1, 6):
            next_pit_coordinates = (first_pit_coordinates[0] + self.space_between_pits * i,
                                    first_pit_coordinates[1])
            self.pits.append(PitComponent(self.window, next_pit_coordinates, i + 1))
        self.pits.append(self.right_pot)
        j = 8
        for i in range(5, -1, -1):
            next_pit_coordinates = (first_pit_coordinates[0] + self.space_between_pits * i,
                                    first_pit_coordinates[1] + self.height_between_rows)
            self.pits.append(PitComponent(self.window, next_pit_coordinates, j))
            j += 1

    def set_highlighted_pits(self, player_turn):
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
        for pit in self.pits:
            pit._draw()

    def treat_hovering(self, mouse_position, player_turn):
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
        return (destination == 0 and player_turn == 1
                or destination == 7 and player_turn == 2)

    @staticmethod
    def is_last_destination_player_pit(destination, player_turn):
        if player_turn == 1:
            return destination in range(1, 7)
        else:
            return destination in range(8, 14)

    def move_all_to_player_pot(self, pit_index, player_turn):
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
        return len(self.pits[last_destination].stones) == 1

    def is_game_over(self):
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
