import pygame
from pygame.locals import *

# Start Pygame project
pygame.init()

# Set width, height
width = 900
height = 600

# Colors
black = (0, 0, 0)
red = (255, 0, 0)

# Frame per second(FPS)
FPS = 60

# Game screen
screen = pygame.display.set_mode((width, height))

# Game name
pygame.display.set_caption("Phenomenal Game")

# Create  clock of a game
clock = pygame.time.Clock()

# Game status
running = True  # True = YES, False = NO


class Player(pygame.sprite.Sprite):
    def __init__(self):
        """Main function alway run, when we are call"""
        pygame.sprite.Sprite.__init__(self)

        img = "C:\\Users\\Hery\\Desktop\\My Projects\\Python-PyGame\\EP.3 - Python PyGame\\First Game\\aircraft.png"
        self.image = pygame.image.load(img).convert_alpha()

        # self.image = pygame.Surface((50, 50))
        # self.image.fill(red)

        # Create squre
        self.rect = self.image.get_rect()
        self.rect.center = (width/2, height/2)

    def update(self):
        self.rect.y += 5
        if self.rect.bottom > height:
            self.rect.y = 0


# Create Sprite group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


while running:
    # User game running in framerate
    clock.tick(FPS)

    # Check are you close game?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Use game background
    screen.fill(black)

    # Use all game actors
    all_sprites.draw(screen)

    # Show Pygame
    pygame.display.flip()


# Quit game
pygame.quit()
