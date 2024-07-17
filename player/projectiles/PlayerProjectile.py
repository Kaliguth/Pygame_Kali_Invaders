# Projectile class

import pygame


class PlayerProjectile(pygame.sprite.Sprite):
    def __init__(self, player):
        # Initiate sprite constructor
        super().__init__()
        # Projectile's player object
        self.__player = player
        # Current player's x position variable - for shooting the projectile from the right location
        self.__center_x = player.current_x
        # Projectile width
        self.__width = 50
        # Projectile height
        self.__height = 50
        # Projectile speed
        self.__speed = 5
        # Boolean to determine if the projectile hit an enemy
        self.enemy_hit = False

        # Projectile images list
        self.__sprites = []
        # Current sprite variable
        self.__current_sprite = 0
        # Load projectile images based on player's spaceship's color
        self.load_images(player.spaceship_color)

        # Projectile parameters:
        # Image - Starts as first projectile's image
        self.image = self.__sprites[int(self.__current_sprite)]
        self.image = pygame.transform.scale(self.image, (self.__width, self.__height))
        # Rect
        self.rect = self.image.get_rect()
        self.rect.center = (player.current_x, player.spaceship_rect.top - 10)

    # Method to add projectile images to the projectile images list
    def load_images(self, color):
        # Set number of frames based on spaceship's color
        # Each projectile color has different number of images
        __frames = 0
        if color == "red":
            __frames = 3
        elif color == "orange":
            __frames = 4
        elif color == "green":
            __frames = 10
        else:
            __frames = 8

        # Add all projectile images to the projectile images list
        for index in range(1, __frames+1):
            image = pygame.image.load(f"player/projectiles/images/{color}_{index}.png")
            self.__sprites.append(image)

    # Method to update the projectile
    def update(self):
        # Increment current active sprite by 0.2 (when it reaches next sprite index, image changes)
        self.__current_sprite += 0.2

        # If the projectile's animation is over - start it over
        if self.__current_sprite >= len(self.__sprites):
            self.__current_sprite = 0

        # Set image to the image in current sprite index
        self.image = self.__sprites[(int(self.__current_sprite))]
        # Render the current sprite image
        self.image = pygame.transform.scale(self.image, (self.__width, self.__height))

        # Move the projectile up
        self.rect.y -= self.__speed

        # If the projectile left the screen or hit an enemy - delete it
        if self.rect.bottom < 0 or self.enemy_hit:
            self.kill()
