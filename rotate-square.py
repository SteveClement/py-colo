import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Rotate Surface on Its Own Axis')

# Create a surface (a red square for demonstration)
surface = pygame.Surface((50, 50), pygame.SRCALPHA)
surface.fill((255, 0, 0))

# Initial position
x, y = 100, 100

# Set up clock
clock = pygame.time.Clock()
rotation_speed_per_second = 10  # Degrees per second

# Initial angle
angle = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the time elapsed since the last frame
    dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

    # Update the angle
    angle += rotation_speed_per_second * dt
    angle %= 360  # Ensure the angle stays within 0-359 degrees

    # Rotate the surface around its own axis
    rotated_surface = pygame.transform.rotate(surface, angle)
    rotated_rect = rotated_surface.get_rect(center=(x, y))

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw the rotated surface
    screen.blit(rotated_surface, rotated_rect.topleft)

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()

