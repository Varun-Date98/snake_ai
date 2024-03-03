import pygame
from typing import List
from random import randint
from pygame.math import Vector2
from settings import CELL_SIZE, N_CELLS, FOOD_COLOR


class Food:
    def __init__(self):
        self.color = FOOD_COLOR
        self.x = randint(0, N_CELLS - 1)
        self.y = randint(0, N_CELLS - 1)
        self.pos = Vector2(self.x, self.y)

    def randomize(self, snake_body: List[pygame.Vector2]):
        self.x = randint(0, N_CELLS - 1)
        self.y = randint(0, N_CELLS - 1)
        self.pos = Vector2(self.x, self.y)

        if any(self.pos == cell for cell in snake_body):
            self.randomize(snake_body)

    def draw_food(self, surface: pygame.Surface):
        rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, self.color, rect)
