from Ball import Ball
from Paddle import Paddle
from ScoreBoard import ScoreBoard
from globals import *
import pygame
from AutoPaddle import AutoPaddle


class GameManager():
    def __init__(self):
        self.ball = Ball(int(main_window.width // 2), int(main_window.height // 2), 7, 2)
        self.player_paddle = Paddle(20, 10, 50, 5)
        self.bot_paddle = AutoPaddle(370, 10, 50, 0, 5)
        self.scoreboard = ScoreBoard()

    def draw(self):
        main_window.window.fill(Color.BLACK.value)
        pygame.draw.rect(main_window.window, Color.WHITE.value,
                         ((0, 0), (main_window.width, main_window.height)), 20)

        self.ball.draw()
        self.scoreboard.draw()
        self.player_paddle.draw()
        self.bot_paddle.draw()

    def update(self):
        self.ball.move()
        self.bot_paddle.move()
        self.player_paddle.move()

        if self.ball.hit_paddle(self.bot_paddle):
            self.ball.bounce("x")
        elif self.ball.hit_paddle(self.player_paddle):
            self.ball.bounce("x")
        elif self.ball.pass_player():
            print("Passed player")
        elif self.ball.pass_computer():
            print("passed bot")
