

# The Braviary, a Flying-type Pokémon, is utilized to update its position and display it on the screen, creating a flying motion in a circular path.


import pygame
import requests
import math
from io import BytesIO

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
IMAGE_WIDTH = 200
IMAGE_HEIGHT = 200

image_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/628.png"

class Braviary:
    def __init__(self, center_x, center_y, radius, angle_increment):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.angle = 0
        self.angle_increment = angle_increment

        # Download the image and save it locally
        response = requests.get(image_url)
        image_data = response.content
        image_path = "braviary.jpg"  
        with open(image_path, "wb") as file:
            file.write(image_data)

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (IMAGE_WIDTH, IMAGE_HEIGHT))

    def update_position(self):
        braviary_x = self.center_x + math.cos(math.radians(self.angle)) * self.radius - IMAGE_WIDTH // 2
        braviary_y = self.center_y + math.sin(math.radians(self.angle)) * self.radius - IMAGE_HEIGHT // 2
        self.angle += self.angle_increment
        return braviary_x, braviary_y

    def display(self, screen, position):
        screen.blit(self.image, position)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Braviary Flying")

braviary = Braviary(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, min(SCREEN_WIDTH, SCREEN_HEIGHT) // 2 - IMAGE_WIDTH // 2, 0.7)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    braviary_position = braviary.update_position()
    braviary.display(screen, braviary_position)

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()

