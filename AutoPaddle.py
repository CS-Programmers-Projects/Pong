from Paddle import *
import pygame


class AutoPaddle(Paddle):

    def __init__(self, x, w, h,  ball, speed):
        super().__init__(x, w, h, speed)
        self.ball = ball

    def move(self):
        if self.ball.rect.y > self.rect.center[1]:
            self.rect.y += self.speed
        if self.ball.rect.y < self.rect.center[1]:
            self.rect.y += self.speed
