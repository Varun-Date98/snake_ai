import sys
import pygame
import numpy as np
from game import Game
from settings import N_CELLS, CELL_SIZE, GRASS_DARK, GAME_BACKGROUND


class SnakeAI:
    def __init__(self):
        self.game = Game()
        self.frame_iterations = 0
        self.width = N_CELLS * CELL_SIZE
        self.height = N_CELLS * CELL_SIZE
        self.clock = pygame.time.Clock()
        self. screen = pygame.display.set_mode((self.width, self.height))

    def reset(self):
        self.game = Game()
        self.frame_iterations = 0

    def play_step(self, action):
        self.draw_elements()
        self.frame_iterations += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the snake action => [straight, left, right]
        if np.array_equal(action, [1, 0, 0]):
            self.game.snake.move_straight()
        elif np.array_equal(action, [0, 1, 0]):
            self.game.snake.left_turn()
        elif np.array_equal(action, [0, 0, 1]):
            self.game.snake.right_turn()

        # Check for game over conditions
        reward = 0
        game_over = False

        if self.is_game_over() or self.frame_iterations > len(self.game.snake) * 100:
            reward -= 10
            game_over = True
            return game_over, reward, self.game.score()

        # Increase reward is food is eaten
        if self.game.check_food_collision():
            reward += 10

        # Update UI and tick clock
        self.game.update_screen()
        self.clock.tick(6)

        return reward, game_over, self.game.score()

    def draw_elements(self):
        self.screen.fill(GAME_BACKGROUND)

        for row in range(N_CELLS):
            for col in range(N_CELLS):
                if row % 2 ^ col % 2:
                    rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(self.screen, GRASS_DARK, rect)

        self.game.draw_elements(self.screen)
        pygame.display.update()
        self.clock.tick(60)

    def is_game_over(self) -> bool:
        return self.game.check_game_over()
