import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
from random import randint

from player import Player

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# Should these be absolute globals?
# Would there ever be a case where we don't want to share these dimensions with the game?
# How to use that global information?

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: # Presse ESCAPE key
                running = False
        if event.type == QUIT: # Click X on the window
            running = False

        keys = pygame.key.get_pressed()

    player.update(keys)
    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.flip()    

    clock.tick(60) # Multiplies 1/60 * 1000 to determine the delay timer (16.667ms)

pygame.quit()
