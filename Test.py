import pygame
import random
from collections import deque
from typing import Tuple, Iterable

# ===============================
# CONFIGURAÇÕES
# ===============================

CELL_SIZE = 30
ROWS = 20
COLS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (100, 149, 237)
YELLOW = (255, 215, 0)
GRAY = (200, 200, 200)

# ===============================
# GERAR LABIRINTO
# ===============================

def generate_maze(rows=20, cols=20, obstacle_prob=0.30):
    maze = []
    for r in range(rows):
        row = []
        for c in range(cols):
            if random.random() < obstacle_prob:
                row.append("#")
            else:
                row.append(".")
        maze.append(row)

    maze[0][0] = "S"
    maze[rows - 1][cols - 1] = "G"
    return maze

# ===============================
# VIZINHOS
# ===============================

def neighbors(pos: Tuple[int, int], grid) -> Iterable[Tuple[int, int]]:
    r, c = pos
    directions = [(-1,0),(1,0),(0,-1),(0,1),
                  (-1,-1),(-1,1),(1,-1),(1,1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != "#":
                yield (nr, nc)

# ===============================
# RECONSTRUIR CAMINHO
# ===============================

def reconstruct_path(parent, start, goal):
    path = []
    cur = goal
    while cur in parent:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()
    return path

# ===============================
# DESENHO
# ===============================

def draw_grid(screen, grid, visited, path):
    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if (r,c) in path:
                color = YELLOW
            elif grid[r][c] == "#":
                color = BLACK
            elif grid[r][c] == "S":
                color = GREEN
            elif grid[r][c] == "G":
                color = RED
            elif (r,c) in visited:
                color = BLUE
            else:
                color = WHITE

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)
