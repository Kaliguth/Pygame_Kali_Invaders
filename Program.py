# Main file to initiate the game

# pygame imports
import pygame
from pygame import mixer

# UI imports
from ui.Menu import Menu

if __name__ == '__main__':
    pygame.init()  # Initiate pygame
    mixer.init()  # Initiate mixer
    Menu()  # Run Menu
    pygame.quit()  # Turn off pygame when leaving menu
