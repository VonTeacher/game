import pygame

from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT
)

SPRITE_SIZE = 20
STEP_SIZE = 5

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super(Player, self).__init__()
        self.surface = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
        self.rect = self.surface.get_rect()
        self.size = SPRITE_SIZE
        self.step = STEP_SIZE
        self.red = 255
        self.green = 255
        self.blue = 255
        # how to get this out of player?
        self.screen_width = screen_width
        self.screen_height = screen_height
        # how to get this out of player?

    def draw(self, surface):
        pygame.draw.rect(surface, (self.red, self.green, self.blue), self.rect)

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -self.step)
            if self.rect.y < 0: self.rect.y = 0
        if keys[K_DOWN]:
            self.rect.move_ip(0, self.step)
            if self.rect.y > self.screen_height - self.size: self.rect.y = self.screen_height - self.size
        if keys[K_LEFT]:
            self.rect.move_ip(-self.step, 0)
            if self.rect.x <= 0: self.rect.x = 0
        if keys[K_RIGHT]:
            self.rect.move_ip(self.step, 0)
            if self.rect.x > self.screen_width - self.size: self.rect.x = self.screen_width - self.size

# Should the player know about the screen width and height?
# Is this not an unfortunate and tight coupling?
