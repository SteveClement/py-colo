import pygame, sys
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0, 100)
GREEN = (0, 255, 0, 100)
BLUE = (0, 0, 255, 100)

size = (500, 500)

x, y = 200, 200

pygame.init()

# Initial angle
angle = 0

# Set up clock
clock = pygame.time.Clock()
speed_per_second = 90  # Pixels per second

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Rotate me')

surf1 = pygame.Surface(size)
surf1.fill(BLACK)
surf1.set_colorkey(BLACK)
pygame.draw.circle(surf1, BLUE, (430, 280), 60)

surf2 = pygame.Surface(size)
surf2.fill(BLACK)
surf2.set_colorkey(BLACK)
pygame.draw.circle(surf2, GREEN, (370, 280), 60)

surf3 = pygame.Surface(size)
surf3.fill(BLACK)
surf3.set_colorkey(BLACK)
pygame.draw.circle(surf3, RED, (400, 220), 60)


surf4 = pygame.Surface(size)
surf4.set_colorkey(BLACK)
surf4.blit(surf1, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
surf4.blit(surf2, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
surf4.blit(surf3, (0, 0), special_flags=pygame.BLEND_RGB_ADD)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Get the time elapsed since the last frame
    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    # Update the angle
    angle += speed_per_second * dt
    angle %= 360  # Ensure the angle stays within 0-359 degrees

    # Rotate the surface around its own axis
    rotated_surface = pygame.transform.rotate(surf4, angle)
    rotated_rect = rotated_surface.get_rect(center=(x, y))

    screen.fill(WHITE)
    # Draw the rotated surface
    screen.blit(rotated_surface, rotated_rect.topleft)
#    screen.blit(surf4, (x, 0))

    pygame.display.flip()
