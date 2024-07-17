# Game class

# pygame imports
import pygame
from pygame import Surface
# Object imports
from player.Player import Player
from enemies.Enemy import Enemy
from enemies.EnemyLines import EnemyLines
from ui.HighScoresPage import HighScoresPage

# Logic imports
from logic.PlayerLogic import PlayerLogic

# UI imports
from ui.PauseMenu import PauseMenu
from ui.QuitMenu import QuitMenu

# Import required global vars
from util.Globals import (
    WIDTH, HEIGHT, GAME_BG, WHITE, BLACK, GOLD, SMALL_FONT, TITLE_FONT, HUGE_FONT, GAME_OVER_TEXT, YOU_WIN_TEXT)

# Other imports
import random


class Game:
    # Constructor
    def __init__(self, screen, spaceship_color, spaceship_type, difficulty):
        self.screen: Surface = screen  # Set the screen's resolution to be the same as menu_music's
        self.__spaceship_color = spaceship_color  # Spaceship color variable
        self.__spaceship_type = spaceship_type  # Spaceship type variable
        self.clock = pygame.time.Clock()  # pygame's Clock module for fps management
        self.game_in_progress = True  # Boolean to determine if the game is in progress
        self.game_is_paused = False  # Boolean to determine if the game is paused
        self.game_is_quitting = False  # Boolean to determine if player clicked X or QUIT button
        self.player_entry_complete = False  # Boolean to determine when player entry animation is complete
        self.countdown = 3  # Variable for countdown before game starts

        # Enemy speed based on difficulty
        # The difficulty text variable is used for restarting the game in the same difficulty
        # The enemy speed variable determines enemies' speed to pass over to the enemy lines object
        self.__difficulty_text = difficulty
        if self.__difficulty_text == "easy":
            self.__enemy_speed = 1
        elif self.__difficulty_text == "medium":
            self.__enemy_speed = 3
        elif self.__difficulty_text == "hard":
            self.__enemy_speed = 6
        else:
            self.__enemy_speed = 1

        # Enemies list, enemy lines and player Objects
        self.__enemies = []  # Enemies list for enemy lines
        self.load_enemies()  # Load enemies into enemies list
        self.__player = (
            Player(WIDTH / 2, HEIGHT + 80, 99, 75,
                   self.__spaceship_type, self.__spaceship_color))  # Game's player object with chosen color and type
        self.__enemy_lines = EnemyLines(self.__enemies, self.__player, self.__enemy_speed)  # Game's enemy lines object

        # Score and health bar parameters
        self.__life_icon = pygame.image.load('player/effects/life.png')
        self.__bar_height = 50
        self.__bar_color = (50, 50, 50)
        self.__bar_rect = pygame.Rect(0, 0, WIDTH, self.__bar_height)

        # Logics
        self.__player_logic = PlayerLogic(self.__player)  # Player logic object
        self.__highscores = HighScoresPage()  # Highscores page object for checking and adding highscores

        # Music
        # BGM files list
        self.game_bgm_list = [
            "music/game_music/dimensions.ogg",
            "music/game_music/orbital_colossus.ogg",
        ]
        self.game_bgm = None  # Variable for game BGM
        self.play_random_music()  # Load random music from list into the object

        # Play spaceship engine sound every new game
        spaceship_start = pygame.mixer.Sound("sound_effects/spaceship/rocket_launch.ogg")
        spaceship_start.set_volume(0.5)
        spaceship_start.play()

    # Method to play random background music
    def play_random_music(self):
        # Choose random BGM from the list
        chosen_bgm = random.choice(self.game_bgm_list)
        # Change BGM variable to chosen music file
        self.game_bgm = pygame.mixer.Sound(chosen_bgm)
        # Set BGM volume to 30%
        self.game_bgm.set_volume(0.3)
        # Play the chosen music endlessly
        self.game_bgm.play(loops=-1)

    # Method to load enemies into enemies list
    def load_enemies(self):
        # 27 enemies
        for enemy in range(0, 27):
            # New enemy object
            new_enemy = Enemy(50, 50)
            # Add the enemy object into the list
            self.__enemies.append(new_enemy)

    # Run method
    # This method runs the main loop and all other methods
    def run_game(self):
        while self.game_in_progress:
            # Handle user events and draw game object each iteration
            self.handle_events()
            self.draw_game_objects()
            # If player entry animation is not complete - keep playing it
            if not self.player_entry_complete:
                self.player_entry()
            # Countdown before game starts
            elif self.countdown > 0:
                self.display_countdown()
            # If game is not paused or quitting - handle game logic events
            elif not (self.game_is_paused or self.game_is_quitting):
                self.handle_game_logic()
            # If X button clicked - open quit menu
            elif self.game_is_quitting:
                self.quit_menu()
            # If game is paused - open pause menu
            elif self.game_is_paused:
                self.pause_menu()

            self.clock.tick(60)  # Set FPS to 60

            # If all enemies destroyed - display you win screen
            if self.__enemy_lines.is_empty():
                self.show_you_win()
            # If player health reached 0 - display game over screen
            if self.__player.health == 0:
                self.show_game_over()

    # Method to handle user events (mouse clicks and button presses)
    def handle_events(self):
        for event in pygame.event.get():
            # Will not handle events while countdown is in progress
            if self.countdown == 0:
                # If X button is clicked - change boolean to open quit menu
                if event.type == pygame.QUIT:
                    self.game_is_quitting = True
                # Key press events
                if event.type == pygame.KEYDOWN:
                    # ESCAPE is pressed - change boolean to open pause menu
                    if event.key == pygame.K_ESCAPE:
                        self.game_is_paused = True
                    # EASTER EGG FOR CODERS!
                    # Win by pressing DELETE (initially used for testing)
                    if event.key == pygame.K_DELETE:
                        self.show_you_win()

    # Method to handle all game logics
    def handle_game_logic(self):
        keys = pygame.key.get_pressed()  # Variable for key inputs list
        # If left key is pressed - spaceship moves left
        if keys[pygame.K_LEFT]:
            self.__player_logic.move_left()
        # If right key is pressed - paddle moves right
        if keys[pygame.K_RIGHT]:
            self.__player_logic.move_right()
        # If space key is pressed - player shoots a projectile
        if keys[pygame.K_SPACE]:
            self.__player_logic.shoot()

        # Update the player's spaceship and enemy lines status
        self.__player.update()
        self.__enemy_lines.update()

    # Method to animate the player's spaceship into the screen from below
    def player_entry(self):
        # Check if spaceship has reached the correct position
        if self.__player.spaceship_rect.y > HEIGHT - 115:
            # Set player's moving status for engine animation
            self.__player.moving = True
            # Move player's spaceship one pixel up as long as not in the correct position
            self.__player.spaceship_rect.y -= 1
            # Move player's spaceship's engine one pixel up as long as not in the correct position
            self.__player.engine_rect.y -= 1
        else:
            # If reached correct position - change the boolean to let the game know the game can start
            self.player_entry_complete = True

    # Method to display the countdown before game starts
    def display_countdown(self):
        # Countdown text render (This cannot be in global variables file because it is not static and text changes)
        countdown_text = HUGE_FONT.render(str(self.countdown), True, BLACK)
        # Draw/render the countdown text in the middle of the screen
        self.screen.blit(countdown_text,
                         (WIDTH / 2 - countdown_text.get_width() / 2, HEIGHT / 2 - countdown_text.get_height() / 2))

        pygame.display.update()  # Update the display
        pygame.time.delay(1000)  # One-second delay between numbers
        self.countdown -= 1  # Decrement countdown number by 1 (this runs until countdown is 0)

    # Method to display pause menu
    def pause_menu(self):
        pause_menu = PauseMenu(self.screen)  # New pause menu object

        action = pause_menu.run()  # Collect the action returned from the pause menu run method
        # If Resume button clicked - change the pause boolean to resume the game
        if action == "resume":
            self.game_is_paused = False
        # If Restart button clicked - start a new game
        elif action == "restart":
            self.game_bgm.stop()  # Stop the current game music
            # Restart the game
            self.__init__(self.screen, self.__spaceship_color, self.__spaceship_type, self.__difficulty_text)
        # If Quit button clicked - change the game running boolean to quit the game
        elif action == "quit":
            self.game_bgm.stop()  # Stop the game music
            self.game_in_progress = False

    # Method to display quit menu
    def quit_menu(self):
        quit_menu = QuitMenu(self.screen)  # New quit menu object

        action = quit_menu.run()  # Collect the action returned from the quit menu run method
        # If Continue button clicked - change the quitting boolean to resume the game
        if action == "continue":
            self.game_is_quitting = False
        # If Quit button clicked - change the game running boolean to quit the game
        elif action == "quit":
            self.game_bgm.stop()  # Stop the game music
            self.game_in_progress = False

    # Method to show the player's score at the end of the game
    def show_score(self):
        score_text = TITLE_FONT.render(f"Your score: {self.__player.score}", True, WHITE)
        score_text_rect = score_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.screen.blit(score_text, score_text_rect)

    # Method to display game over screen
    def show_game_over(self):
        # Hide all objects by filling the background again
        self.screen.blit(GAME_BG, [0, 0])
        # Stop the game music
        self.game_bgm.stop()

        # Play a loss sound
        loss_sound = pygame.mixer.Sound("sound_effects/sounds/lose.ogg")
        loss_sound.play()

        # Render big game over text in the middle of the screen
        game_over_text_rect = GAME_OVER_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 150))
        self.screen.blit(GAME_OVER_TEXT, game_over_text_rect)

        # Render the player's score on the screen
        self.show_score()

        # Update the display
        pygame.display.update()
        # Display for 4 seconds
        pygame.time.delay(4000)
        # Change the game running boolean to quit the game
        self.game_in_progress = False

    # Method to display you win screen
    def show_you_win(self):
        # Hide all objects by filling the background again
        self.screen.blit(GAME_BG, [0, 0])
        # Stop the game music
        self.game_bgm.stop()

        # Render big you win text in the middle of the screen
        you_win_text_rect = YOU_WIN_TEXT.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 200))
        self.screen.blit(YOU_WIN_TEXT, you_win_text_rect)

        # Render the player's score on the screen
        self.show_score()

        # If the player's score is a new highscore
        if self.__highscores.is_highscore(self.__player.score):
            # Play a highscore sound
            highscore_sound = pygame.mixer.Sound("sound_effects/sounds/highscore.ogg")
            highscore_sound.play()
            # Render informative texts on the screen
            highscore_text = TITLE_FONT.render("Congratulations! You got a HIGHSCORE!", True, GOLD)
            highscore_text_rect = highscore_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 90))
            self.screen.blit(highscore_text, highscore_text_rect)
            enter_name_text = SMALL_FONT.render("Please enter your name and press ENTER or ESC to cancel", True, WHITE)
            enter_name_text_rect = enter_name_text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + 180))
            self.screen.blit(enter_name_text, enter_name_text_rect)

            # Render a name text box rect
            input_box = pygame.Rect(WIDTH / 2 - 130, HEIGHT / 2 + 240, 300, 70)
            text = ""
            input_active = True

            # Loop until player presses ESCAPE to quit or ENTER to add the highscore
            while input_active:
                for event in pygame.event.get():
                    # Clicked X button - quit the game without submitting the highscore
                    if event.type == pygame.QUIT:
                        input_active = False
                        self.game_in_progress = False
                    # Key press events
                    elif event.type == pygame.KEYDOWN:
                        # If ESCAPE is pressed - cancel and don't submit the highscore
                        if event.key == pygame.K_ESCAPE:
                            input_active = False
                            self.game_in_progress = False
                        # If ENTER is pressed - submit the highscore and quit the game
                        elif event.key == pygame.K_RETURN:
                            # Add the highscore with inputted name
                            self.__highscores.add_highscore(text, self.__player.score)
                            input_active = False
                            self.game_in_progress = False
                        # If BACKSPACE is pressed - deletes characters from the input box
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        # Any other key pressed - adds pressed key's characters
                        else:
                            text += event.unicode

                # Fill the input box rect with white background
                self.screen.fill(WHITE, input_box)
                # Render a border for the input box
                pygame.draw.rect(self.screen, BLACK, input_box, 4)
                # Render a text area for the input box
                text_area = SMALL_FONT.render(text, True, BLACK)
                self.screen.blit(text_area, (input_box.x + 5, input_box.y + 5))

                # Update the display
                pygame.display.update()

        # If player's score is not a highscore
        else:
            # Play a win sound
            win_sound = pygame.mixer.Sound("sound_effects/sounds/win.ogg")
            win_sound.play()

        # Update the display
        pygame.display.update()
        # Display for 4 seconds
        pygame.time.delay(4000)
        # Change the game running boolean to quit the game
        self.game_in_progress = False

    # Method to draw all game objects
    def draw_game_objects(self):
        # Screen background fill
        self.screen.blit(GAME_BG, [0, 0])

        # Objects:
        # Render player's spaceship and enemy lines
        self.__player.draw(self.screen)
        self.__enemy_lines.draw(self.screen)

        # Score bar and health bar
        pygame.draw.rect(self.screen, self.__bar_color, self.__bar_rect)
        # Render score text (inside the bar)
        score_text = SMALL_FONT.render(f"Score: {self.__player.score}", True, WHITE)
        score_text_rect = score_text.get_rect(topleft=(5, self.__bar_height / 2 - 20))
        self.screen.blit(score_text, score_text_rect)
        # Render health text (inside the bar)
        health_text = SMALL_FONT.render("Health:", True, WHITE)
        health_text_rect = health_text.get_rect(center=(WIDTH - 300, self.__bar_height / 2))
        self.screen.blit(health_text, health_text_rect)
        # Render Health icons (inside the bar)
        # Initially 5 icons for 5 health
        # Changes according to player's health
        icon_x = health_text_rect.right
        icon_y = self.__bar_height / 2 - 15
        for i in range(self.__player.health):
            icon_rect = pygame.Rect(icon_x, icon_y, self.__life_icon.get_width(), self.__life_icon.get_height())
            self.screen.blit(self.__life_icon, icon_rect)
            icon_x += 50

        # Update the display
        pygame.display.update()
