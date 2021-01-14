"""class ball by TOMER"""

from pygame import sprite, draw
from globals import *
from Paddle import Paddle
import math


class Ball(sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int, speed: float):
        super(Ball, self).__init__()
        self.__start_x = x
        self.__start_y = y
        self.speed_x = speed
        self.speed_y = speed
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self):
        draw.circle(main_window.window, Color.RED.value, [self.x, self.y], self.radius)

    def move(self):
        tmp_x = self.x + self.speed_x
        tmp_y = self.y + self.speed_y

        if self.pass_player():
            self.speed_x = -self.speed_x
        elif tmp_y < 10 + self.radius:  # ceiling
            self.bounce('y')
        elif tmp_y > main_window.height - 10 - self.radius:  # floor
            self.bounce('y')
        elif tmp_x + self.radius > main_window.width - 10:
            self.bounce('x')
        else:
            self.x = tmp_x
            self.y = tmp_y

    def hit_paddle(self, paddle) -> bool:
        return math.sqrt((self.x - paddle.x) ** 2 + (self.y - paddle) ** 2) + self.radius < 10

    def hit_floor(self):
        tmp_y = self.y + self.speed_y
        if tmp_y > main_window.height - 10 - self.radius:
            self.bounce('y')

    def hit_ceiling(self):
        tmp_y = self.y + self.speed_y
        if tmp_y > main_window.height - 10 - self.radius:
            self.bounce('x')

    def pass_computer(self) -> bool:
        tmp_x = self.x + self.speed_x
        return tmp_x + self.radius > main_window.width - 10

    def pass_player(self) -> bool:
        tmp_x = self.x + self.speed_x
        return tmp_x < 10 + self.radius

    def bounce(self, axis: str) -> None:
        if axis.lower() == 'x':
            self.speed_x *= -1
        else:
            self.speed_y *= -1

    def reset_pos(self):
        self.x = self.__start_x
        self.y = self.__start_y
