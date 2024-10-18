import pygame
from pygame.locals import (
    K_ESCAPE,
    K_q,
    K_e,
    K_s,
    K_d,
    K_f,
    KEYDOWN,
    QUIT,
    RLEACCEL
)
from math import sqrt
from random import randrange

SPRITE_SIZE = 40
WIDTH_UNITS = 16
HEIGHT_UNITS = 10
SCREEN_WIDTH = WIDTH_UNITS * SPRITE_SIZE
SCREEN_HEIGHT = HEIGHT_UNITS * SPRITE_SIZE
MAX_BLOCK_COUNT = 20

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.image.load("rock.png").convert()
        self.surface.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surface.get_rect(left = 0, top = 0)
        self.vel = 3

    def update(self, keys):
        dv = pygame.math.Vector2(0, 0)

        if keys[K_e]: dv.y = -self.vel
        if keys[K_d]: dv.y =  self.vel
        if keys[K_s]: dv.x = -self.vel
        if keys[K_f]: dv.x =  self.vel

        if (dv.x and dv.y):
            self.rect.move_ip(dv.x / sqrt(2), dv.y/sqrt(2))
        else:
            self.rect.move_ip(dv.x, dv.y)

        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT: self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH: self.rect.right = SCREEN_WIDTH

class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.surface = pygame.image.load("block.png")
        self.surface.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surface.get_rect(
            left = randrange(WIDTH_UNITS) * SPRITE_SIZE,
            top = randrange(HEIGHT_UNITS) * SPRITE_SIZE)

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()
        self.surface = pygame.image.load("bg_640_400.png").convert()
        self.rect = self.surface.get_rect()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock  = pygame.time.Clock()

player = Player()
background = Background()
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
all_sprites.add(background)
all_sprites.add(blocks)
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE or event.key == K_q: running = False # Presse ESCAPE key
        if event.type == QUIT: running = False # Click X on the window

    keys = pygame.key.get_pressed()

    player.update(keys)

    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surface, entity.rect)

    # if pygame.sprite.spritecollideany(player, blocks):
    #     print(f"Player {player.rect.center} collided with block.")

    # Removes a block when a player collides with it
    # pygame.sprite.spritecollide(player, blocks, True)

    for block in blocks:
        if pygame.sprite.collide_rect(player, block):
            block.surface.fill((0, 0, 255))

    pygame.display.flip()

    clock.tick(60) # Multiplies 1/60 * 1000 to determine the delay timer (16.667ms)

pygame.quit()
