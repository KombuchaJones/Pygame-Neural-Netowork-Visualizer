import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, x, y):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE))
        self.image.fill('black')
        self.rect = self.image.get_rect(topleft = pos)
        self.clicked = False
        self.x = x
        self.y = y

    def color_white(self):
        self.image.fill('white')

    def uncolor(self):
        self.image.fill('black')

    def update(self):
        pass