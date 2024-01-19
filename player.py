import pygame
from pygame.locals import *


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rectangle = pygame.Rect(self.x, self.y, 100, 100)

    def draw_player(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rectangle)

    def player_move(self):
        pressed_keys = pygame.key.get_pressed()

        # LEFT CHECK
        if self.rectangle.left > 0:
            if pressed_keys[K_a]:
                self.rectangle.move_ip(-5.0, 0.0)

        # RIGHT CHECK
        if self.rectangle.right < self.x * 2:
            if pressed_keys[K_d]:
                self.rectangle.move_ip(5.0, 0.0)

        # UP CHECK
        if self.rectangle.top > 0:
            if pressed_keys[K_w]:
                self.rectangle.move_ip(0.0, -5.0)

        # DOWN CHECK
        if self.rectangle.bottom < self.y * 2:
            if pressed_keys[K_s]:
                self.rectangle.move_ip(0.0, 5.0)
