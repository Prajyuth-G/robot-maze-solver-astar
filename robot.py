"""
robot.py
---------
Defines the Robot class: tracks the robot's current grid position,
handles smooth pixel-based movement animation between cells, and
draws itself (using assets/robot.png if available, otherwise a
simple circle shape).
"""

import pygame
from utils import CELL_SIZE, COLOR_ROBOT, load_robot_image, grid_to_pixel_center


class Robot:
    def __init__(self, start_pos):
        """start_pos: (row, col) starting grid cell."""
        self.grid_pos = start_pos
        self.pixel_pos = list(grid_to_pixel_center(*start_pos))
        self.target_pixel_pos = list(self.pixel_pos)
        self.speed = 6  # pixels moved per frame while animating between cells

        self.image = load_robot_image(int(CELL_SIZE * 0.7))

    def show(self, grid_pos):
        """
        Places the robot at a starting grid cell (Show Robot step).
        Resets both logical and pixel position.
        """
        self.grid_pos = grid_pos
        self.pixel_pos = list(grid_to_pixel_center(*grid_pos))
        self.target_pixel_pos = list(self.pixel_pos)

    def move_to(self, grid_pos):
        """
        Sets a new target grid cell. The robot will animate smoothly
        toward it on subsequent update() calls.
        """
        self.grid_pos = grid_pos
        self.target_pixel_pos = list(grid_to_pixel_center(*grid_pos))

    def update(self):
        """
        Moves the robot's pixel position a little closer to its target
        each frame, producing smooth animation. Returns True once the
        robot has arrived at the target cell.
        """
        dx = self.target_pixel_pos[0] - self.pixel_pos[0]
        dy = self.target_pixel_pos[1] - self.pixel_pos[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance <= self.speed:
            self.pixel_pos = list(self.target_pixel_pos)
            return True  # arrived

        self.pixel_pos[0] += self.speed * dx / distance
        self.pixel_pos[1] += self.speed * dy / distance
        return False

    def draw(self, screen):
        x, y = int(self.pixel_pos[0]), int(self.pixel_pos[1])
        if self.image:
            rect = self.image.get_rect(center=(x, y))
            screen.blit(self.image, rect)
        else:
            pygame.draw.circle(screen, COLOR_ROBOT, (x, y), CELL_SIZE // 3)
