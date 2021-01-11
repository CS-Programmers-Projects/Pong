"""
This file is for global variables needed throughout the game
"""
import pygame

from enum import Enum
class Color(Enum):
    BLACK = (0,0,0)
    BLUE = (0, 0, 128)
    GREEN = (0, 200, 0)
    WHITE = (255, 255, 255)
    SHADOW = (192, 192, 192)
    LIGHTBLUE = (0, 0, 255)
    RED = (200, 0, 0)
    LIGHTRED = (255, 100, 100)
    PURPLE = (102, 0, 102)
    LIGHTPURPLE = (153, 0, 153)


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))

main_window = Window(400, 300)