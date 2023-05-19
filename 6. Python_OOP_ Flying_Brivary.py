import pygame
import requests
import math
from io import BytesIO

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
IMAGE_WIDTH = 200
IMAGE_HEIGHT = 200

# URL of the image
image_url = "https://img.pokemondb.net/artwork/braviary.jpg"

# Download the image and save it locally
response = requests.get(image_url)
image_data = response.content
image_path = "braviary.jpg"  # Choose a local filename to save the image
with open(image_path, "wb") as file:
    file.write(image_data)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Braviary Flying")

# Load the image using pygame
braviary_image = pygame.image.load(image_path)
braviary_image = pygame.transform.scale(braviary_image, (IMAGE_WIDTH, IMAGE_HEIGHT))

# Initial position of Braviary
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2
radius = min(center_x, center_y) - IMAGE_WIDTH // 2
angle = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the position of Braviary using circular motion equations
    braviary_x = center_x + math.cos(math.radians(angle)) * radius - IMAGE_WIDTH // 2
    braviary_y = center_y + math.sin(math.radians(angle)) * radius - IMAGE_HEIGHT // 2

    # Increment the angle to make Braviary move along the circular path
    angle += 1

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the Braviary image at the updated position
    screen.blit(braviary_image, (braviary_x, braviary_y))

    # Update the display
    pygame.display.flip()

    # Add a small delay to control the speed of the animation
    pygame.time.delay(10)

# Quit the game
pygame.quit()

