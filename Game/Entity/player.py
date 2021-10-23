import pygame
from .entity import Entity


class Player(Entity):
    MOVEMENT_SPEED = 3

    def __init__(self, x, y, w, h):
        super(Player, self).__init__(x, y, w, h)
        self.moving_right = False
        self.moving_left = False

    def move_x(self):
        if self.moving_left:
            self.movement[0] -= self.MOVEMENT_SPEED

        if self.moving_right:
            self.movement[0] += self.MOVEMENT_SPEED

    def draw(self):
        pass
