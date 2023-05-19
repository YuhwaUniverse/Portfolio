

import pygame
import requests
import math
from io import BytesIO

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
IMAGE_WIDTH = 200
IMAGE_HEIGHT = 200

image_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/628.png"

# Download the image and save it locally
response = requests.get(image_url)
image_data = response.content
image_path = "braviary.jpg"  
with open(image_path, "wb") as file:
    file.write(image_data)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Braviary Flying")


braviary_image = pygame.image.load(image_path)
braviary_image = pygame.transform.scale(braviary_image, (IMAGE_WIDTH, IMAGE_HEIGHT))

# Initial position of Braviary
center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2
radius = min(center_x, center_y) - IMAGE_WIDTH // 2
angle = 0
angle_increment = 0.7 

# Motion loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 
    braviary_x = center_x + math.cos(math.radians(angle)) * radius - IMAGE_WIDTH // 2
    braviary_y = center_y + math.sin(math.radians(angle)) * radius - IMAGE_HEIGHT // 2

   
    angle += angle_increment
    screen.fill((255, 255, 255))
    screen.blit(braviary_image, (braviary_x, braviary_y))


    pygame.display.flip()
    pygame.time.delay(10)


pygame.quit()

