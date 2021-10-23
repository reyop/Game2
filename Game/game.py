import pygame


class Game(object):
    DISPLAY_SIZE = 640, 320

    def __init__(self, screen):
        self.display = pygame.Surface(self.DISPLAY_SIZE)
        self.screen = screen


