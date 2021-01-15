from globals import *
import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, w, h, speed):
        self.width = w
        self.height = h
        self.speed = speed
        self.rect = pygame.Rect(x, main_window.height / 2 - h / 2, w, h)

    def draw(self):
        pygame.draw.rect(main_window.window, Color.WHITE.value, (self.rect.x, self.rect.y, self.width, self.height))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < main_window.height - self.height - self.speed:
            self.rect.y += self.speed
