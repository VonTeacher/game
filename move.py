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

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
STEP_SIZE = 20

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((STEP_SIZE, STEP_SIZE))
        # self.surface.fill((100, 255, 0))
        self.rect = self.surface.get_rect()

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -STEP_SIZE)
            if self.rect.y < 0: self.rect.y = 0
        if keys[K_DOWN]:
            self.rect.move_ip(0, STEP_SIZE)
            if self.rect.y > SCREEN_HEIGHT - STEP_SIZE: self.rect.y = SCREEN_HEIGHT - STEP_SIZE
        if keys[K_LEFT]:
            self.rect.move_ip(-STEP_SIZE, 0)
            if self.rect.x <= 0: self.rect.x = 0
        if keys[K_RIGHT]:
            self.rect.move_ip(STEP_SIZE, 0)
            if self.rect.x > SCREEN_WIDTH - STEP_SIZE: self.rect.x = SCREEN_WIDTH - STEP_SIZE

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False

        keys = pygame.key.get_pressed()

    player.update(keys)
    screen.fill((0, 0, 0))
    player.draw(screen)

    pygame.display.flip()    

    clock.tick(16)

pygame.quit()
