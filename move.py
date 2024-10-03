import pygame
import pygame.locals

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
STEP_SIZE = 20

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surface = pygame.Surface((STEP_SIZE, STEP_SIZE))
        self.rect = self.surface.get_rect()

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)

    def update(self, keys):
        if keys[pygame.locals.K_UP]:
            self.rect.y -= STEP_SIZE
            if self.rect.y < 0: self.rect.y = 0
        if keys[pygame.locals.K_DOWN]:
            self.rect.y += STEP_SIZE
            if self.rect.y > SCREEN_HEIGHT - STEP_SIZE: self.rect.y = SCREEN_HEIGHT - STEP_SIZE
        if keys[pygame.locals.K_LEFT]:
            self.rect.x -= STEP_SIZE
            if self.rect.x <= 0: self.rect.x = 0
        if keys[pygame.locals.K_RIGHT]:
            self.rect.x += STEP_SIZE
            if self.rect.x > SCREEN_WIDTH - STEP_SIZE: self.rect.x = SCREEN_WIDTH - STEP_SIZE

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.locals.K_ESCAPE:
                running = False
        if event.type == pygame.locals.QUIT:
            running = False

        keys = pygame.key.get_pressed()

    player.update(keys)
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()    
    clock.tick(16)

pygame.quit()
