import sys

import pygame


class ViewModel:

    def _loop(self):
        raise NotImplementedError

    def _load_view(self):
        raise NotImplementedError

    def _listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
