"""
astar.py
---------
Implements the A* search algorithm to find the shortest path between
the robot's start position and the goal, avoiding walls.

A* combines:
  g(n) = cost so far to reach node n
  h(n) = estimated cost from n to the goal (Manhattan distance heuristic)
  f(n) = g(n) + h(n)

It always expands the node with the lowest f(n) first, which guarantees
the shortest path is found (as long as the heuristic never overestimates,
which Manhattan distance does not for grid movement).
"""

import heapq


def manhattan_distance(a, b):
    """Heuristic: estimated distance between two grid cells (no diagonals)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def calculate_best_path(maze, start=None, goal=None):
    """
    Runs A* on the given Maze object and returns the best path as a list
    of (row, col) tuples from start to goal (inclusive).

    Returns None if no path exists.
    """
    start = start or maze.start
    goal = goal or maze.goal

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    open_set = []
    heapq.heappush(open_set, (0, start))          # (f_score, node)
    came_from = {}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return _reconstruct_path(came_from, current)

        if current in visited:
            continue
        visited.add(current)

        for dr, dc in directions:
            neighbor = (current[0] + dr, current[1] + dc)

            if not maze.is_walkable(*neighbor):
                continue

            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + manhattan_distance(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

    return None  # No path found


def _reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path
