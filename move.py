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

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.locals.KEYDOWN:
            match event.key:
                case pygame.locals.K_UP:
                    player.rect.move_ip(0, -STEP_SIZE)
                    if player.rect.y <= 0:
                        player.rect.y = 0
                case pygame.locals.K_DOWN:
                    player.rect.move_ip(0, STEP_SIZE)
                    if player.rect.y >= SCREEN_HEIGHT:
                        player.rect.y = SCREEN_HEIGHT - STEP_SIZE
                case pygame.locals.K_LEFT:
                    player.rect.move_ip(-STEP_SIZE, 0)
                    if player.rect.x <= 0:
                        player.rect.x = 0
                case pygame.locals.K_RIGHT:
                    player.rect.move_ip(STEP_SIZE, 0)
                    if player.rect.x >= SCREEN_WIDTH:
                        player.rect.x = SCREEN_WIDTH - STEP_SIZE
                case pygame.locals.K_ESCAPE: running = False
        elif event.type == pygame.locals.QUIT:
            running = False

    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()    
