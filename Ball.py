"""class ball by TOMER"""

from pygame import sprite, draw
from globals import *


class Ball(sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int, speed: float):
        super(Ball, self).__init__()
        self.__speed_x = speed
        self.__speed_y = speed
        self.__x = x
        self.__y = y
        self.__radius = radius

    def draw(self):
        draw.circle(main_window.window, Color.RED.value, [self.__x, self.__y], self.__radius)

    def move(self):
        tmp_x = self.__x + self.__speed_x
        tmp_y = self.__y + self.__speed_y

        if tmp_x < 10 + self.__radius:
            self.__speed_x = -self.__speed_x
        elif tmp_y < 10 + self.__radius or tmp_y > main_window.height - 10 - self.__radius:
            self.__speed_y = -self.__speed_y
        elif tmp_x + self.__radius > main_window.width - 10:
            self.__speed_x = -self.__speed_x
        else:
            self.__x = tmp_x
            self.__y = tmp_y
