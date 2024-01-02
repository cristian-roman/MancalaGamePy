from pages.Game.Components.GameComponent import GameComponent
from pages.Game.Components.PitComponent.PitComponent import PitComponent


class PitSystem(GameComponent):
    space_between_pits = 116.5
    height_between_rows = 261

    def __init__(self, window, first_pit_coordinates):
        self.window = window
        first_pit_coordinates = first_pit_coordinates

        self.pits = list()
        self.__generate_pits(first_pit_coordinates)

    def __generate_pits(self, first_pit_coordinates):

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

    def _draw(self):
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
                    print(to_return)
        return to_return

    def move_stones(self, pit_index, left_pot, right_pot, player_turn):
        stones_to_move = self.pits[pit_index].stones
