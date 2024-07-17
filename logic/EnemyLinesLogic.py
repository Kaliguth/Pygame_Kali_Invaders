# EnemyLinesLogic class

# Import required global vars
from util.Globals import WIDTH


class EnemyLinesLogic:
    def __init__(self, enemy_lines):
        # Enemy lines object
        self.__enemy_lines = enemy_lines
        # Booleans to determine if enemies can move left or right
        self.__can_move_right = True  # Enemies will move right first
        self.__can_move_left = False

    # Method to move enemies left or right
    def enemy_lines_movement(self):
        # If enemies can move right
        if self.__can_move_right:
            # Find rightmost enemy that is not destroyed (None)
            __last_enemy_index = 8
            columns_checked = 0
            last_enemy = None
            # Check enemies in every column from right to left
            while columns_checked < 9:
                __last_enemy_index = 8 - columns_checked
                while last_enemy is None and __last_enemy_index <= columns_checked + 18:
                    last_enemy = self.__enemy_lines.enemies[__last_enemy_index]
                    __last_enemy_index += 9
                columns_checked += 1

            # If rightmost enemy found
            if last_enemy:
                # If the rightmost enemy has not hit the right edge of the screen yet
                if last_enemy.rect.right < WIDTH - 5:
                    # Move right by changing enemy lines' start x (add current speed - changes based on difficulty)
                    self.__enemy_lines.start_x += self.__enemy_lines.enemy_speed
                # If the rightmost enemy hit the right edge of the screen
                else:
                    # Set booleans to move left next
                    self.__can_move_right = False
                    self.__can_move_left = True

        # If enemies can move left
        if self.__can_move_left:
            # Find leftmost enemy that is not destroyed (None)
            __first_enemy_index = 0
            columns_checked = 0
            first_enemy = None
            # Check enemies in every column from left to right
            while columns_checked < 9:
                __first_enemy_index = 0 + columns_checked
                while first_enemy is None and __first_enemy_index <= columns_checked + 18:
                    first_enemy = self.__enemy_lines.enemies[__first_enemy_index]
                    __first_enemy_index += 9
                columns_checked += 1

            # If leftmost enemy found
            if first_enemy:
                # If the leftmost enemy has not hit the left edge of the screen yet
                if first_enemy.rect.left > 6:
                    # Move left by changing enemy lines' start x (add current speed - changes based on difficulty)
                    self.__enemy_lines.start_x -= self.__enemy_lines.enemy_speed
                # If the leftmost enemy hit the left edge of the screen
                else:
                    # Set booleans to move right next
                    self.__can_move_left = False
                    self.__can_move_right = True

    # Method to check if any enemy is hit by the player's projectiles
    def check_enemies_hit(self):
        # Boolean to determine if an enemy was hit
        enemy_hit = False

        # Go over all enemy lines' enemies
        for index, enemy in enumerate(self.__enemy_lines.enemies):
            # If the enemy is not destroyed (not None)
            if enemy:
                # Go over all player's projectiles
                for projectile in self.__enemy_lines.player.projectiles:
                    # If one of the projectiles hit the enemy
                    if enemy.rect.colliderect(projectile.rect):
                        # Destroy the enemy (change to None)
                        self.__enemy_lines.enemies[index] = None
                        # Change enemy hit boolean to True
                        enemy_hit = True
                        # Change the projectile's enemy hit boolean to True (for removing it)
                        projectile.enemy_hit = True

                        # Add score to the player
                        # Score changes based on elapsed game time
                        # If elapsed game time is less than 5 minutes - add 300 minus elapsed game time to score
                        if 300 - self.__enemy_lines.game_time > 1:
                            self.__enemy_lines.player.score += 300 - self.__enemy_lines.game_time
                        # If elapsed game time is longer than 5 minutes - add 1 to score
                        else:
                            self.__enemy_lines.player.score += 1
                        # If a projectile hit an enemy - break the loop
                        break

            # If an enemy was hit - break the loop
            if enemy_hit:
                break

    # Method to check if the player was hit by any enemy projectile
    def check_player_hit(self):
        # Boolean to determine if the player was hit
        __player_hit = False

        # Go over all enemy lines' enemies
        for index, enemy in enumerate(self.__enemy_lines.enemies):
            # If the enemy is not destroyed (not None)
            if enemy:
                # If the enemy has a projectile
                if enemy.projectile:
                    # If the projectile hit the player
                    if self.__enemy_lines.player.spaceship_rect.colliderect(enemy.projectile):
                        # Decrease the player's health by 1
                        self.__enemy_lines.player.health -= 1
                        # Set player hit boolean to True
                        __player_hit = True
                        # Set the enemy's projectile's player hit boolean to True (for removing it)
                        enemy.projectile.player_hit = True
                        # Set the player's got hit boolean to True (for hit animation)
                        self.__enemy_lines.player.got_hit = True
                        # Set the enemy's projectile to None
                        enemy.projectile = None
                        # If an enemy projectile hit the player - break the loop
                        break

            # If the player was hit - break the loop
            if __player_hit:
                break
