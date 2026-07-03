"""
utils.py
---------
Shared constants and small helper functions used across the project
(colors, sizes, timing, and image loading with a safe fallback).
"""

import os
import pygame

# --------------------------------------------------------------------------
# Layout / timing settings
# --------------------------------------------------------------------------
CELL_SIZE = 60
MOVE_DELAY_MS = 300     # time between robot steps, in milliseconds
FPS = 60

# --------------------------------------------------------------------------
# Colors (R, G, B)
# --------------------------------------------------------------------------
COLOR_BG = (25, 25, 30)
COLOR_WALL = (55, 60, 75)
COLOR_PATH = (235, 235, 235)
COLOR_GRID_LINE = (90, 90, 100)
COLOR_START = (255, 165, 0)
COLOR_GOAL = (0, 200, 100)
COLOR_ROBOT = (0, 150, 255)
COLOR_TRAIL = (255, 200, 0)
COLOR_TEXT = (255, 255, 255)
COLOR_OVERLAY = (0, 0, 0)

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")


def load_robot_image(size):
    """
    Attempts to load assets/robot.png and scale it to (size, size).
    If the image is missing, returns None so the caller can fall back
    to drawing a simple shape instead.
    """
    image_path = os.path.join(ASSETS_DIR, "robot.png")
    if os.path.exists(image_path):
        try:
            image = pygame.image.load(image_path).convert_alpha()
            return pygame.transform.smoothscale(image, (size, size))
        except pygame.error:
            return None
    return None


def grid_to_pixel_center(row, col, cell_size=CELL_SIZE):
    """Converts a (row, col) grid position to the pixel center of that cell."""
    x = col * cell_size + cell_size // 2
    y = row * cell_size + cell_size // 2
    return x, y
