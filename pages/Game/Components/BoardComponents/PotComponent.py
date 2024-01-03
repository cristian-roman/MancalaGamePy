import os

import pygame

from pages.Game.Components.GameComponent import GameComponent
from AppSettings import AppSettings
import pages.Game.Components.LabelComponent as Label


class PotComponent(GameComponent):
    pot_width = 400
    pot_height = 400
    pot_file_name = 'player_pot.png'

    def __init__(self, window, pot_coordinates, images_path):
        self.window = window
        self.pot_coordinates = pot_coordinates
        self.stones = list()

        self.score_label_x = self.pot_coordinates[0] + self.pot_width // 2
        if pot_coordinates[1] < self.window.get_height() // 2:
            self.score_label_y = self.pot_coordinates[1] + self.pot_height - 70
            self.score_label_text = "Player 1 Score: "
            self.color = AppSettings.colors['orange_h2']
        else:
            self.score_label_y = self.pot_coordinates[1] + 45
            self.score_label_text = "Player 2 Score: "
            self.color = AppSettings.colors['orange_h6']

        self.score_label = Label.LabelComponent(self.window,
                                                (self.score_label_x, self.score_label_y),
                                                self.score_label_text, 36,
                                                AppSettings.colors['white'],
                                                True,
                                                self.color)

        self.pot = pygame.image.load(os.path.join(images_path, self.pot_file_name))
        self.pot = pygame.transform.scale(self.pot, (self.pot_width, self.pot_height))

        self.stones_coordinates = (self.pot_coordinates[0] + 150, self.pot_coordinates[1] + 150)

    def _draw(self):
        self.window.blit(self.pot, self.pot_coordinates)
        for stone in self.stones:
            stone._draw()

        self.score_label.set_text(self.score_label_text + str(len(self.stones)))
        self.score_label._draw()

    def add_stone(self, stone):
        self.stones.append(stone)

    def get_score(self):
        return len(self.stones)
