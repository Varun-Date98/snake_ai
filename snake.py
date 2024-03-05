import pygame
from pygame.math import Vector2
from settings import CELL_SIZE, SNAKE_COLOR


class Snake:
    def __init__(self):
        self.color = SNAKE_COLOR
        self.direction = Vector2(1, 0)
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]

    def __len__(self) -> int:
        return len(self.body)

    def draw_snake(self, surface: pygame.Surface) -> None:
        for block in self.body:
            rect = pygame.Rect(block.x * CELL_SIZE, block.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, self.color, rect)

        return

    def move_snake(self, eat_food=False):
        if not eat_food:
            self.body.pop()

        head = self.body[0]
        self.body = [head + self.direction] + self.body

    def move_straight(self):
        self.direction = self.direction

    def left_turn(self):
        # 1 0 -> move right -> 0 -1
        # 0 1 -> move down -> 1 0
        # -1 0 -> move left -> 0 1
        # 0 -1 -> move up -> -1 0
        x = self.direction.x
        y = self.direction.y
        self.direction = Vector2(y, -x)

    def right_turn(self):
        # 1 0 -> move right -> 0 1
        # 0 1 -> move down -> -1 0
        # -1 0 -> move left -> 0 -1
        # 0 -1 -> move up -> 1 0
        x = self.direction.x
        y = self.direction.y
        self.direction = Vector2(-y, x)
