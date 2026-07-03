# Autonomous Robot Maze Solver using A* Path Planning

## Project Goal
Imagine a robot placed inside a maze. Its job is to:
- Find the destination
- Avoid obstacles
- Choose the shortest path
- Reach the goal automatically

There is no real robot — everything happens inside a computer simulation built with Pygame.

## Technologies

| Technology | Purpose                     |
|------------|------------------------------|
| Python     | Programming language        |
| Pygame     | Create the robot simulation |
| VS Code    | Code editor                  |
| Git        | Version control              |
| GitHub     | Store and share the project  |

## What the Maze Looks Like

```
##########
#S..#...G#
#.#.#.#..#
#.#...#..#
#...#....#
##########
```

Where:
- `S` = Start
- `G` = Goal
- `#` = Wall
- `.` = Open path

The robot starts at `S`, calculates the shortest route using the **A\* search algorithm**,
and moves automatically, step by step, until it reaches `G`.

## How the Project Works

```
Start Program
      ↓
  Load Maze
      ↓
  Show Robot
      ↓
Calculate Best Path
      ↓
Move Step by Step
      ↓
 Reached Goal?
      ↓
     Yes
      ↓
Show Success Message
```

## Project Structure

```
Robot-Maze-Solver/
│
├── main.py              # Entry point - runs the simulation loop
├── maze.py               # Maze class - loads and parses the grid
├── robot.py               # Robot class - position, movement, drawing
├── astar.py               # A* pathfinding algorithm
├── utils.py               # Shared constants and helper functions
├── assets/
│     robot.png            # (optional) robot sprite image
├── screenshots/
├── README.md
├── requirements.txt
└── LICENSE
```

## Installation

1. Clone or download this repository.
2. Install the dependency:
   ```
   pip install -r requirements.txt
   ```
   > This project uses **pygame-ce** (Community Edition), which has the same API as
   > regular `pygame` but includes prebuilt wheels for the latest Python versions.
   > If you already have classic `pygame` installed and it works, that's fine too.

## Running the Project

```
python main.py
```

A window will open showing the maze. The robot (blue circle, or `assets/robot.png`
if you add one) will automatically move along the shortest path toward the goal.
When it arrives, a success message is displayed. Press `ESC` or close the window
to exit.

## Customizing the Maze

Edit `DEFAULT_MAZE_LAYOUT` in `maze.py` — it's just a list of equal-length strings.
Use `#` for walls, `.` for open paths, and exactly one `S` and one `G`.

## How the Pathfinding Works (A*)

A* explores the maze outward from the start, always prioritizing the cell that
looks most promising — combining:
- **g(n)** — the actual number of steps taken so far to reach a cell
- **h(n)** — an estimate (Manhattan distance) of how far that cell is from the goal

By always expanding the cell with the lowest `g + h`, A* is guaranteed to find the
shortest possible path while avoiding walls, without needing to check every single
cell in the maze (unlike simpler algorithms like plain BFS in large mazes).

## License
This project is released under the MIT License — see `LICENSE` for details.
