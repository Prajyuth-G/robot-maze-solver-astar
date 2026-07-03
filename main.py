"""
main.py
--------
Autonomous Robot Maze Solver using A* Path Planning
=====================================================

This is the entry point of the project. It follows this flow exactly:

    Start Program
        -> Load Maze
        -> Show Robot
        -> Calculate Best Path
        -> Move Step by Step
        -> Reached Goal?
             Yes -> Show Success Message

Run with:
    python main.py
"""

import sys
import pygame

from maze import Maze
from astar import calculate_best_path
from robot import Robot
import utils


def draw_maze(screen, maze, trail):
    """Draws walls, paths, start, goal, and the robot's trail."""
    for row in range(maze.rows):
        for col in range(maze.cols):
            rect = pygame.Rect(col * utils.CELL_SIZE, row * utils.CELL_SIZE,
                                utils.CELL_SIZE, utils.CELL_SIZE)
            color = utils.COLOR_WALL if maze.is_wall(row, col) else utils.COLOR_PATH
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, utils.COLOR_GRID_LINE, rect, 1)

    # Trail dots for cells the robot has already visited
    for (row, col) in trail:
        cx, cy = utils.grid_to_pixel_center(row, col)
        pygame.draw.circle(screen, utils.COLOR_TRAIL, (cx, cy), utils.CELL_SIZE // 8)

    # Start marker
    sr, sc = maze.start
    start_rect = pygame.Rect(sc * utils.CELL_SIZE + 8, sr * utils.CELL_SIZE + 8,
                              utils.CELL_SIZE - 16, utils.CELL_SIZE - 16)
    pygame.draw.rect(screen, utils.COLOR_START, start_rect, border_radius=6)

    # Goal marker
    gr, gc = maze.goal
    goal_rect = pygame.Rect(gc * utils.CELL_SIZE + 8, gr * utils.CELL_SIZE + 8,
                             utils.CELL_SIZE - 16, utils.CELL_SIZE - 16)
    pygame.draw.rect(screen, utils.COLOR_GOAL, goal_rect, border_radius=6)


def draw_success_message(screen, font, width, height):
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(180)
    overlay.fill(utils.COLOR_OVERLAY)
    screen.blit(overlay, (0, 0))

    text = font.render("SUCCESS! Robot reached the goal!", True, utils.COLOR_TEXT)
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)

    sub_font = pygame.font.SysFont("Arial", 18)
    sub_text = sub_font.render("Press ESC or close the window to exit", True, utils.COLOR_TEXT)
    sub_rect = sub_text.get_rect(center=(width // 2, height // 2 + 36))
    screen.blit(sub_text, sub_rect)


def main():
    print("=== Start Program ===")

    # ---- Load Maze ----
    maze = Maze().load()

    # ---- Calculate Best Path ----
    path = calculate_best_path(maze)
    if path is None:
        print("No path could be found between start and goal. Exiting.")
        return
    print(f"Best path calculated with {len(path) - 1} moves: {path}")

    # ---- Pygame / window setup ----
    pygame.init()
    width = maze.cols * utils.CELL_SIZE
    height = maze.rows * utils.CELL_SIZE
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Autonomous Robot Maze Solver - A*")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 26, bold=True)

    # ---- Show Robot ----
    robot = Robot(path[0])

    trail = []
    step_index = 0
    reached_goal = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # ---- Move Step by Step ----
        if not reached_goal:
            arrived_at_cell = robot.update()
            if arrived_at_cell:
                if robot.grid_pos not in trail:
                    trail.append(robot.grid_pos)
                step_index += 1
                if step_index < len(path):
                    robot.move_to(path[step_index])
                else:
                    # ---- Reached Goal? -> Yes ----
                    reached_goal = True

        # ---- Draw everything ----
        screen.fill(utils.COLOR_BG)
        draw_maze(screen, maze, trail)
        robot.draw(screen)

        if reached_goal:
            # ---- Show Success Message ----
            draw_success_message(screen, font, width, height)

        pygame.display.flip()
        clock.tick(utils.FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
