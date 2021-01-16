"""
This file is for global variables needed throughout the game
"""
import pygame

from enum import Enum
class Color(Enum):
    """
    Color enum that represents pygame colors.
    """
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
    """
    Windows class that represents pygame window
    """
    def __init__(self, width, height):
        """

        :param width: width of the window
        :type width: int
        :param height: height of the window
        :type height: int
        """
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width,height))

# the global window variable.
main_window = Window(400, 300)