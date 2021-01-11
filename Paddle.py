from globals import *
import pygame

class Paddle():
    def __init__(self, x, w, h, speed):
        self.x = x
        self.y = main_window.height/2 - h/2
        self.width = w
        self.height = h
        self.speed = speed

    def draw(self):
        pygame.draw.rect(main_window.window,  Color.WHITE.value, (self.x, self.y, self.width, self.height))

    def move(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y += self.speed
        if keys[pygame.K_DOWN]:
            self.y -= self.speed