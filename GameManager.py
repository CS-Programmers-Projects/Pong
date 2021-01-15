from Ball import Ball
from Paddle import Paddle
from ScoreBoard import ScoreBoard
from globals import *
import pygame
from AutoPaddle import AutoPaddle


class GameManager():
    def __init__(self):
        self.ball = Ball(main_window.width / 2, main_window.height / 2, 10, 10, 5)
        self.player_paddle = Paddle(20, 10, 50, 5)
        #self.bot_paddle = AutoPaddle(370, 10, 50, 0, 5)
        self.scoreboard = ScoreBoard()

    def draw(self):
        main_window.window.fill(Color.BLACK.value)
        pygame.draw.rect(main_window.window, Color.WHITE.value,
                         ((0, 0), (main_window.width, main_window.height)), 20)

        self.ball.draw()
        self.scoreboard.draw()
        self.player_paddle.draw()
        #self.bot_paddle.draw()

    def update(self):
        self.ball.move()
       #self.bot_paddle.move()
        self.player_paddle.move()

        # if self.ball.hit_paddle(self.bot_paddle):
        #     self.ball.bounce("x")
        if self.ball.hit_paddle(self.player_paddle):
            self.ball.bounce("x")
        elif self.ball.pass_player():
            print("Passed player")
            self.ball.reset_pos()
        elif self.ball.pass_computer():
            print("passed bot")
