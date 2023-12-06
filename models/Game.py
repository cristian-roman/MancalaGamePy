import os.path
import sys
import time

import pygame

from AppSettings import AppSettings
from models.ViewModel import ViewModel
from ViewTree import ViewTree


class Game(ViewModel):
    game_images_path = os.path.join('images', 'Game')

    table_width = 800
    table_height = 500

    pit_width = 400
    pit_height = 400

    def __init__(self, window: pygame.Surface):
        self.window = window

        self.bg_image_path = os.path.join(self.game_images_path, 'background.png')
        self.bg_image = pygame.image.load(self.bg_image_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.window.get_width(), self.window.get_height()))

        self.board_path = os.path.join(self.game_images_path, 'board.png')
        self.board = pygame.image.load(self.board_path)
        self.board = pygame.transform.scale(self.board, (self.table_width, self.table_height))

        self.player_pot = os.path.join(self.game_images_path, 'player_pot.png')
        self.player_pot = pygame.image.load(self.player_pot)
        self.player_pot = pygame.transform.scale(self.player_pot, (self.pit_width, self.pit_height))

    def _animate_scaling(self, text, text_rect):
        clock = pygame.time.Clock()
        frame_rate = 15  # Adjust the frame rate as needed
        delta_time = 1.0 / frame_rate

        for i in range(10):
            scale_factor = 1.0 + i * 0.01
            scaled_text = pygame.transform.scale(text,
                                                 (int(text_rect.width * scale_factor),
                                                  int(text_rect.height * scale_factor)))
            scaled_rect = scaled_text.get_rect(center=text_rect.center)

            background_rect = pygame.Rect(scaled_rect.x - 10, scaled_rect.y - 5,
                                          scaled_rect.width + 20, scaled_rect.height + 10)

            pygame.draw.rect(self.window, AppSettings.colors['orange_h2'], background_rect)
            self.window.blit(scaled_text, scaled_rect)
            pygame.display.update()

            clock.tick(frame_rate)
            time.sleep(delta_time)

        for i in range(10):
            scale_factor = 1.1 - i * 0.01
            scaled_text = pygame.transform.scale(text,
                                                 (int(text_rect.width * scale_factor),
                                                  int(text_rect.height * scale_factor)))
            scaled_rect = scaled_text.get_rect(center=text_rect.center)

            background_rect = pygame.Rect(scaled_rect.x - 10, scaled_rect.y - 5,
                                          scaled_rect.width + 20, scaled_rect.height + 10)

            pygame.draw.rect(self.window, AppSettings.colors['orange_h2'], background_rect)
            self.window.blit(scaled_text, scaled_rect)
            pygame.display.update()

            clock.tick(frame_rate)
            time.sleep(delta_time)

    def _draw_player_turn_label(self, player_turn):
        text = AppSettings.font.render(f"Player {player_turn} turn", True, AppSettings.colors['white'])
        text_rect = text.get_rect(
            center=(self.window.get_width() // 2, (self.window.get_height() // 2 - self.table_height // 2) // 2))

        rect_width = text_rect.width + 20
        rect_height = text_rect.height + 10
        rect_x = text_rect.centerx - rect_width // 2
        rect_y = text_rect.centery - rect_height // 2
        background_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(self.window, AppSettings.colors['orange_h2'], background_rect)

        # Call the animation function
        self._animate_scaling(text, text_rect)

        # Display the original text
        pygame.draw.rect(self.window, AppSettings.colors['orange_h2'], background_rect)
        self.window.blit(text, text_rect)
        pygame.display.update()

    def _load_view(self):
        self.window.blit(self.bg_image, (0, 0))

        board_x = self.window.get_width() // 2 - self.table_width // 2 + 10
        board_y = self.window.get_height() // 2 - self.table_height // 2
        self.window.blit(self.board, (board_x, board_y))

        left_pot_x = self.window.get_width() // 2 - self.table_width // 2 - self.pit_width + 95
        left_pot_y = self.window.get_height() // 2 - self.table_height // 2 + 40
        self.window.blit(self.player_pot, (left_pot_x, left_pot_y))

        right_pot_x = self.window.get_width() // 2 + self.table_width // 2 - 75
        right_pot_y = self.window.get_height() // 2 - self.table_height // 2 + 40
        self.window.blit(self.player_pot, (right_pot_x, right_pot_y))

        oval_rect = pygame.Rect(board_x + 57, board_y + 47, 102, 155)
        pygame.draw.ellipse(self.window, AppSettings.colors['orange_h4'], oval_rect, 4)

        self._draw_player_turn_label(1)

        pygame.display.update()

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def loop(self):
        self._listen_for_events()
        self._load_view()
        pygame.display.update()
