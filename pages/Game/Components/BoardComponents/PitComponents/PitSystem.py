from pages.Game.Components.BoardComponents.PitComponents.PitComponent import PitComponent


class PitSystem:
    space_between_pits = 116.5
    height_between_rows = 261

    def __init__(self, window, board_coordinates):
        self.window = window
        self.pits = list()
        self.__generate_pits(board_coordinates)

    def __generate_pits(self, board_coordinates):

        first_pit_coordinates = (board_coordinates[0] + 57, board_coordinates[1] + 47)

        self.pits.append(PitComponent(self.window, first_pit_coordinates, 0))
        for i in range(1, 6):
            next_pit_coordinates = (first_pit_coordinates[0] + self.space_between_pits * i,
                                    first_pit_coordinates[1])
            self.pits.append(PitComponent(self.window, next_pit_coordinates, i))

        j = 6
        for i in range(5, -1, -1):
            next_pit_coordinates = (first_pit_coordinates[0] + self.space_between_pits * i,
                                    first_pit_coordinates[1] + self.height_between_rows)
            self.pits.append(PitComponent(self.window, next_pit_coordinates, j))
            j += 1

    def set_highlighted_pits(self, player_turn):
        if player_turn == 1:
            for i in range(6):
                if len(self.pits[i].stones) != 0:
                    self.pits[i].highlight()
                else:
                    self.pits[i].delete_highlight()
            for i in range(6, 12):
                self.pits[i].delete_highlight()
        else:
            for i in range(6, 12):
                if len(self.pits[i].stones) != 0:
                    self.pits[i].highlight()
                else:
                    self.pits[i].delete_highlight()
            for i in range(6):
                self.pits[i].delete_highlight()

    def draw(self):
        for pit in self.pits:
            pit._draw()

    def treat_hovering(self, mouse_position, player_turn):
        to_return = None
        if player_turn == 1:
            for i in range(6):
                if self.pits[i].is_mouse_hovering(mouse_position):
                    self.pits[i].treat_hovering()
                    to_return = i
        else:
            for i in range(6, 12):
                if self.pits[i].is_mouse_hovering(mouse_position):
                    self.pits[i].treat_hovering()
                    to_return = i
        return to_return

    def move_stones(self, pit_index, left_pot, right_pot, player_turn):
        number_of_stones = len(self.pits[pit_index].stones)
        destination_list = list()
        if player_turn == 1:
            j = 0
            for i in range(number_of_stones):
                stone = self.pits[pit_index].stones.pop()
                destination = (pit_index - i - 1) + j
                if destination < 0:
                    stone.move_animate(left_pot.stones_coordinates, True)
                    left_pot.add_stone(stone)
                    j += 13
                    destination_list.append('left_pot')
                else:
                    stone.move_animate(self.pits[destination].pit_coordinates)
                    self.pits[destination].add_stone(stone)
                    destination_list.append(destination)
        else:
            j = 0
            ok = True
            reset = 0
            for i in range(number_of_stones):
                stone = self.pits[pit_index].stones.pop()
                destination = (pit_index - i - 1) + j + reset
                if destination == 5 and ok is True:
                    stone.move_animate(right_pot.stones_coordinates, True)
                    right_pot.add_stone(stone)
                    j += 1
                    destination_list.append('right_pot')
                    ok = False
                else:
                    if destination == 5:
                        ok = True
                    stone.move_animate(self.pits[destination].pit_coordinates)
                    self.pits[destination].add_stone(stone)
                    destination_list.append(destination)
                    if destination == 0:
                        ok = True
                        reset += 12

        print(destination_list)
