# HighScores class

# pygame imports
import pygame
from pygame import Surface

# Import required global vars
from util.Globals import WIDTH, HEIGHT, HIGHSCORES_TITLE_TEXT, RETURN_TO_MENU_TEXT, SMALL_FONT, BLACK, WHITE, GOLD

# Other imports
# Uses json file to keep highscores
import json


class HighScoresPage:
    def __init__(self, file="highscores.json"):
        self.__file = file  # Highscores file variable
        self.__scores = self.load_scores()  # Highscores list

        # Rect for transparent surface measurements
        self.__rect = pygame.Rect(605, 180, WIDTH - 1150, HEIGHT - 330)
        # Transparent surface
        self.__transparent_surface = pygame.Surface((self.__rect.width, self.__rect.height), pygame.SRCALPHA)

    # Method to load highscores from the json file
    def load_scores(self):
        try:
            with open(self.__file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print("Highscores file not found!")
            return []

    # Method to save current highscores to the json file
    def save_scores(self):
        with open(self.__file, "w") as file:
            json.dump(self.__scores, file)

    # Method to add new highscore to the list
    def add_highscore(self, name, score):
        # Add highscore with given name and score
        self.__scores.append({"name": name, "score": score})
        # Sort scores by descending order
        self.__scores = sorted(self.__scores, key=lambda x: x["score"], reverse=True)
        # Keep only top 10 scores
        self.__scores = self.__scores[:10]
        # Save scores to the file
        self.save_scores()
        # Update scores list to show correct new highscores
        self.__scores = self.load_scores()

    # Method to check if given score is eligible to be added to highscores
    def is_highscore(self, score):
        # If there are less than 10 highscores in the list - eligible
        if len(self.__scores) < 10:
            return True
        else:
            # Otherwise check lowest score
            lowest_score = min(self.__scores, key=lambda x: x["score"])
            # If given score is higher than the lowest score in highscores - eligible
            return score > lowest_score["score"]

    # Method to draw highscores page objects
    def draw(self, screen: Surface):
        # Transparent white color for the surface
        transparent_white = (*WHITE, 150)
        # Fill the transparent surface with the color
        self.__transparent_surface.fill(transparent_white)

        # Render the transparent surface
        screen.blit(self.__transparent_surface, (self.__rect.x, self.__rect.y))

        # Highscores title
        highscores_title_rect = (WIDTH / 2 - 140, HEIGHT / 2 - 400)
        screen.blit(HIGHSCORES_TITLE_TEXT, highscores_title_rect)

        # Highscores list
        for index, score in enumerate(self.__scores):
            # Font color
            color = BLACK
            # First place text is gold
            if index == 0:
                color = GOLD
            # Current highscore text
            score_text = (SMALL_FONT.render
                          (f"{index + 1}) {score["name"]} - {score["score"]}", True, color))
            screen.blit(score_text, (WIDTH / 2 - 100, HEIGHT / 2 - 280 + index * 60))

        # Informative text to let users know exiting highscores page is by pressing ESCAPE
        return_to_menu_rect = (WIDTH / 2 - 225, HEIGHT / 2 + 370)
        screen.blit(RETURN_TO_MENU_TEXT, return_to_menu_rect)

        # Update the display
        pygame.display.update()
