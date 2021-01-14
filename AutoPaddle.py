from Paddle import *
import pygame


class AutoPaddle(Paddle):

    def __init__(self, x, w, h, y, ball, speed):
        super().__init__(x, w, h, speed)
        self.ball = ball
        self.y = y

    def move(self):

        if self.ball.y > self.rect.center:
            self.y += self.speed
        if self.ball.y < self.rect.center:
            self.y += self.speed
