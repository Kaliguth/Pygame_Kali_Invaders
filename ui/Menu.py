# Menu class

# pygame imports
import pygame
from pygame import Surface

# Object imports
from game.Game import Game
from ui.HighScoresPage import HighScoresPage
from ui.CreditsPage import CreditsPage

# Import required global vars
from util.Globals import (WIDTH, HEIGHT, MENU_BG, WHITE, DARK_GREY, LIGHT_GREY, DARK_RED, LIGHT_RED, LIGHT_RED_2,
                          DARK_GREEN, LIGHT_GREEN, DARK_BLUE, LIGHT_BLUE, DARK_ORANGE, LIGHT_ORANGE,
                          SMALL_FONT, TITLE_TEXT, START_TEXT, HIGHSCORES_TEXT, QUIT_TEXT, CREDITS_TEXT,
                          DIFFICULTY_TEXT, EASY_TEXT, MEDIUM_TEXT, HARD_TEXT, COLOR_TEXT, TYPE_TEXT,
                          RED_TEXT, GREEN_TEXT, BLUE_TEXT, ORANGE_TEXT, TYPE_ONE_TEXT, TYPE_TWO_TEXT, TYPE_THREE_TEXT,
                          CONTROLS_TEXT, MOVE_KEY_TEXT, SHOOT_KEY_TEXT, PAUSE_KEY_TEXT)

# Other imports
import random


class Menu:
    # Constructor
    def __init__(self):
        self.clock = pygame.time.Clock()  # pygame's Clock module for fps management
        self.screen: Surface = pygame.display.set_mode((WIDTH, HEIGHT))  # Set window resolution
        self.game_is_running = True  # Boolean to determine if the game app is running
        self.start_text_visible = True  # Boolean to determine when start text is visible (for blinking)
        self.showing_highscores = False  # Boolean to determine if highscores page is displayed
        self.showing_credits = False  # Boolean to determine if credits page is displayed
        self.blink_counter = 0  # Counter to manage start text blinking

        # Transparent rect under start text
        # Rect for transparent surface measurements
        self.__start_rect = pygame.Rect(600, 368, WIDTH - 1190, HEIGHT - 895)
        # Transparent surface
        self.__start_transparent_surface = pygame.Surface(
            (self.__start_rect.width, self.__start_rect.height), pygame.SRCALPHA)

        # Transparent rect under controls text
        # Rect for transparent surface measurements
        self.__controls_rect = pygame.Rect(580, 720, WIDTH - 1140, HEIGHT - 750)
        # Transparent surface
        self.__controls_transparent_surface = pygame.Surface((
            self.__controls_rect.width, self.__controls_rect.height), pygame.SRCALPHA)

        # Button rects
        self.buttons = [
            # Difficulty buttons rects
            {"rect": pygame.Rect(WIDTH / 2 + 400, HEIGHT / 2 + 30, 190, 50),
             "color": LIGHT_GREEN, "hover_color": DARK_GREEN},
            {"rect": pygame.Rect(WIDTH / 2 + 400, HEIGHT / 2 + 130, 190, 50),
             "color": LIGHT_ORANGE, "hover_color": DARK_ORANGE},
            {"rect": pygame.Rect(WIDTH / 2 + 400, HEIGHT / 2 + 230, 190, 50),
             "color": LIGHT_RED_2, "hover_color": DARK_RED},
            # Spaceship selection buttons rects:
            # Colors
            {"rect": pygame.Rect(WIDTH / 2 - 700, HEIGHT / 2 + 10, 190, 50),
             "color": LIGHT_RED_2, "hover_color": DARK_RED},
            {"rect": pygame.Rect(WIDTH / 2 - 500, HEIGHT / 2 + 10, 190, 50),
             "color": LIGHT_GREEN, "hover_color": DARK_GREEN},
            {"rect": pygame.Rect(WIDTH / 2 - 700, HEIGHT / 2 + 110, 190, 50),
             "color": LIGHT_BLUE, "hover_color": DARK_BLUE},
            {"rect": pygame.Rect(WIDTH / 2 - 500, HEIGHT / 2 + 110, 190, 50),
             "color": LIGHT_ORANGE, "hover_color": DARK_ORANGE},
            # Types
            {"rect": pygame.Rect(WIDTH / 2 - 640, HEIGHT / 2 + 245, 70, 50),
             "color": LIGHT_GREY, "hover_color": DARK_GREY},
            {"rect": pygame.Rect(WIDTH / 2 - 540, HEIGHT / 2 + 245, 70, 50),
             "color": LIGHT_GREY, "hover_color": DARK_GREY},
            {"rect": pygame.Rect(WIDTH / 2 - 440, HEIGHT / 2 + 245, 70, 50),
             "color": LIGHT_GREY, "hover_color": DARK_GREY},
            # Highscores button rect
            {"rect": pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 + 20, 210, 50),
             "color": DARK_RED, "hover_color": LIGHT_RED},
            # Quit button rect
            {"rect": pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 + 120, 210, 50),
             "color": DARK_RED, "hover_color": LIGHT_RED},
            # Credits button rect
            {"rect": pygame.Rect(WIDTH - 220, 10, 210, 50),
             "color": DARK_RED, "hover_color": LIGHT_RED}
        ]

        # Spaceship selection variables
        # Starts as default spaceship - red type 1
        self.__spaceship_color = "red"
        self.__spaceship_type = 1

        # Difficulty selection variable
        # Starts as default - easy
        self.__difficulty = "easy"

        pygame.display.set_caption("Kali Invaders")  # App caption text (displayed in top left of the window)

        # Music
        # BGM files list
        self.menu_bgm_list = [
            "music/menu_music/high_altitude_station.ogg",
            "music/menu_music/steamtech_mayhem.ogg",
            "music/menu_music/through-space.ogg",
        ]
        self.menu_bgm = None  # Variable for menu BGM
        self.play_random_music()  # Play random BGM from the list

        self.run()  # Run the menu's main method

    # Method to play random background music
    def play_random_music(self):
        # Choose random BGM from the list
        chosen_bgm = random.choice(self.menu_bgm_list)
        # Change BGM variable to chosen music file
        self.menu_bgm = pygame.mixer.Sound(chosen_bgm)
        # Play the chosen music endlessly
        self.menu_bgm.play(loops=-1)

    # Run method
    # This method runs the main loop and all other methods
    def run(self):
        while self.game_is_running:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position

            # If highscore button was clicked - show highscores page
            if self.showing_highscores:
                # This stays True until player exits highscores page by pressing ESCAPE
                self.show_highscores()
            # If credits button was clicked - show credits page
            elif self.showing_credits:
                # This stays True until player exits credits page by pressing ESCAPE
                self.show_credits()
            # Otherwise show menu
            else:
                self.draw_menu(mouse_pos)
                self.start_text_blink()

            self.handle_events(mouse_pos)  # Check for user event
            self.clock.tick(60)  # Set FPS to 60

    # Method to handle user events (mouse clicks and button presses)
    def handle_events(self, mouse_pos):
        for event in pygame.event.get():
            # Quitting by pressing window's X button
            if event.type == pygame.QUIT:
                self.game_is_running = False
            # Mouse click events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Go over all menu buttons
                for button in self.buttons:
                    # If current button was clicked - check which button it is
                    if button["rect"].collidepoint(mouse_pos):
                        # Easy button - change to easy difficulty
                        if button == self.buttons[0]:
                            self.__difficulty = "easy"
                        # Medium button - change to medium difficulty
                        if button == self.buttons[1]:
                            self.__difficulty = "medium"
                        # Hard button - change to hard difficulty
                        if button == self.buttons[2]:
                            self.__difficulty = "hard"
                        # Red button - change spaceship color to red
                        if button == self.buttons[3]:
                            self.__spaceship_color = "red"
                        # Green button - change spaceship color to green
                        if button == self.buttons[4]:
                            self.__spaceship_color = "green"
                        # Blue button - change spaceship color to blue
                        if button == self.buttons[5]:
                            self.__spaceship_color = "blue"
                        # Orange button - change spaceship color to orange
                        if button == self.buttons[6]:
                            self.__spaceship_color = "orange"
                        # Type 1 button - change spaceship type to type 1
                        if button == self.buttons[7]:
                            self.__spaceship_type = 1
                        # Type 2 button - change spaceship type to type 2
                        if button == self.buttons[8]:
                            self.__spaceship_type = 2
                        # Type 3 button - change spaceship type to type 3
                        if button == self.buttons[9]:
                            self.__spaceship_type = 3
                        # Highscores button - show highscores screen
                        if button == self.buttons[10]:
                            self.showing_highscores = True
                        # Quit button - quit the game
                        if button == self.buttons[11]:
                            self.game_is_running = False
                        # Credits button - show credits screen
                        if button == self.buttons[12]:
                            self.showing_credits = True
            # Key press events
            elif event.type == pygame.KEYDOWN:
                # ENTER pressed - start the game
                if event.key == pygame.K_RETURN:
                    self.start_game()
                # ESCAPE pressed - close highscores or credits page (if displayed)
                if event.key == pygame.K_ESCAPE:
                    self.showing_highscores = False
                    self.showing_credits = False

    # Method to show highscores page
    def show_highscores(self):
        # Cover the screen with the background
        self.screen.blit(MENU_BG, [0, 0])
        # Create new highscores page object and display it on screen
        highscores_page = HighScoresPage()
        highscores_page.draw(self.screen)

    # Method to show highscores page
    def show_credits(self):
        # Cover the screen with the background
        self.screen.blit(MENU_BG, [0, 0])
        # Create new credits page object and display it on screen
        credits_page = CreditsPage()
        credits_page.draw(self.screen)

    # Method to start a new game
    def start_game(self):
        # Stop the menu music
        self.menu_bgm.stop()
        # Create a new game object
        new_game = Game(self.screen, self.__spaceship_color, self.__spaceship_type, self.__difficulty)
        # Runs the game's run method
        new_game.run_game()
        # When game ends or exited (returned to main menu)
        self.play_random_music()  # Randomize and play music again

    # Method to manage start text blinking
    def start_text_blink(self):
        # Add 1 to the blink counter (counts frames)
        self.blink_counter += 1
        # Blink the start text every 30 frames (around every 1 second)
        if self.blink_counter >= 30:
            # Change start_text_visible to True or False (depending on current status)
            self.start_text_visible = not self.start_text_visible
            self.blink_counter = 0  # Restart blink counter

    # Method to draw/render all menu objects
    def draw_menu(self, mouse_pos):
        # Screen background fill
        self.screen.blit(MENU_BG, [0, 0])

        # Buttons render
        # Goes through all buttons in the buttons list and draws them on screen
        # Each button gets the colors assigned to it in the list
        for button in self.buttons:
            if button["rect"].collidepoint(mouse_pos):
                pygame.draw.rect(self.screen, button["hover_color"], button["rect"])
            else:
                pygame.draw.rect(self.screen, button["color"], button["rect"])

        # Texts:

        # Title text
        title_text_pos = (WIDTH / 2 - 190, HEIGHT / 2 - 300)
        self.screen.blit(TITLE_TEXT, title_text_pos)

        # Transparent rect under start text
        # Transparent white color for the surface
        transparent_white = (*WHITE, 150)
        # Fill the transparent surface with the color
        self.__start_transparent_surface.fill(transparent_white)
        # Render the transparent surface
        self.screen.blit(self.__start_transparent_surface, (self.__start_rect.x, self.__start_rect.y))

        # Start text render (only if start_text_visible is true)
        start_text_pos = (WIDTH / 2 - 140, HEIGHT / 2 - 100)
        if self.start_text_visible:
            self.screen.blit(START_TEXT, start_text_pos)

        # Transparent rect under controls text
        # Fill the transparent surface with the color
        self.__controls_transparent_surface.fill(transparent_white)
        # Render the transparent surface
        self.screen.blit(self.__controls_transparent_surface, (self.__controls_rect.x, self.__controls_rect.y))

        # Controls texts render:
        # Title
        controls_text_pos = (WIDTH / 2 - 80, HEIGHT / 2 + 250)
        self.screen.blit(CONTROLS_TEXT, controls_text_pos)
        # Keys
        move_key_text_pos = (WIDTH / 2 - 150, HEIGHT / 2 + 300)
        self.screen.blit(MOVE_KEY_TEXT, move_key_text_pos)
        shoot_key_text_pos = (WIDTH / 2 - 150, HEIGHT / 2 + 350)
        self.screen.blit(SHOOT_KEY_TEXT, shoot_key_text_pos)
        pause_key_text_pos = (WIDTH / 2 - 150, HEIGHT / 2 + 400)
        self.screen.blit(PAUSE_KEY_TEXT, pause_key_text_pos)

        # Highscores text
        highscores_text_pos = (WIDTH / 2 - 85, HEIGHT / 2 + 25)
        self.screen.blit(HIGHSCORES_TEXT, highscores_text_pos)

        # Quit text
        quit_text_pos = (WIDTH / 2 - 25, HEIGHT / 2 + 125)
        self.screen.blit(QUIT_TEXT, quit_text_pos)

        # Spaceship selection texts:

        # Spaceship color text
        color_text_pos = (WIDTH / 2 - 640, HEIGHT / 2 - 55)
        self.screen.blit(COLOR_TEXT, color_text_pos)
        # Color texts for buttons
        red_text_pos = (WIDTH / 2 - 635, HEIGHT / 2 + 15)
        self.screen.blit(RED_TEXT, red_text_pos)
        green_text_pos = (WIDTH / 2 - 455, HEIGHT / 2 + 15)
        self.screen.blit(GREEN_TEXT, green_text_pos)
        blue_text_pos = (WIDTH / 2 - 640, HEIGHT / 2 + 115)
        self.screen.blit(BLUE_TEXT, blue_text_pos)
        orange_text_pos = (WIDTH / 2 - 465, HEIGHT / 2 + 115)
        self.screen.blit(ORANGE_TEXT, orange_text_pos)

        # Spaceship type text
        type_text_pos = (WIDTH / 2 - 627, HEIGHT / 2 + 185)
        self.screen.blit(TYPE_TEXT, type_text_pos)
        # Type texts for buttons
        type_one_pos = (WIDTH / 2 - 613, HEIGHT / 2 + 250)
        self.screen.blit(TYPE_ONE_TEXT, type_one_pos)
        type_two_pos = (WIDTH / 2 - 513, HEIGHT / 2 + 250)
        self.screen.blit(TYPE_TWO_TEXT, type_two_pos)
        type_three_pos = (WIDTH / 2 - 413, HEIGHT / 2 + 250)
        self.screen.blit(TYPE_THREE_TEXT, type_three_pos)

        # Spaceship image for selection
        # Changes based on clicks on color and type buttons
        spaceship_image = (pygame.image.load
                           (f"player/spaceships/spaceship{self.__spaceship_type}_{self.__spaceship_color}.png"))
        spaceship_image = pygame.transform.scale(spaceship_image, (99, 75))
        spaceship_rect = spaceship_image.get_rect()
        spaceship_rect.center = (WIDTH / 2 - 510, HEIGHT / 2 + 380)
        self.screen.blit(spaceship_image, spaceship_rect)

        # Difficulty texts:

        # Choose difficulty text
        difficulty_text_pos = (WIDTH / 2 + 350, HEIGHT / 2 - 55)
        self.screen.blit(DIFFICULTY_TEXT, difficulty_text_pos)
        # Easy
        easy_text_pos = (WIDTH / 2 + 450, HEIGHT / 2 + 35)
        self.screen.blit(EASY_TEXT, easy_text_pos)
        # Medium
        medium_text_pos = (WIDTH / 2 + 437, HEIGHT / 2 + 135)
        self.screen.blit(MEDIUM_TEXT, medium_text_pos)
        # Hard
        hard_text_pos = (WIDTH / 2 + 455, HEIGHT / 2 + 235)
        self.screen.blit(HARD_TEXT, hard_text_pos)
        # Current difficulty text
        current_difficulty_pos = (WIDTH / 2 + 345, HEIGHT / 2 + 335)
        self.screen.blit(SMALL_FONT.render(
            f"Current difficulty: {self.__difficulty}", True, WHITE), current_difficulty_pos)

        # Credits text for credits button
        credits_text_pos = (WIDTH - 180, 15)
        self.screen.blit(CREDITS_TEXT, credits_text_pos)

        # Update the display
        pygame.display.update()
