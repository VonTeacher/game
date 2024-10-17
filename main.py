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
from random import randint, randrange

STEP_SIZE = 5
SPRITE_SIZE = 40

WIDTH_UNITS = 16
HEIGHT_UNITS = 10

SCREEN_WIDTH = WIDTH_UNITS * SPRITE_SIZE
SCREEN_HEIGHT = HEIGHT_UNITS * SPRITE_SIZE

MAX_BLOCK_COUNT = 20

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
        self.surface.fill((0, 255, 0))
        self.rect = self.surface.get_rect(left = 0, top = 0)

    def update(self, keys):
        if keys[K_UP]:    playerRect.move_ip(0, -STEP_SIZE)
        if keys[K_DOWN]:  playerRect.move_ip(0, STEP_SIZE)
        if keys[K_LEFT]:  playerRect.move_ip(-STEP_SIZE, 0)
        if keys[K_RIGHT]: playerRect.move_ip(STEP_SIZE, 0)

        # Keep player on screen
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.surface = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
        self.surface.fill((255, 0, 0))
        self.rect = self.surface.get_rect(
            left = randrange(WIDTH_UNITS) * SPRITE_SIZE,
            top = randrange(HEIGHT_UNITS) * SPRITE_SIZE)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock  = pygame.time.Clock()

player = Player()
playerRect = player.rect

blocks = pygame.sprite.Group()
while len(blocks) < MAX_BLOCK_COUNT:
    block = Block()
    if any(
        [
            (block.rect.top == existing.rect.top and block.rect.left == existing.rect.left) or \
            (block.rect.top == 0 and block.rect.left == 0) \
            for existing in blocks
        ]
    ): continue
    else: blocks.add(block)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(blocks)

running = True

while running:
    px = playerRect.left
    px1 = playerRect.right
    py = playerRect.top
    py1 = playerRect.bottom

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q: running = False # Presse ESCAPE key
        if event.type == QUIT: running = False # Click X on the window

    keys = pygame.key.get_pressed()

    player.update(keys)

    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surface, entity.rect)

    if pygame.sprite.spritecollideany(player, blocks):
        player.kill()
        running = False

    pygame.display.flip()

    clock.tick(60) # Multiplies 1/60 * 1000 to determine the delay timer (16.667ms)

pygame.quit()
