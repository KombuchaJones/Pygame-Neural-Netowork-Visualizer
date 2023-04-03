import pygame
from settings import *

class ClassifierPixel(pygame.sprite.Sprite):
    def __init__(self, pos, groups, grid, x, y):
        super().__init__(groups)
        self.image = pygame.Surface((1,1))
        self.rgb_color = 0
        self.image.fill((self.rgb_color, self.rgb_color, self.rgb_color))
        self.rect = self.image.get_rect(topleft = pos)
        self.x = x
        self.y = y
        self.number = grid


    def update(self):
        self.image.fill((self.rgb_color, self.rgb_color, self.rgb_color))