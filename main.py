import sys
import pygame
from game import Game
from settings import N_CELLS, CELL_SIZE, MOVEMENT_SPEED_MSEC, GRASS_DARK, GAME_BACKGROUND


def draw_grass(surface: pygame.Surface):
    for row in range(N_CELLS):
        for col in range(N_CELLS):
            if row % 2 ^ col % 2:
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(surface, GRASS_DARK, rect)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((N_CELLS * CELL_SIZE, N_CELLS * CELL_SIZE))

    game = Game()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, MOVEMENT_SPEED_MSEC)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                game.update_screen()

            # Control movement of the snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.snake.move_up()
                elif event.key == pygame.K_LEFT:
                    game.snake.move_left()
                elif event.key == pygame.K_DOWN:
                    game.snake.move_down()
                elif event.key == pygame.K_RIGHT:
                    game.snake.move_right()

        screen.fill(GAME_BACKGROUND)
        draw_grass(screen)
        game.draw_elements(screen)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
