# Credits class

# pygame imports
import pygame
from pygame import Surface

# Import required global vars
from util.Globals import (WIDTH, HEIGHT, WHITE, CREDITS_TITLE_TEXT, RETURN_TO_MENU_TEXT,
                          MUSIC_SOUND_EFFECTS_TEXT, IMAGES_ANIMATIONS_TEXT,
                          DKLON_TEXT, DKLON_SOUND_TEXT, BART_TEXT, BART_SOUND_TEXT,
                          QUBODUP_TEXT, QUBODUP_SOUND_TEXT, CONGUS_TEXT, CONGUS_MUSIC_TEXT,
                          ERIC_TEXT, ERIC_MUSIC_TEXT, MATTHEW_TEXT, MATTHEW_MUSIC_TEXT,
                          MAXSTACK_TEXT, MAXSTACK_MUSIC_TEXT, ROBIN_TEXT, ROBIN_SOUND_TEXT,
                          RAWDANITSU_TEXT, RAWDANITSU_IMAGE_TEXT, KENNEY_TEXT,
                          KENNEY_IMAGE_TEXT1, KENNEY_IMAGE_TEXT2, FOOZLE_TEXT, FOOZLE_IMAGE_TEXT)


class CreditsPage:
    def __init__(self):
        # Rect for transparent surface measurements
        self.__rect = pygame.Rect(50, 130, WIDTH - 100, HEIGHT - 250)
        # Transparent surface
        self.__transparent_surface = pygame.Surface((self.__rect.width, self.__rect.height), pygame.SRCALPHA)

    def draw(self, screen: Surface):
        # Transparent white color for the surface
        transparent_white = (*WHITE, 150)
        # Fill the transparent surface with the color
        self.__transparent_surface.fill(transparent_white)

        # Render the transparent surface
        screen.blit(self.__transparent_surface, (self.__rect.x, self.__rect.y))

        # Credits title text
        credits_title_rect = (WIDTH / 2 - 90, HEIGHT / 2 - 450)
        screen.blit(CREDITS_TITLE_TEXT, credits_title_rect)

        # Music and sound effects text
        music_sound_effect_text_rect = (WIDTH / 2 - 500, HEIGHT / 2 - 320)
        screen.blit(MUSIC_SOUND_EFFECTS_TEXT, music_sound_effect_text_rect)

        # Music and sound effects credits:
        # dklon
        dklon_text_rect = (WIDTH / 2 - 495, HEIGHT / 2 - 270)
        screen.blit(DKLON_TEXT, dklon_text_rect)
        dklon_sound_text_rect = (WIDTH / 2 - 408, HEIGHT / 2 - 240)
        screen.blit(DKLON_SOUND_TEXT, dklon_sound_text_rect)
        # bart
        bart_text_rect = (WIDTH / 2 - 475, HEIGHT / 2 - 190)
        screen.blit(BART_TEXT, bart_text_rect)
        bart_sound_text_rect = (WIDTH / 2 - 415, HEIGHT / 2 - 160)
        screen.blit(BART_SOUND_TEXT, bart_sound_text_rect)
        # qubodup
        qubodup_text_rect = (WIDTH / 2 - 525, HEIGHT / 2 - 110)
        screen.blit(QUBODUP_TEXT, qubodup_text_rect)
        qubodup_sound_text_rect = (WIDTH / 2 - 355, HEIGHT / 2 - 80)
        screen.blit(QUBODUP_SOUND_TEXT, qubodup_sound_text_rect)
        # congusbongus
        congus_text_rect = (WIDTH / 2 - 575, HEIGHT / 2 - 30)
        screen.blit(CONGUS_TEXT, congus_text_rect)
        congus_sound_text_rect = (WIDTH / 2 - 375, HEIGHT / 2)
        screen.blit(CONGUS_MUSIC_TEXT, congus_sound_text_rect)
        # Robin Lamb
        robin_text_rect = (WIDTH / 2 - 535, HEIGHT / 2 + 50)
        screen.blit(ROBIN_TEXT, robin_text_rect)
        robin_sound_text_rect = (WIDTH / 2 - 382, HEIGHT / 2 + 80)
        screen.blit(ROBIN_SOUND_TEXT, robin_sound_text_rect)
        # Eric Matyes
        eric_text_rect = (WIDTH / 2 - 492, HEIGHT / 2 + 130)
        screen.blit(ERIC_TEXT, eric_text_rect)
        eric_music_text_rect = (WIDTH / 2 - 465, HEIGHT / 2 + 160)
        screen.blit(ERIC_MUSIC_TEXT, eric_music_text_rect)
        # Matthew Pablo
        matthew_text_rect = (WIDTH / 2 - 515, HEIGHT / 2 + 210)
        screen.blit(MATTHEW_TEXT, matthew_text_rect)
        matthew_music_text_rect = (WIDTH / 2 - 525, HEIGHT / 2 + 240)
        screen.blit(MATTHEW_MUSIC_TEXT, matthew_music_text_rect)
        # maxstack
        maxstack_text_rect = (WIDTH / 2 - 515, HEIGHT / 2 + 290)
        screen.blit(MAXSTACK_TEXT, maxstack_text_rect)
        maxstack_music_text_rect = (WIDTH / 2 - 365, HEIGHT / 2 + 320)
        screen.blit(MAXSTACK_MUSIC_TEXT, maxstack_music_text_rect)

        # Images and animations text
        images_animations_text_rect = (WIDTH / 2 + 180, HEIGHT / 2 - 320)
        screen.blit(IMAGES_ANIMATIONS_TEXT, images_animations_text_rect)

        # Images and animations credits:
        # Rawdanitsu
        rawdanitsu_text_rect = (WIDTH / 2 + 105, HEIGHT / 2 - 270)
        screen.blit(RAWDANITSU_TEXT, rawdanitsu_text_rect)
        rawdanitsu_image_text_rect = (WIDTH / 2 + 195, HEIGHT / 2 - 240)
        screen.blit(RAWDANITSU_IMAGE_TEXT, rawdanitsu_image_text_rect)
        # Kenney
        kenney_text_rect = (WIDTH / 2 + 205, HEIGHT / 2 - 190)
        screen.blit(KENNEY_TEXT, kenney_text_rect)
        kenney_image_text_rect1 = (WIDTH / 2 + 145, HEIGHT / 2 - 160)
        screen.blit(KENNEY_IMAGE_TEXT1, kenney_image_text_rect1)
        kenney_image_text_rect2 = (WIDTH / 2 + 245, HEIGHT / 2 - 130)
        screen.blit(KENNEY_IMAGE_TEXT2, kenney_image_text_rect2)
        # Foozle
        foozle_text_rect = (WIDTH / 2 + 225, HEIGHT / 2 - 80)
        screen.blit(FOOZLE_TEXT, foozle_text_rect)
        foozle_image_text_rect = (WIDTH / 2 + 285, HEIGHT / 2 - 50)
        screen.blit(FOOZLE_IMAGE_TEXT, foozle_image_text_rect)

        # Informative text to let users know exiting credits page is by pressing ESCAPE
        return_to_menu_rect = (WIDTH / 2 - 225, HEIGHT / 2 + 370)
        screen.blit(RETURN_TO_MENU_TEXT, return_to_menu_rect)

        # Update the display
        pygame.display.update()
