from pages.Game.Components.GameComponent import GameComponent
from pages.Game.Components.PitComponent.PitComponent import PitComponent
from multiprocessing import Pool



class PitSystem(GameComponent):
    space_between_pits = 116.5
    height_between_rows = 261

    def __init__(self, window, first_pit_coordinates):
        self.highlighted_pits = None
        self.no_highlighted_pits = None

        self.window = window
        first_pit_coordinates = first_pit_coordinates

        self.pits = list()
        self.__generate_pits(first_pit_coordinates)

    def __generate_pits(self, first_pit_coordinates):

        self.pits.append(PitComponent(self.window, first_pit_coordinates))
        for i in range(1, 6):
            next_pit_coordinates = (first_pit_coordinates[0] + self.space_between_pits * i,
                                    first_pit_coordinates[1])
            self.pits.append(PitComponent(self.window, next_pit_coordinates))
        for i in range(6):
            next_pit_coordinates = (first_pit_coordinates[0] + self.space_between_pits * i,
                                    first_pit_coordinates[1] + self.height_between_rows)
            self.pits.append(PitComponent(self.window, next_pit_coordinates))

    def set_highlighted_pits(self, player_turn):
        self.highlighted_pits = list()
        self.no_highlighted_pits = list()
        if player_turn == 1:
            for i in range(6):
                if len(self.pits[i].stones) != 0:
                    self.highlighted_pits.append(i)
                else:
                    self.no_highlighted_pits.append(i)
            for i in range(6, 12):
                self.no_highlighted_pits.append(i)
        else:
            for i in range(6, 12):
                if len(self.pits[i].stones) != 0:
                    self.highlighted_pits.append(i)
                else:
                    self.no_highlighted_pits.append(i)
            for i in range(6):
                self.no_highlighted_pits.append(i)

    def _draw(self):
        if self.highlighted_pits is not None:
            for pit_index in self.highlighted_pits:
                self.pits[pit_index]._draw()
                self.pits[pit_index].highlight()
        if self.no_highlighted_pits is not None:
            for pit_index in self.no_highlighted_pits:
                self.pits[pit_index]._draw()
                self.pits[pit_index].delete_highlight()

