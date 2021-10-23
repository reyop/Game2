import pygame
from Game.Entity.player import Player

run = True
SCREEN_SIZE = 1280, 720
screen = pygame.display.set_mode(SCREEN_SIZE)
p = Player(0, 0, 30, 60)

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = not run

    pygame.display.update()
