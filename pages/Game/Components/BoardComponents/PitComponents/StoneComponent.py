import os
import random
import pygame
import ViewTree
from pages.Game.Components.GameComponent import GameComponent


class StoneComponent(GameComponent):
    """
    A class that represents a stone.

    Class-level attributes:
        stone_images_path (str): The path of the images of the stones.
        offsets (dict): The offsets of the stones.
        sizes (dict): The sizes of the stones.

    Attributes:
        stone_index (int):  The index of the stone
                            from stones in image path.
        window (pygame.Surface): The pygame window.
        stone (pygame.Surface): The image of the stone.
        stone_coordinates (tuple): The coordinates of the stone.
    """
    stone_images_path = os.path.join('images', 'Game', 'Stones')

    offsets = {
        1: (-30, -25),
        2: (-4, 42),
        3: (-28, 1),
        4: (-40, -45),
        5: (-39, 2),
    }

    sizes = {
        1: (150, 150),
        2: (75, 75),
        3: (100, 100),
        4: (150, 150),
        5: (150, 150),
    }

    def __init__(self, window, pit_coordinates, stone_index):
        """
        The constructor initializing the attributes of the class.
        :param window: the pygame window
        :param pit_coordinates:     the coordinates of the pit
                                    that contains the stone
        :param stone_index:     the index of the stone
                                in the stones list from images
        """
        super().__init__()
        self.stone_index = stone_index
        self.window = window

        self.stone = pygame.image.load(os.path.join(self.stone_images_path, f'stone_{stone_index}.png'))
        self.stone = pygame.transform.scale(self.stone, self.sizes[stone_index])
        self.stone = pygame.transform.rotate(self.stone, random.randint(0, 360))

        self.stone_coordinates = (pit_coordinates[0] + self.offsets[stone_index][0] + random.randint(-1, 1),
                                  pit_coordinates[1] + self.offsets[stone_index][1] + random.randint(-1, 1))

    def move_animate(self, new_coordinates, is_in_pot=False):
        """
        Moves the stone to the new coordinates. It animates the movement.
        :param new_coordinates: new pit coordinates
        :param is_in_pot: False default, True if the new coordinates point to a pot
        :return: None
        """
        if is_in_pot:
            a = -5
            b = 5
        else:
            a = -1
            b = 1

        new_stone_coordinates = (new_coordinates[0] + self.offsets[self.stone_index][0] + random.randint(a, b),
                                 new_coordinates[1] + self.offsets[self.stone_index][1] + random.randint(a, b))
        speed = 10
        if new_stone_coordinates[0] < self.stone_coordinates[0]:
            multiplier_x = -1
        else:
            multiplier_x = 1

        if new_stone_coordinates[1] < self.stone_coordinates[1]:
            multiplier_y = -1
        else:
            multiplier_y = 1

        step_x = abs(new_stone_coordinates[0] - self.stone_coordinates[0]) / speed
        step_y = abs(new_stone_coordinates[1] - self.stone_coordinates[1]) / speed

        for i in range(1, speed):

            self.stone_coordinates = (self.stone_coordinates[0] + step_x * multiplier_x,
                                      self.stone_coordinates[1] + step_y * multiplier_y)
            ViewTree.ViewTree.get_current_view()._load_view()
            self._draw()
            pygame.display.update()
            pygame.time.delay(100)

        self.stone_coordinates = new_stone_coordinates

    def _draw(self):
        """Draw the stone on the window"""
        self.window.blit(self.stone, self.stone_coordinates)
