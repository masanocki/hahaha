import pygame
from pygame.locals import *


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.running = True
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        self.bg_first_arena = pygame.image.load("./assets/arena_1.jpg")

    def update(self):
        pygame.display.flip()
        # 60 FPS
        self.clock.tick(60)

    def event_check(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def draw(self):
        self.screen.fill("black")
        self.bg_first_arena = pygame.transform.smoothscale(
            self.bg_first_arena, self.screen.get_size()
        )
        self.screen.blit(self.bg_first_arena, (0, 0))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.event_check(event=event)
            self.draw()
            self.update()
        pygame.quit()
