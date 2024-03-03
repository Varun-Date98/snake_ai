import sys

import pygame

from food import Food
from settings import FONT, N_CELLS, CELL_SIZE
from snake import Snake


class Game:
    def __init__(self):
        self.food = Food()
        self.snake = Snake()
        self.font = pygame.font.Font(FONT, 25)

    def update_screen(self):
        self.check_game_over()
        check = self.check_food_collision()
        self.snake.move_snake(eat_food=check)

    def draw_elements(self, surface: pygame.Surface):
        self.food.draw_food(surface)
        self.snake.draw_snake(surface)
        self.draw_score(surface, self.font)

    def check_food_collision(self) -> bool:
        if self.food.pos == self.snake.body[0]:
            self.food.randomize(self.snake.body)
            return True

        return False

    def check_game_over(self):
        head = self.snake.body[0]

        # Check if head is out of bounds
        if not (0 <= head.x < N_CELLS) or not (0 <= head.y < N_CELLS):
            pygame.quit()
            sys.exit()

        for block in self.snake.body[1:]:
            if head == block:
                pygame.quit()
                sys.exit()

    def draw_score(self, screen: pygame.display, font: pygame.font.Font):
        score = f"Score: {len(self.snake) - 3}"
        score_x, score_y = CELL_SIZE * N_CELLS - 120, 40
        score_surface = font.render(score, True, (56, 74, 12))
        score_rectangle = score_surface.get_rect(center=(score_x, score_y))
        screen.blit(score_surface, score_rectangle)