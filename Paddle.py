from globals import *
import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, w, h, speed):
        self.x = x
        self.y = main_window.height / 2 - h / 2
        self.width = w
        self.height = h
        self.speed = speed
        self.rect = pygame.Rect(x, self.y, w, h)

    def draw(self):
        pygame.draw.rect(main_window.window, Color.WHITE.value, (self.x, self.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.y > self.speed:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < main_window.height - self.height - self.speed:
            self.y += self.speed
