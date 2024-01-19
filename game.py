import pygame
from pygame.locals import *
from player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.WIDTH = 1280
        self.HEIGHT = 720
        self.running = True
        self.screen = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT), pygame.RESIZABLE
        )
        self.clock = pygame.time.Clock()
        self.bg_first_arena = pygame.image.load("./assets/arena_1.jpg")
        self.player_1 = Player(x=self.WIDTH // 2, y=self.HEIGHT // 2)

    def update(self):
        # 60 FPS
        self.clock.tick(60)
        pygame.display.flip()
        self.player_1.player_move()

    def event_check(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def draw(self):
        self.screen.fill("black")
        self.bg_first_arena = pygame.transform.smoothscale(
            self.bg_first_arena, (self.WIDTH, self.HEIGHT)
        )
        self.screen.blit(self.bg_first_arena, (0, 0))
        self.player_1.draw_player(screen=self.screen)

        # DISPLAY FPS
        self.font = pygame.font.Font("freesansbold.ttf", 40)
        self.fps_text = self.font.render(
            str(int(self.clock.get_fps())), True, (0, 255, 0)
        )
        self.screen.blit(self.fps_text, (10, 10))

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.event_check(event=event)
            self.draw()
            self.update()
        pygame.quit()
