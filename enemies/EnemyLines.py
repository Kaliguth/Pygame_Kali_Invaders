# EnemyLines class
# This class gets a list of enemies and draws them on the screen in 3 lines of up to 9 enemies

# pygame imports
import pygame
from pygame import Surface

# Logic imports
from logic.EnemyLinesLogic import EnemyLinesLogic

# Import required global vars
from util.Globals import WIDTH, HEIGHT


class EnemyLines:
    def __init__(self, enemies, player, enemy_speed):
        # Enemy lines logic object to use methods
        self.enemy_lines_logic = EnemyLinesLogic(self)
        # Enemy list object
        self.enemies = enemies
        # Player object
        self.player = player
        # Enemy speed variable (based on difficulty)
        self.enemy_speed = enemy_speed
        # Current x y positions variables (used for movements and drawing enemies in the right positions):
        # Current x position of enemy lines' beginning (leftmost side)
        self.start_x = WIDTH / 2 - 546
        # Current y position of enemy lines' line (starts as top line's y)
        self.__start_y = HEIGHT / 2 - 400
        # x and y offsets variables for drawing next enemy lines and columns:
        # x offset = Distance between enemies in the same line
        self.__x_offset = 130
        # y offset = Distance between each line
        self.__y_offset = 120
        # Max enemies per line variable
        self.__enemies_per_line = 9
        # Elapsed time of game variable (for score)
        self.game_time = 0
        # Ticks to count get time
        self.ticks = pygame.time.get_ticks()

    # Method to check if enemy lines object is empty (all enemies are None - Destroyed enemies become None)
    def is_empty(self):
        for enemy in self.enemies:
            if enemy is not None:
                return False
        return True

    # Method to update elapsed game time, check projectile collisions and move enemy lines
    def update(self):
        # Get current time
        current_ticks = pygame.time.get_ticks()
        # Check if a second has passed (1000 ticks is one second)
        if current_ticks - self.ticks >= 1000:
            # Add one second to elapsed game time
            self.game_time += 1
            # Update the current ticks to the ticks variable
            self.ticks = current_ticks
        # Check projectile collisions
        self.enemy_lines_logic.check_enemies_hit()
        self.enemy_lines_logic.check_player_hit()
        # Move enemy lines
        self.enemy_lines_logic.enemy_lines_movement()

        # Update existing enemy in the list (not None/not destroyed)
        for enemy in self.enemies:
            if enemy:
                enemy.update()

    # Method to draw all enemies in lines based on the variables
    def draw(self, screen: Surface):
        # Current x and y positions to draw
        current_x = self.start_x
        current_y = self.__start_y
        # Number of enemies in the current line
        current_line_enemies = 0

        # Go over all enemies in the list
        for enemy in self.enemies:
            # If the enemy is not destroyed (not None)
            if enemy:
                # Set enemy's current x position to the x location it was drawn at
                enemy.current_x = current_x
                # Set enemy's top left of the rect to current x and y
                enemy.rect.topleft = (current_x, current_y)
                # Draw enemy on the screen
                screen.blit(enemy.image, (current_x, current_y))
                # If enemy has a projectile - draw it
                if enemy.projectile:
                    enemy.projectile.draw(screen)
            # If enemy is destroyed (None)
            else:
                # Draw a transparent rect
                transparent_rect = pygame.Surface((50, 50), pygame.SRCALPHA)
                transparent_rect.fill((0, 0, 0, 0))  # Fill with fully transparent color
                screen.blit(transparent_rect, (current_x, current_y))

            # Change x location to draw the next enemy (next column)
            current_x += self.__x_offset
            # Add 1 to enemies in the line
            current_line_enemies += 1

            # If enemies in line reached the max number of enemies per line
            if current_line_enemies == self.__enemies_per_line:
                # Set x position for next enemy to the beginning of the enemy lines (first column)
                current_x = self.start_x
                # Set y position to be the next line
                current_y += self.__y_offset
                # Set enemies in line to 0
                current_line_enemies = 0
