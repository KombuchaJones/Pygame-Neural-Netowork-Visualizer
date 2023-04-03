import pygame
from settings import *

class OverGrid(pygame.sprite.Sprite):
    def __init__(self, groups, pos, grid):
        super().__init__(groups)
        self.image = pygame.Surface((60, 60))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
        self.grid = grid

    def update(self):
        pass

