# Quit menu class

# pygame imports
import pygame
from pygame import Surface

# Import required global vars
from util.Globals import WIDTH, HEIGHT, WHITE, DARK_RED, LIGHT_RED, QUIT_TEXT, QUIT_MENU_TEXT, CONTINUE_TEXT


class QuitMenu:
    # Constructor
    def __init__(self, screen):
        self.screen: Surface = screen  # Set the screen's resolution to be the same as game's
        self.clock = pygame.time.Clock()  # pygame's Clock module for fps management
        self.game_is_quitting = True  # Boolean to determine if the game is in quit menu_music
        self.quit_menu_text = QUIT_MENU_TEXT  # Quit menu_music title text
        self.continue_text = CONTINUE_TEXT  # Resume button text
        self.quit_text = QUIT_TEXT  # Quit button text
        self.background_rect = pygame.Rect(WIDTH / 2 - 230, HEIGHT / 2 - 150, 460, 330)  # Background
        self.continue_button_rect = pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 - 40, 190, 50)  # Resume button
        self.quit_button_rect = pygame.Rect(WIDTH / 2 - 95, HEIGHT / 2 + 70, 190, 50)  # Quit button

    # Run method
    # This method runs the main loop and all other methods
    def run(self):
        while self.game_is_quitting:
            mouse_pos = pygame.mouse.get_pos()  # Get mouse position
            self.draw(mouse_pos)
            self.clock.tick(60)  # Set FPS to 60
            action = self.handle_events(mouse_pos)  # Get action string returned from handle_events
            if action:
                return action  # Return the action

    # Method to handle user events
    def handle_events(self, mouse_pos):
        for event in pygame.event.get():
            # Quitting by pressing X button
            if event.type == pygame.QUIT:
                self.game_is_quitting = False
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Resume button clicked - resume the game
                if self.continue_button_rect.collidepoint(mouse_pos):
                    self.game_is_quitting = False  # Disable quit menu_music
                    return "continue"  # Return "continue" to continue playing
                # Quit button clicked - quit the game and return to menu
                if self.quit_button_rect.collidepoint(mouse_pos):
                    self.game_is_quitting = False  # Disable quit menu_music
                    return "quit"  # Return "quit" to quit the game
            if event.type == pygame.KEYDOWN:
                # ESC key pressed
                if event.key == pygame.K_ESCAPE:
                    self.game_is_quitting = False  # Disable quit menu_music
                    return "continue"  # Return "continue" to resume the game

    # Method to draw all quit menu objects
    def draw(self, mouse_pos):
        # Size of the background rect
        background = pygame.Surface((self.background_rect.width, self.background_rect.height))
        # Alpha level for transparency
        background.set_alpha(20)
        # Fill the surface with color
        background.fill(WHITE)
        # Render it to the screen
        self.screen.blit(background, (self.background_rect.x, self.background_rect.y))

        # Render and position the "QUIT GAME?" text over all buttons
        quit_menu_text_pos = (WIDTH / 2 - self.quit_menu_text.get_width() / 2, HEIGHT / 2 - 150)
        self.screen.blit(self.quit_menu_text, quit_menu_text_pos)

        # Buttons:
        # All buttons change color when hovered over

        # Continue button
        if self.continue_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, DARK_RED, self.continue_button_rect)
        else:
            pygame.draw.rect(self.screen, LIGHT_RED, self.continue_button_rect)
        # Continue text
        self.screen.blit(self.continue_text, (WIDTH / 2 - 85, HEIGHT / 2 - 34))

        # Quit button
        if self.quit_button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.screen, DARK_RED, self.quit_button_rect)
        else:
            pygame.draw.rect(self.screen, LIGHT_RED, self.quit_button_rect)
        # Quit text
        self.screen.blit(self.quit_text, (WIDTH / 2 - 85, HEIGHT / 2 + 76))

        pygame.display.update()  # Update the display
