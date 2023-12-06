import sys

import pygame


class ViewModel:

    def loop(self):
        pass

    def _load_view(self):
        pass

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
