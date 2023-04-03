import pygame
from sys import exit
from level import Level
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.set_caption(f'Visualized Neural Network {self.clock.get_fps()}')
            dt = self.clock.tick(60) / 1000
            self.screen.fill('black')
            self.level.update(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()