from Paddle import *
import pygame


class AutoPaddle(Paddle):

    def __init__(self, x, w, h, ball, speed):
        self.ball = ball
        super().__init__(x, w, h, speed)

    def draw(self):
        pygame.draw.rect(main_window.window, Color.WHITE.value, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.ball.y > self.y:
            self.y += self.speed
        if self.ball.y < self.y:
            self.y += self.speed
