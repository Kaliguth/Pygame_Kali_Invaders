# EnemyProjectile class

# pygame imports
import pygame
from pygame import Surface

# Import required global vars
from util.Globals import HEIGHT

# Other imports
import random


class EnemyProjectile(pygame.sprite.Sprite):
    def __init__(self, enemy):
        # Initiate sprite constructor
        super().__init__()
        # Projectile's enemy object
        self.__enemy = enemy
        # Current enemy's x position variable - for shooting the projectile from the right location
        self.__center_x = enemy.current_x
        # Projectile width
        self.__width = 10
        # Projectile height
        self.__height = 30
        # Projectile speed
        self.__speed = 2
        # Boolean to determine if the projectile hit the player
        self.player_hit = False

        # Projectile images list
        self.__projectiles = []
        # Load projectile images into the list
        self.load_images()

        # Projectile parameters:
        # Image - picks a random projectile image from the projectile images list
        self.image = random.choice(self.__projectiles)
        self.image = pygame.transform.scale(self.image, (self.__width, self.__height))
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = (enemy.current_x, enemy.rect.bottom + 10)

    # Method to add projectile images to the projectile images list
    def load_images(self):
        # 8 projectile images
        for index in range(1, 9):
            image = pygame.image.load(f"enemies/projectiles/images/laser_{index}.png")
            self.__projectiles.append(image)

    # Method to update the projectile's location and check collision
    def update(self):
        # Move the projectile down
        self.rect.y += self.__speed

        # If the projectile left the screen or hit the player - delete it
        if self.rect.bottom > HEIGHT or self.player_hit:
            self.kill()

    # Method to Draw the projectile
    def draw(self, screen: Surface):
        # Render projectile
        screen.blit(self.image, self.rect)
