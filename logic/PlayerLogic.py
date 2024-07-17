# PlayerLogic class

# pygame imports
import pygame

# Object imports
from player.projectiles.PlayerProjectile import PlayerProjectile

# Import required global vars
from util.Globals import WIDTH

# Other imports
import random


class PlayerLogic:
    # Constructor
    def __init__(self, player):
        self.__player = player  # Player object

    # Method to move the player's spaceship left
    def move_left(self):
        # If the spaceship has not hit the left edge of the screen
        if self.__player.spaceship_rect.left > 6:
            # Set the moving boolean to True
            self.__player.moving = True
            # If the spaceship did not move left yet - play a random engine sound
            # Engine sounds only play if the last movement was to the opposite side
            if not self.__player.moved_left:
                sound = pygame.mixer.Sound(random.choice(self.__player.spaceship_sounds))
                sound.play()
            # Spaceship and engine moving logics
            self.__player.spaceship_rect.x -= self.__player.spaceship_speed
            self.__player.engine_rect.x -= self.__player.spaceship_speed
            self.__player.current_x -= self.__player.spaceship_speed
            # Set the moved booleans accordingly
            self.__player.moved_left = True
            self.__player.moved_right = False

    # Method to move the player's spaceship left
    def move_right(self):
        # If the spaceship has not hit the right edge of the screen
        if self.__player.spaceship_rect.right < WIDTH - 5:
            # Set the moving boolean to True
            self.__player.moving = True
            # If the spaceship did not move right yet - play a random engine sound
            # Engine sounds only play if the last movement was to the opposite side
            if not self.__player.moved_right:
                sound = pygame.mixer.Sound(random.choice(self.__player.spaceship_sounds))
                sound.play()
            # Spaceship and engine moving logics
            self.__player.spaceship_rect.x += self.__player.spaceship_speed
            self.__player.engine_rect.x += self.__player.spaceship_speed
            self.__player.current_x += self.__player.spaceship_speed
            # Set the moved booleans accordingly
            self.__player.moved_right = True
            self.__player.moved_left = False

    # Method to shoot a projectile out of the spaceship
    def shoot(self):
        # Get current time
        time = pygame.time.get_ticks()
        # If enough time passed since last shot (800 milliseconds) - can shoot
        if time - self.__player.last_shot > self.__player.shoot_delay:
            # Set last shot time to current time
            self.__player.last_shot = time
            # Create a new projectile object
            projectile = PlayerProjectile(self.__player)
            # Add the projectile to the player's projectiles list
            self.__player.projectiles.append(projectile)
            # Play a shooting sound
            sound = pygame.mixer.Sound("sound_effects/spaceship/shoot.ogg")
            sound.set_volume(0.5)
            sound.play()
