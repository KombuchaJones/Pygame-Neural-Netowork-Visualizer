import pygame
from settings import *

class Timer:
    def __init__(self, timer_length):
        self.active = False
        self.timer_length = timer_length
        self.start_time = pygame.time.get_ticks()
        self.current_time = 0

    def activate(self):
        self.start_time = pygame.time.get_ticks()
        self.active = True
        self.current_time = pygame.time.get_ticks()

    def deactivate(self):
        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.start_time >= self.timer_length:
            self.active = False

    def update(self):

        if self.active:
            self.deactivate()




