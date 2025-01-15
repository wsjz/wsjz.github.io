
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tank properties
TANK_WIDTH = 40
TANK_HEIGHT = 20
TANK_SPEED = 5

# Bullet properties
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_SPEED = 7

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tank Battle")

# Tank class
class Tank(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([TANK_WIDTH, TANK_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = TANK_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface([BULLET_WIDTH, BULLET_HEIGHT])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = BULLET_SPEED

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# Initialize tanks and bullets
player_tank = Tank(GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT - TANK_HEIGHT - 10)
enemy_tank = Tank(RED, SCREEN_WIDTH // 2, 10)
all_sprites = pygame.sprite.Group()
all_sprites.add(player_tank)
all_sprites.add(enemy_tank)
bullets = pygame.sprite.Group()

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(WHITE, player_tank.rect.centerx, player_tank.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    # Update sprites
    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollide(enemy_tank, bullets, True):
        print("Enemy tank hit!")

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
