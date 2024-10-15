import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_q,
    KEYDOWN,
    QUIT,
)
from random import randrange

STEP_SIZE = 5
SPRITE_SIZE = 20

WIDTH_UNITS = 16
HEIGHT_UNITS = 10

SCREEN_WIDTH = WIDTH_UNITS * SPRITE_SIZE
SCREEN_HEIGHT = HEIGHT_UNITS * SPRITE_SIZE

MAX_BLOCK_COUNT = 10

SCORE = 0

pygame.init()
pygame.font.init()

clock  = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect(0, 0, SPRITE_SIZE, SPRITE_SIZE)
blocks = []
font   = pygame.font.SysFont("Comic Sans", 12)

while len(blocks) < MAX_BLOCK_COUNT:
    block = pygame.Rect(
        randrange(WIDTH_UNITS) * SPRITE_SIZE,
        randrange(HEIGHT_UNITS) * SPRITE_SIZE,
        SPRITE_SIZE,
        SPRITE_SIZE
    )
    if any([(block.top == existing.top and block.left == existing.left) or (block.top == 0 and block.left == 0) for existing in blocks]): continue
    else: blocks.append(block)

running = True

while running:
    px = player.left
    px1 = player.left + SPRITE_SIZE
    py = player.top
    py1 = player.top + SPRITE_SIZE

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q: running = False # Presse ESCAPE key
        if event.type == QUIT: running = False # Click X on the window

        keys = pygame.key.get_pressed()

    if keys[K_UP]:    player.top -= STEP_SIZE
    if keys[K_DOWN]:  player.top += STEP_SIZE
    if keys[K_LEFT]:  player.left -= STEP_SIZE
    if keys[K_RIGHT]: player.left += STEP_SIZE

    for b in blocks:
        bx  = b.left
        bx1 = b.left + SPRITE_SIZE
        by  = b.top
        by1 = b.top + SPRITE_SIZE

        # pygame/src_c/rect.c
        # https://github.com/pygame/pygame/blob/79807da84c9bacf8df5a177763e14c924e3b15e2/src_c/rect.c#L356
        if player.colliderect(b):
            STEP_SIZE = 0
            if (px < bx1 and px1 > bx) and py == by1: player.top = by1
            if (px < bx1 and px1 > bx) and py1 == by: player.top = by - SPRITE_SIZE
            if (py < by1 and py1 > by) and px == bx1: player.left = bx1
            if (py < by1 and py1 > by) and px1 == bx: player.left = bx - SPRITE_SIZE
            blocks.remove(b)
            SCORE += 1
            # Once the last block was removed, I was unable to move the player. Why is it happening?
        else: STEP_SIZE = 5

        # BUG: if we hit the corners just perfectly so, the collision detection fails and
        # the player block goes through a red block

    # Keep player on screen
    if player.top < 0: player.top = 0
    if player.top > SCREEN_HEIGHT - SPRITE_SIZE: player.top = SCREEN_HEIGHT - SPRITE_SIZE
    if player.left < 0: player.left = 0
    if player.left > SCREEN_WIDTH - SPRITE_SIZE: player.left = SCREEN_WIDTH - SPRITE_SIZE

    screen.fill((0, 0, 0))

    text = font.render(f"{SCORE}", 1, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - SPRITE_SIZE, SCREEN_HEIGHT - SPRITE_SIZE))

    pygame.draw.rect(screen, (0, 255, 0), player)
    for b in blocks: pygame.draw.rect(screen, (255, 0, 0), b)

    pygame.display.flip()

    clock.tick(60) # Multiplies 1/60 * 1000 to determine the delay timer (16.667ms)

pygame.quit()
