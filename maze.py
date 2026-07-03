"""
maze.py
--------
Defines the Maze class: loads a maze layout, finds the Start (S) and
Goal (G) positions, and tells the rest of the program which cells are
walls and which are open paths.

Grid coordinates are given as (row, col).
"""

# Default maze layout.
# '#' = wall, '.' = open path, 'S' = start, 'G' = goal
DEFAULT_MAZE_LAYOUT = [
    "##########",
    "#S..#...G#",
    "#.#.#.#..#",
    "#.#...#..#",
    "#...#....#",
    "##########",
]


class Maze:
    def __init__(self, layout=None):
        """
        layout: optional list of equal-length strings describing the maze.
        If not provided, the DEFAULT_MAZE_LAYOUT above is used.
        """
        self.layout = layout if layout is not None else DEFAULT_MAZE_LAYOUT
        self.grid = []          # 2D list: 0 = open, 1 = wall
        self.start = None       # (row, col)
        self.goal = None        # (row, col)

        self._parse_layout()

    def _parse_layout(self):
        for row_index, row_str in enumerate(self.layout):
            grid_row = []
            for col_index, char in enumerate(row_str):
                if char == "#":
                    grid_row.append(1)
                elif char == "S":
                    self.start = (row_index, col_index)
                    grid_row.append(0)
                elif char == "G":
                    self.goal = (row_index, col_index)
                    grid_row.append(0)
                else:  # '.' or anything else counts as open path
                    grid_row.append(0)
            self.grid.append(grid_row)

        if self.start is None or self.goal is None:
            raise ValueError("Maze layout must contain both 'S' (start) and 'G' (goal).")

    @property
    def rows(self):
        return len(self.grid)

    @property
    def cols(self):
        return len(self.grid[0]) if self.grid else 0

    def is_wall(self, row, col):
        return self.grid[row][col] == 1

    def in_bounds(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def is_walkable(self, row, col):
        return self.in_bounds(row, col) and not self.is_wall(row, col)

    def load(self):
        """Prints a confirmation that the maze has loaded (Load Maze step)."""
        print(f"Maze loaded: {self.rows} rows x {self.cols} cols")
        print(f"Start: {self.start}   Goal: {self.goal}")
        return self
