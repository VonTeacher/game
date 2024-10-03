import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

pygame.init()

SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

### Game Loop
# 1 Process user input
# 2 Updated the state of all game objects
# 3 Update the display and audio output
# 4 Maintain the speed of the game

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill((255,255,255))
    surface = pygame.Surface((50, 50))
    surface.fill((0,0,0))
    rect = surface.get_rect()
    surface_center = (
        (SCREEN_WIDTH - surface.get_width()) / 2,
        (SCREEN_HEIGHT - surface.get_height()) / 2
    )
    screen.blit(surface, surface_center)
    pygame.display.flip()
