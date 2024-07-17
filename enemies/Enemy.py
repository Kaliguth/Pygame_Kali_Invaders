# Enemy class

# pygame imports
import pygame

# Logic imports
from logic.EnemyLogic import EnemyLogic

# Import required global vars
from util.Globals import HEIGHT

# Other imports
import random


class Enemy:
    # Constructor
    def __init__(self, width, height):
        # Enemy logic object - for using the shoot method
        self.enemy_logic = EnemyLogic(self)

        # Current enemy spaceship's x location for projectiles
        self.current_x = 0

        # Enemy spaceship images list
        self.__spaceships = []
        # Load enemy spaceship images into the list
        self.load_images()

        # Enemy spaceship parameters:
        # Image (uses a random spaceship image from the list)
        self.image = random.choice(self.__spaceships)
        self.image = pygame.transform.scale(self.image, (width, height))
        # Rect
        self.rect = self.image.get_rect()

        # Projectile parameters:
        # Projectile variable
        self.projectile = None
        # Twenty-second delay between shots
        self.shoot_delay = 20000
        # Ticks to check when was last shot - initial time randomized up to 20 seconds
        self.last_shot = pygame.time.get_ticks() - random.randint(0, 20000)

    # Method to load enemy spaceship images
    def load_images(self):
        # 35 enemy spaceships
        for index in range(1, 36):
            self.__spaceships.append(pygame.image.load(f"enemies/spaceships/enemy_{index}.png"))

    # Method to use the shoot method and update the current projectile
    def update(self):
        # Shoot automatically
        self.enemy_logic.shoot()

        # Update the projectile (if there is one)
        if self.projectile:
            self.projectile.update()
            # Remove the projectile if it has left the screen
            if self.projectile.rect.top > HEIGHT:
                self.projectile = None

    # Draw:
    # EnemyLines handles enemy drawing
