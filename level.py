import pygame
from tile import Tile
from timer import Timer
from over_grid import OverGrid
from classifier_pixel import ClassifierPixel
from settings import *


class Level:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.drawing_sprites = pygame.sprite.Group()
        self.classifier_pixels = pygame.sprite.Group()
        self.grid_buttons = pygame.sprite.Group()
        self.draw_level()
        self.can_add_array = True
        self.save_timer =Timer(2000)
        self.test_font = pygame.font.Font(None, 20)
        self.statement = []


    def draw_level(self):
        for y in range(60):
            for x in range(60):
                tile_position = (x * TILE_W + 200, y * TILE_H + 200)
                self.drawing_sprites.add(Tile((tile_position), self.drawing_sprites, x, y))
        for i in range(10):
            grid_position = (i * 100 + 20, 75)
            OverGrid(self.grid_buttons, grid_position, i)

        self.grid_array = []

        for grid in range(10):
            self.grid_array.append([])
            for y in range(60):
                self.grid_array[grid].append([])
                for x in range(60):
                    pixel_position = (grid * 100 + 20 + x, y + 75)
                    new_pixel = ClassifierPixel(pixel_position, self.classifier_pixels, grid, x , y)
                    self.grid_array[grid][y].append(new_pixel)

    def input(self):
        keys = pygame.key.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if keys[pygame.K_c]:
            self.clear()
        # elif keys[pygame.K_s] and self.can_add_array:
        #     self.intensity_array()
        #     self.can_add_array = False
        #     self.save_timer.activate()

        for sprite in self.drawing_sprites:
            if mouse_pressed[0] and sprite.rect.collidepoint(mouse_pos):
                sprite.image.fill('white')
                sprite.clicked = True

        for sprite in self.grid_buttons:
            if mouse_pressed[0] and sprite.rect.collidepoint(mouse_pos):
                if self.can_add_array:
                    self.intensity_array(sprite.grid)
                    self.can_add_array = False
                    self.save_timer.activate()
                    break

            elif mouse_pressed[2] and sprite.rect.collidepoint(mouse_pos):
                if self.can_add_array:
                    self.predict_number(sprite.grid)
                    self.can_add_array = False
                    self.save_timer.activate()
                    break

    def grid_lines(self):
        for x in range(61):
            start_pos = (200 + x * TILE_W, 200)
            end_pos = (200 + x * TILE_W, 800)
            pygame.draw.line(self.screen, (128, 128,128,), start_pos, end_pos, width=1)

        for y in range(61):
            start_pos = (200, 200 + y * TILE_H)
            end_pos = (800, 200 + y * TILE_H)
            pygame.draw.line(self.screen, (128, 128,128,), start_pos, end_pos, width=1)

    def clear(self):
        for sprite in self.drawing_sprites:
            sprite.image.fill('black')
            sprite.clicked = False
        self.statement.clear()

    def intensity_array(self, grid_number):

        # empty_intensity_array = []

        # for y in range(60):
        #     empty_intensity_array.append([])
        #     for x in range(60):
        #         empty_intensity_array[y].append(0)
        working_grid = self.grid_array[grid_number]
        for sprite in self.drawing_sprites:
            if sprite.clicked and working_grid[sprite.y][sprite.x].rgb_color < 250:
                # empty_intensity_array[sprite.y][sprite.x] = 1
                working_grid[sprite.y][sprite.x].rgb_color += 50
            else:
                pass


        # print(empty_intensity_array)
        # for y in range(len(empty_intensity_array)):
        #     for x in range(y):
        #         if empty_intensity_array[y][x] == 1:
        #             color = working_grid[y][x].rgb_color = 250
        #             working_grid[y][x].image.fill((color, color, color))
        print(f'Array saved in {grid_number}')
        self.statement.append(f'Array saved in {grid_number}')

    def decrement(self, grid):
        for sprite in self.drawing_sprites:
            if sprite.clicked:
                if grid[sprite.y][sprite.x].rgb_color >= 50:
                    grid[sprite.y][sprite.x].rgb_color -= 50
                    # color = grid[sprite.y][sprite.x].rgb_color - 50
                    # grid[sprite.y][sprite.x].rgb_color = color
                    # grid[sprite.y][sprite.x].image.fill((color, color, color))
                    # print('hello')

    def predict_number(self, grid_number):
        probability_list = []

        for grid in self.grid_array:
            probability_list.append(0)
            for sprite in self.drawing_sprites:
                if sprite.clicked and grid[sprite.y][sprite.x].rgb_color > 0:
                    probability_list[-1] += 1

        self.statement.append(f' Probability list {probability_list}')
        max_prob_value = max(probability_list)
        predicted_number = probability_list.index(max_prob_value)
        print(f'Predicted number is {predicted_number} with a probability of {max_prob_value}')
        print(f'True number is {grid_number}.')
        self.statement.append(f'Predicted number is {predicted_number} with a probability of {max_prob_value}')
        self.statement.append(f'True number is {grid_number}.')

        if predicted_number != grid_number:
            decrement_grid = self.grid_array[predicted_number]
            print(f'Decrementing {predicted_number}')
            self.statement.append(f'Decrementing {predicted_number}')
        else:
            decrement_grid = None

        self.intensity_array(grid_number)
        if decrement_grid:
            self.decrement(decrement_grid)
        print()

    def classifier_grids(self):
        for i in range(10):
            pygame.draw.rect(self.screen, (128, 128,128,), (i * 100 + 20,75, 60,60), 1)

    def status_statement(self):
        for statement in range(len(self.statement)):
            statement_surf = self.test_font.render(f'{self.statement[statement]}', False, ('white'))
            statement_rect = statement_surf.get_rect(midtop=(SCREEN_W//2, 850 + statement * 25))
            self.screen.blit(statement_surf, statement_rect)

    def update(self, dt):
        self.input()
        self.classifier_pixels.update()
        self.grid_buttons.draw(self.screen)
        self.classifier_pixels.draw(self.screen)
        self.drawing_sprites.draw(self.screen)
        self.classifier_grids()
        self.grid_lines()
        self.save_timer.update()
        if not self.save_timer.active:
            self.can_add_array = True
        if self.statement:
            self.status_statement()
