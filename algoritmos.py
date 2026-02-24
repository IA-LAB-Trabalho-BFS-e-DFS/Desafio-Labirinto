import random
from collections import deque
from typing import Tuple, Iterable
from time import time
import tracemalloc

# ===============================
# GERAR LABIRINTO ALEATÓRIO
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
# FUNÇÕES AUXILIARES
# ===============================


def neighbors(pos: Tuple[int, int], grid) -> Iterable[Tuple[int, int]]:
    r, c = pos

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != "#":
                yield (nr, nc)


def reconstruct_path(parent, start, goal):
    if goal not in parent and goal != start:
        return []

    path = [goal]
    cur = goal

    while cur != start:
        cur = parent[cur]
        path.append(cur)

    path.reverse()
    return path


# ===============================
# BFS
# ===============================


def bfs_grid(grid, start, goal):
    tracemalloc.start()
    inicio = time()

    queue = deque([start])
    visited = {start}
    parent = {}

    while queue:
        u = queue.popleft()
        if u == goal:
            tempo = time() - inicio
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return True, reconstruct_path(parent, start, goal), tempo, current, peak

        for v in neighbors(u, grid):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)

    tempo = time() - inicio
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return False, [], tempo, current, peak


# ===============================
# DFS
# ===============================


def dfs_grid(grid, start, goal):
    tracemalloc.start()
    inicio = time()

    stack = [start]
    visited = {start}
    parent = {}

    while stack:
        u = stack.pop()
        if u == goal:
            tempo = time() - inicio
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            return True, reconstruct_path(parent, start, goal), tempo, current, peak

        for v in reversed(list(neighbors(u, grid))):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                stack.append(v)

    tempo = time() - inicio
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return False, [], tempo, current, peak


# ===============================
# VISUALIZAÇÃO
# ===============================


def draw_path(grid, path):
    g = [row[:] for row in grid]
    for r, c in path:
        if g[r][c] not in ("S", "G"):
            g[r][c] = "*"
    return g


def print_grid(grid):
    for row in grid:
        print("".join(row))


# ===============================
# EXECUÇÃO
# ===============================

maze = generate_maze(20, 20, 0.30)

start = (0, 0)
goal = (19, 19)

found_bfs, path_bfs, time_bfs, mem_bfs_current, mem_bfs_peak = bfs_grid(
    maze, start, goal
)
found_dfs, path_dfs, time_dfs, mem_dfs_current, mem_dfs_peak = dfs_grid(
    maze, start, goal
)


print("RESULTADOS:\n")

print(
    "BFS -> Encontrou:",
    found_bfs,
    "| Passos:",
    len(path_bfs),
    "| Tempo:",
    f"{time_bfs:.6f}s",
    "| Memória atual:",
    f"{mem_bfs_current / 1024:.2f} KB",
    "| Pico memória:",
    f"{mem_bfs_peak / 1024:.2f} KB",
)

print(
    "DFS -> Encontrou:",
    found_dfs,
    "| Passos:",
    len(path_dfs),
    "| Tempo:",
    f"{time_dfs:.6f}s",
    "| Memória atual:",
    f"{mem_dfs_current / 1024:.2f} KB",
    "| Pico memória:",
    f"{mem_dfs_peak / 1024:.2f} KB",
)

if found_bfs:
    print("\nCAMINHO BFS:")
    print_grid(draw_path(maze, path_bfs))

if found_dfs:
    print("\nCAMINHO DFS:")
    print_grid(draw_path(maze, path_dfs))
