# EnemyLogic class

# pygame imports
import pygame

# Object imports
from enemies.projectiles.EnemyProjectile import EnemyProjectile


class EnemyLogic:
    # Constructor
    def __init__(self, enemy):
        # Enemy object
        self.enemy = enemy

    # Method to make an enemy shoot
    def shoot(self):
        # Get current time
        time = pygame.time.get_ticks()
        # If there is no projectile yet and the time from last shot is larger than the delay time (20 seconds)
        if self.enemy.projectile is None and time - self.enemy.last_shot > self.enemy.shoot_delay:
            # Set last shot time to now
            self.enemy.last_shot = time
            # Set a new projectile to the enemy
            self.enemy.projectile = EnemyProjectile(self.enemy)
