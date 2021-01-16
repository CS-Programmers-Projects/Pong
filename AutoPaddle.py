from Paddle import *
import pygame


class AutoPaddle(Paddle):
    """
    AutoPaddle class to create an NPC paddler that will go against the Player
    """

    def __init__(self, x, w, h, ball, speed):
        """

        initializing the objects needed in this class, including the ones it inherits from Paddle.
        :param x: x value of location
        :param w: width of the autopaddler
        :param h: height of the autopaddler
        :param ball: pointer to the ball object
        :param speed: speed of the autopaddler
        """

        super().__init__(x, w, h, speed)
        self.ball = ball
        self.rect = pygame.Rect(x, main_window.height / 2 - h / 2, w, h)

    def move(self):
        """
        incharge of the movement of our AutoPaddle , according to the ball location
        :return: nothing
        """

        if self.ball.rect.y > self.rect.y and self.rect.y + self.height + self.speed < main_window.height:
            self.rect.y += self.speed
        if self.ball.rect.y < self.rect.y:
            self.rect.y -= self.speed
