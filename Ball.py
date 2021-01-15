"""class ball by TOMER"""

from pygame import sprite, draw, Rect
from globals import *
from Paddle import Paddle
import math
from random import randint


class Ball(sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, speed: float):
        super(Ball, self).__init__()
        self.__start_x = x
        self.__start_y = y
        self.speed = speed
        self.dir_x = speed
        self.dir_y = speed
        self.rect = Rect(x, y, width, height)
        self.radius = height/2

    def draw(self):
        draw.circle(main_window.window, Color.RED.value, self.rect.center, self.radius)

    def move(self):
        if self.hit_floor():
            self.bounce('y')
        elif self.hit_ceiling():
            self.bounce('y')
        elif self.pass_computer():
            self.bounce('x')
        else:
            self.rect.x += self.dir_x
            self.rect.y += self.dir_y
            #self.rect.move(self.x + self.dir_x, self.y + self.dir_y)
            # self.x += self.dir_x
            # self.y += self.dir_y

    def hit_paddle(self, paddle: Paddle) -> bool:
        return self.rect.colliderect(paddle.rect)

    def hit_floor(self):
        return self.rect.y + self.dir_y + self.radius > main_window.height - 10

    def hit_ceiling(self):
        tmp_y = self.rect.y + self.dir_y
        return tmp_y < 10 + self.radius

    def pass_computer(self) -> bool:
        tmp_x = self.rect.x + self.dir_x
        return tmp_x + self.radius > main_window.width - 10

    def pass_player(self) -> bool:
        tmp_x = self.rect.x + self.dir_x
        return tmp_x < 10 + self.radius

    def bounce(self, axis: str) -> None:
        if axis.lower() == 'x':
            self.dir_x *= -1
        else:
            self.dir_y *= -1

    def reset_pos(self):
        self.rect.x = self.__start_x
        self.rect.y = self.__start_y

        self.dir_x = 6
        self.dir_y = 6
