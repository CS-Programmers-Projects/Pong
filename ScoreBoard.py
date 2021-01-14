from globals import *
import pygame

class ScoreBoard():

    def __init__(self, x = main_window.width // 2, y = main_window.height // 10):
        self.x = x
        self.y = y
        self.userScore = 0
        self.computerScore = 0
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def draw(self):
        text = self.font.render("player: " + str(self.userScore) + "               computer: " + str(self.computerScore) ,
                                True, (255, 255, 255))

        textRect = text.get_rect()

        textRect.center = (self.x , self.y)

        main_window.window.blit(text, textRect)

    def update_player_score(self, score_new = 1):
        self.userScore += score_new

    def update_computer_score(self, score_new = 1):
        self.computerScore += score_new