# Global variables

# pygame imports
import pygame.font

# Screen resolution
WIDTH, HEIGHT = 1500, 960

# Backgrounds
MENU_BG = pygame.transform.scale(pygame.image.load("backgrounds/Menu_bg.png"), (WIDTH, HEIGHT))
GAME_BG = pygame.transform.scale((pygame.image.load("backgrounds/Game_bg.png")), (WIDTH, HEIGHT))

# Colors
WHITE = 255, 255, 255
BLACK = 0, 0, 0
LIGHT_GREY = 190, 190, 190
DARK_GREY = 100, 100, 100
LIGHT_RED = 160, 40, 40
LIGHT_RED_2 = 255, 90, 90
DARK_RED = 139, 0, 0
LIGHT_GREEN = 102, 194, 102
DARK_GREEN = 0, 100, 0
LIGHT_BLUE = 108, 166, 205
DARK_BLUE = 0, 0, 139
LIGHT_ORANGE = 255, 120, 85
DARK_ORANGE = 255, 69, 0
GOLD = 255, 215, 0

# Fonts
pygame.font.init()  # Initiate pygame font module
TITLE_FONT = pygame.font.SysFont("Comic Sans", 60, bold=True)
SMALL_FONT = pygame.font.SysFont("Arial", 35, bold=True)
HUGE_FONT = pygame.font.SysFont("Comic Sans", 120, bold=True)
SMALLER_FONT = pygame.font.SysFont("Arial", 25, bold=True)
SMALLEST_FONT = pygame.font.SysFont("Arial", 20, bold=True)

# Rendering different texts:
# General (used in a more than one class)
QUIT_TEXT = SMALL_FONT.render("QUIT", True, WHITE)
RETURN_TO_MENU_TEXT = SMALL_FONT.render("Press ESCAPE to return to main menu", True, WHITE)
# Menu
TITLE_TEXT = TITLE_FONT.render("Kali Invaders", True, LIGHT_RED)
START_TEXT = SMALL_FONT.render("Press ENTER to start", True, BLACK)
HIGHSCORES_TEXT = SMALL_FONT.render("HIGHSCORES", True, WHITE)
COLOR_TEXT = SMALL_FONT.render("SPACESHIP COLOR", True, WHITE)
RED_TEXT = SMALL_FONT.render("RED", True, BLACK)
GREEN_TEXT = SMALL_FONT.render("GREEN", True, BLACK)
BLUE_TEXT = SMALL_FONT.render("BLUE", True, BLACK)
ORANGE_TEXT = SMALL_FONT.render("ORANGE", True, BLACK)
TYPE_TEXT = SMALL_FONT.render("SPACESHIP TYPE", True, WHITE)
TYPE_ONE_TEXT = SMALL_FONT.render("1", True, BLACK)
TYPE_TWO_TEXT = SMALL_FONT.render("2", True, BLACK)
TYPE_THREE_TEXT = SMALL_FONT.render("3", True, BLACK)
DIFFICULTY_TEXT = SMALL_FONT.render("CHOOSE DIFFICULTY", True, WHITE)
EASY_TEXT = SMALL_FONT.render("EASY", True, BLACK)
MEDIUM_TEXT = SMALL_FONT.render("MEDIUM", True, BLACK)
HARD_TEXT = SMALL_FONT.render("HARD", True, BLACK)
CREDITS_TEXT = SMALL_FONT.render("CREDITS", True, GOLD)
CONTROLS_TEXT = SMALL_FONT.render("CONTROLS", True, DARK_RED)
MOVE_KEY_TEXT = SMALLER_FONT.render("Move:               ←  → arrow keys", True, BLACK)
SHOOT_KEY_TEXT = SMALLER_FONT.render("Shoot:                   SPACE BAR", True, BLACK)
PAUSE_KEY_TEXT = SMALLER_FONT.render("Pause game:             ESCAPE", True, BLACK)
# Game
PAUSE_TEXT = TITLE_FONT.render("GAME PAUSED", True, BLACK)
RESUME_TEXT = SMALL_FONT.render("RESUME", True, WHITE)
RESTART_TEXT = SMALL_FONT.render("RESTART", True, WHITE)
QUIT_MENU_TEXT = TITLE_FONT.render("QUIT GAME?", True, BLACK)
CONTINUE_TEXT = SMALL_FONT.render("CONTINUE", True, WHITE)
GAME_OVER_TEXT = HUGE_FONT.render("GAME OVER", True, LIGHT_RED)
YOU_WIN_TEXT = HUGE_FONT.render("YOU WIN!", True, LIGHT_RED)
# Highscores
HIGHSCORES_TITLE_TEXT = TITLE_FONT.render("High scores", True, LIGHT_RED)
# Credits
CREDITS_TITLE_TEXT = TITLE_FONT.render("Credits", True, LIGHT_RED)
MUSIC_SOUND_EFFECTS_TEXT = SMALL_FONT.render("MUSIC & SOUND EFFECTS", True, DARK_RED)
DKLON_TEXT = SMALLER_FONT.render("dklon - opengameart.org/users/dklon", True, DARK_BLUE)
DKLON_SOUND_TEXT = SMALLEST_FONT.render("'Rocket Launch', 'laser5'", True, BLACK)
BART_TEXT = SMALLER_FONT.render("bart - opengameart.org/users/bart", True, DARK_BLUE)
BART_SOUND_TEXT = SMALLEST_FONT.render("'Space Ship Shield Sounds'", True, BLACK)
QUBODUP_TEXT = SMALLER_FONT.render("qubodup - opengameart.org/users/qubodup", True, DARK_BLUE)
QUBODUP_SOUND_TEXT = SMALLEST_FONT.render("'Well Done'", True, BLACK)
CONGUS_TEXT = SMALLER_FONT.render("congusbongus - opengameart.org/users/congusbongus", True, DARK_BLUE)
CONGUS_MUSIC_TEXT = SMALLEST_FONT.render("'New Thing Get!'", True, BLACK)
ERIC_TEXT = SMALLER_FONT.render("Music by Eric Matyas - soundimage.org", True, DARK_BLUE)
ERIC_MUSIC_TEXT = SMALLEST_FONT.render("'Steamtech Mayhem', 'High Altitude Station'", True, BLACK)
MATTHEW_TEXT = SMALLER_FONT.render("Music by Matthew Pablo - matthewpablo.com", True, DARK_BLUE)
MATTHEW_MUSIC_TEXT = SMALLEST_FONT.render("'Space Dimensions (8bit/Retro Version)', 'Orbital Colossus'", True, BLACK)
MAXSTACK_TEXT = SMALLER_FONT.render("maxstack - opengameart.org/users/maxstack", True, DARK_BLUE)
MAXSTACK_MUSIC_TEXT = SMALLEST_FONT.render("'Through Space'", True, BLACK)
ROBIN_TEXT = SMALLER_FONT.render("Robin Lamb - opengameart.org/users/robin-lamb",True, DARK_BLUE)
ROBIN_SOUND_TEXT = SMALLEST_FONT.render("'Lose Game Music'", True, BLACK)
IMAGES_ANIMATIONS_TEXT = SMALL_FONT.render("IMAGES & ANIMATIONS", True, DARK_RED)
RAWDANITSU_TEXT = SMALLER_FONT.render("RawDanitsu - opengameart.org/users/rawdanitsu", True, DARK_BLUE)
RAWDANITSU_IMAGE_TEXT = SMALLEST_FONT.render("'Space Background - 'Image4', 'Image6'", True, BLACK)
KENNEY_TEXT = SMALLER_FONT.render("Kenney Vleugels - kenney.nl", True, DARK_BLUE)
KENNEY_IMAGE_TEXT1 = SMALLEST_FONT.render("'Space Shooter Redux', 'Space Shooter Extension',", True, BLACK)
KENNEY_IMAGE_TEXT2 = SMALLEST_FONT.render("'Space Shooter Graphics'", True, BLACK)
FOOZLE_TEXT = SMALLER_FONT.render("Foozle - foozleacc.itch.io", True, DARK_BLUE)
FOOZLE_IMAGE_TEXT = SMALLEST_FONT.render("'Void Main Ship'", True, BLACK)
