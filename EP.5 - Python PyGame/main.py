import pygame
from pygame.locals import *
import random

# Start Pygame project
pygame.init()

# Set width, height
WIDTH = 1250
HEIGHT = 700

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

# Score
SCORE = 0

# Lives
LIVES = 3

# Frame per second(FPS)
FPS = 60

# Game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game name
pygame.display.set_caption("Phenomenal Game")

# background

bgImage = "C:\\Users\\Hery\\Desktop\\My Projects\\Python-PyGame\\EP.5 - Python PyGame\\background.png"
background = pygame.image.load(bgImage).convert_alpha()
background_rect = background.get_rect()

# Create  clock of a game
clock = pygame.time.Clock()

# Game status
running = True  # True = YES, False = NO


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """ Main function alway run, when we are call """
        pygame.sprite.Sprite.__init__(self)

        img = "C:\\Users\\Hery\\Desktop\\My Projects\\Python-PyGame\\EP.4 - Python PyGame\\First Game\\bomber.png"
        self.image = pygame.image.load(img).convert_alpha()

        # self.image = pygame.Surface((50, 50))
        # self.image.fill(red)

        # Create squre
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT - self.rect.height)

        # speed x
        self.speed_x = 0

    def update(self):
        # self.rect.y += 5
        self.speed_x = 0
        keys_state = pygame.key.get_pressed()

        if keys_state[pygame.K_LEFT]:
            self.speed_x = -5

        if keys_state[pygame.K_RIGHT]:
            self.speed_x = 5

        self.rect.x += self.speed_x

        if self.rect.bottom > HEIGHT:
            self.rect.y = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        group_bullet.add(bullet)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # x =  center of plane
        # y = top of plane
        """ Main function alway run, when we are call """
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 10))
        self.image.fill(red)

        # Create squre
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

        # speed y
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y

        if self.rect.y < 0:
            self.kill()


font_name = pygame.font.match_font("arial")


def draw_text(screen, text, size, y, x):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """ Main function alway run, when we are call """
        pygame.sprite.Sprite.__init__(self)

        img = "C:\\Users\\Hery\\Desktop\\My Projects\\Python-PyGame\\EP.4 - Python PyGame\\First Game\\aircraft.png"
        self.image = pygame.image.load(img).convert_alpha()

        # self.image = pygame.Surface((50, 50))
        # self.image.fill(red)

        # Create squre
        self.rect = self.image.get_rect()

        # random x kernel
        rand_x = random.randint(self.rect.width, WIDTH - self.rect.width)

        # Center position
        self.rect.center = (rand_x, 0)

        # speed y
        self.speed_y = random.randint(1, 10)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.bottom > HEIGHT:
            self.rect.y = 0
            rand_x = random.randint(self.rect.width, WIDTH - self.rect.width)
            self.rect.x = rand_x
            self.speed_y = random.randint(1, 10)


# Create Sprite group
all_sprites = pygame.sprite.Group()
group_enemy = pygame.sprite.Group()
group_bullet = pygame.sprite.Group()

# player
player = Player()
all_sprites.add(player)

# enemy
for i in range(5):
    enemy = Enemy()
    all_sprites.add(enemy)
    group_enemy.add(enemy)

# Status of game
running = True

while running:
    # User game running in framerate
    clock.tick(FPS)

    # Check are you close game?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    collide = pygame.sprite.spritecollide(player, group_enemy, False)
    # if collide:
    #     LIVES -= 1

    if collide:
        running = False

    # Bullet collission
    hits = pygame.sprite.groupcollide(group_bullet, group_enemy, True, True)
    # print(hits)
    for h in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        group_enemy.add(enemy)
        # Add score
        SCORE += 10 

      # Use game background
    screen.fill(black)

    screen.blit(background, background_rect)

    draw_text(screen, f"SCORE: {SCORE}", 20, WIDTH-1250, 10)
    draw_text(screen, f"LIVES: {LIVES}", 20, 50, 10)

    # Use all game actors
    all_sprites.draw(screen)

    # Show Pygame
    pygame.display.flip()


# Quit game
pygame.quit()
