# from Ball import Ball
from Paddle import Paddle
# from AutoPaddle import AutoPaddle
from ScoreBoard import ScoreBoard
from globals import *
import pygame


class GameManager():
    def __init__(self):
        # self.ball = Ball(x,y,width,height,speed)
        self.player_paddle = Paddle(20, 10, 50, 5)
        # self.bot_paddle = AutoPaddle(x,y,width,height, self.ball, speed)
        self.scoreboard =  ScoreBoard()
        pass

    def draw(self):

        main_window.window.fill(Color.BLACK.value)
        pygame.draw.rect(main_window.window, Color.WHITE.value,
                         ((0, 0), (main_window.width, main_window.height)), 20)

        pygame.draw.line(main_window.window,  Color.WHITE.value,
                         (int(main_window.width // 2), 0),
                         (int(main_window.width / 2), main_window.height),int(10 / 4))

        # self.ball.draw()
        self.scoreboard.draw()
        self.player_paddle.draw()
        # self.bot_paddle.draw()

    def update(self):
        # self.ball.move()
        # self.bot_paddle.move()
        self.player_paddle.move()
        # TODO, logic of ball passing or hitting paddles...
        pass
