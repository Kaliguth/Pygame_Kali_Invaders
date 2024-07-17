# Player class

# pygame imports
import pygame
from pygame import Surface

# Import required global vars
from util.Globals import HEIGHT


class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, center_x, center_y, width, height, spaceship_type, spaceship_color):
        super().__init__()
        self.center_y = center_y  # Spaceship's center y variable - for engine's location
        self.__width = width  # Spaceship's width
        self.__height = height  # Spaceship's height
        self.spaceship_color = spaceship_color  # Spaceship's color variable - for choosing fitting projectiles
        self.spaceship_speed = 5  # Spaceship's speed
        self.engine_height = center_y - height / 2 + 22  # Engine's location based on spaceship's center y
        self.__engine_width = 70  # Engine's width
        self.__engine_height = 70  # Engine's height
        self.health = 5  # Player's health
        self.score = 0  # Player's score
        self.moving = False  # Boolean to determine if the spaceship is moving - for engine animation
        self.moved_left = False  # Boolean to determine if the spaceship already moved left
        self.moved_right = False  # Boolean to determine if the spaceship already moved right
        self.got_hit = False  # Boolean to determine if the spaceship was hit by an enemy
        self.__hit_time = None  # Hit time variable to know when the spaceship was last hit

        # Current spaceship x location for projectiles
        self.current_x = center_x

        # Animation sprites objects and variables
        self.__sprites = {}
        self.__current_sprite = 0
        self.spaceship_sounds = []
        self.load_images(spaceship_color)  # Load images based on the spaceship's color
        self.load_sounds()  # Load spaceship's engine sounds

        # Spaceship parameters:
        # Image (uses given type and color from constructor parameters)
        self.spaceship_image = (pygame.image.load
                                (f"player/spaceships/spaceship{spaceship_type}_{spaceship_color}.png"))
        self.spaceship_image = pygame.transform.scale(self.spaceship_image, (width, height))
        # Rect
        self.spaceship_rect = self.spaceship_image.get_rect()
        self.spaceship_rect.center = (center_x, center_y)

        # Engine parameters:
        # Image - starts as a moving engine image for entry animation
        self.engine_image = self.__sprites["moving_engine"][self.__current_sprite]
        self.engine_image = pygame.transform.scale(self.engine_image, (self.__engine_width, self.__engine_height))
        # Rect
        self.engine_rect = self.engine_image.get_rect()
        self.engine_rect.center = (center_x, self.engine_height + height)

        # Hit animation parameters:
        # Image - starts as first hit image (only displayed when enemy is hit)
        self.hit_image = self.__sprites["hit"][self.__current_sprite]
        self.hit_image = pygame.transform.scale(self.hit_image, (width, height))
        # Rect
        self.hit_rect = self.hit_image.get_rect()
        self.hit_rect.center = (self.current_x, HEIGHT - self.__height - 20)

        # Projectile parameters:
        # Player's projectiles list
        self.projectiles = []
        # 800-millisecond delay between shots
        self.shoot_delay = 800
        # Ticks - for checking when was last shot
        self.last_shot = pygame.time.get_ticks()

    # Method to load images
    def load_images(self, color):
        # Idle engine animation images list (for when spaceship is idle)
        idle_engine_sprites = []
        # Set number of frames and location based on spaceship's color
        # Each engine color has different number of images and needs a different location
        __frames = 0
        if color == "red":
            __frames = 3
            self.engine_height = self.center_y - self.__height / 2 - 10
        elif color == "orange":
            __frames = 4
            self.engine_height = self.center_y - self.__height / 2 - 13
        elif color == "green":
            __frames = 4
            self.engine_height = self.center_y - self.__height / 2 + 5
        else:
            __frames = 6

        # Add all engine images into the list
        for index in range(1, __frames+1):
            idle_engine_sprites.append(pygame.image.load(f"player/engines/{color}_idle_{index}.png"))
        # Set idle engine sprite with added images
        self.__sprites["idle_engine"] = idle_engine_sprites

        # Moving engine animation images list (for when spaceship is moving)
        # Same logic as idle engine sprite
        moving_engine_frames = []
        if color == "red":
            __frames = 4
        elif color == "orange":
            __frames = 4
        elif color == "green":
            __frames = 4
        else:
            __frames = 7

        for index in range(1, __frames + 1):
            moving_engine_frames.append(pygame.image.load(f"player/engines/{color}_moving_{index}.png"))
        # Set moving engine sprite with added images
        self.__sprites["moving_engine"] = moving_engine_frames

        # Hit animation images list (for when spaceship is hit)
        hit_frames = []
        # This animation uses 3 images
        for index in range(1, 4):
            hit_frames.append(pygame.image.load(f"player/effects/hit_{index}.png"))
        # Set hit sprite with added images
        self.__sprites["hit"] = hit_frames

    # Method to load spaceship engine sounds (for when spaceship is moving)
    def load_sounds(self):
        for index in range(1, 10):
            self.spaceship_sounds.append(pygame.mixer.Sound(f"sound_effects/spaceship/move_{index}.ogg"))
        self.__sprites["spaceship_sounds"] = self.spaceship_sounds

    # Method to update the player
    def update(self):
        # Increment current active sprites by 0.2 (when it reaches next sprite index, image changes)
        self.__current_sprite += 0.2

        # If the spaceship is moving
        if self.moving:
            # If the moving engine animation is over - start it over
            if self.__current_sprite >= len(self.__sprites["moving_engine"]):
                self.__current_sprite = 0

            # Set image to the image in current sprite index
            self.engine_image = self.__sprites["moving_engine"][(int(self.__current_sprite))]
        # If the spaceship is idle
        else:
            # If the idle engine animation is over - start it over
            if self.__current_sprite >= len(self.__sprites["idle_engine"]):
                self.__current_sprite = 0

            # Set image to the image in current sprite index
            self.engine_image = self.__sprites["idle_engine"][(int(self.__current_sprite))]

        # Render the engine image of the current sprite
        self.engine_image = pygame.transform.scale(self.engine_image, (self.__engine_width, self.__engine_height))
        # Set moving boolean to False (if the spaceship is still moving, it will change to True again)
        self.moving = False

        # If the spaceship is hit by an enemy
        if self.got_hit:
            # Set the hit animation rect based on current the spaceship's location
            self.hit_rect = self.hit_image.get_rect()
            self.hit_rect.center = (self.current_x, HEIGHT - self.__height - 20)
            # If there is no hit time (animation did not start yet) - set the time of the hit
            if self.__hit_time is None:
                self.__hit_time = pygame.time.get_ticks()
            # Check how long the animation is playing
            time_animating = pygame.time.get_ticks() - self.__hit_time

            # If the animation played for 1 second,
            # stop it, change the got hit boolean to False and remove the hit time
            if time_animating >= 1000:
                self.got_hit = False
                self.__hit_time = None
            # Otherwise keep playing the animation
            else:
                if self.__current_sprite >= len(self.__sprites["hit"]):
                    self.__current_sprite = 0
                self.hit_image = self.__sprites["hit"][(int(self.__current_sprite))]
                self.hit_image = pygame.transform.scale(self.hit_image, (self.__width, self.__height))

        # Update all projectiles
        for projectile in self.projectiles:
            projectile.update()
            # Remove projectiles that have left the screen or hit an enemy from the list
            if projectile.rect.bottom < 0 or projectile.enemy_hit:
                self.projectiles.remove(projectile)

    # Method to draw the spaceship and it's projectiles
    def draw(self, screen: Surface):
        # Render the spaceship and engine images
        screen.blit(self.spaceship_image, self.spaceship_rect)
        screen.blit(self.engine_image, self.engine_rect)

        # If spaceship got hit, render the hit animation
        if self.got_hit:
            screen.blit(self.hit_image, self.hit_rect)

        # Render all projectiles
        for projectile in self.projectiles:
            screen.blit(projectile.image, projectile.rect)
