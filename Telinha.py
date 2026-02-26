import pygame
import random
from collections import deque
from typing import Tuple, Iterable
import tracemalloc
from time import time


# ===============================
# CONFIGURAÇÕES
# ===============================

CELL_SIZE = 30
ROWS = 20
COLS = 20
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE
FPS = 60
search_start_time = time()
SEARCH_DELAY = 120  # velocidade da busca (ms)

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
# VIZINHOS (8 DIREÇÕES)
# ===============================

def neighbors(pos: Tuple[int, int], grid) -> Iterable[Tuple[int, int]]:
    r, c = pos

    directions = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1),
        (-1, -1), (-1, 1),
        (1, -1), (1, 1)
    ]

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

            if (r, c) in path:
                color = YELLOW
            elif grid[r][c] == "#":
                color = BLACK
            elif grid[r][c] == "S":
                color = GREEN
            elif grid[r][c] == "G":
                color = RED
            elif (r, c) in visited:
                color = BLUE
            else:
                color = WHITE

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

# ===============================
# MAIN
# ===============================

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT + 60))
    pygame.display.set_caption("Busca em Tempo Real - Métricas")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    grid = generate_maze(ROWS, COLS)
    start = (0, 0)
    goal = (ROWS-1, COLS-1)

    structure = None
    visited = set()
    parent = {}
    running_search = False
    found = False
    path = []
    mode = None

    steps = 0
    last_step_time = 0

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_b:
                    tracemalloc.start()
                    structure = deque([start])
                    visited = {start}
                    parent = {}
                    running_search = True
                    found = False
                    path = []
                    mode = "BFS"
                    steps = 0

                if event.key == pygame.K_d:
                    tracemalloc.start()
                    structure = [start]
                    visited = {start}
                    parent = {}
                    running_search = True
                    found = False
                    path = []
                    mode = "DFS"
                    steps = 0

                if event.key == pygame.K_r:
                    grid = generate_maze(ROWS, COLS)
                    visited.clear()
                    parent.clear()
                    path = []
                    running_search = False
                    found = False
                    steps = 0

                if event.key == pygame.K_UP:
                    global SEARCH_DELAY
                    SEARCH_DELAY = max(20, SEARCH_DELAY - 20)

                if event.key == pygame.K_DOWN:
                    SEARCH_DELAY += 20

        # EXECUTA PASSO CONTROLADO
        current_time = pygame.time.get_ticks()

        if running_search and not found and structure:
            if current_time - last_step_time > SEARCH_DELAY:
                last_step_time = current_time
                steps += 1

                if mode == "BFS":
                    current = structure.popleft()
                else:
                    current = structure.pop()

                if current == goal:
                    found = True
                    path = reconstruct_path(parent, start, goal)
                else:
                    for neighbor in neighbors(current, grid):
                        if neighbor not in visited:
                            visited.add(neighbor)
                            parent[neighbor] = current
                            structure.append(neighbor)

        # MÉTRICAS DE MEMÓRIA
        current_mem, peak_mem = tracemalloc.get_traced_memory() if running_search else (0, 0)

        # DESENHO
        screen.fill(WHITE)
        draw_grid(screen, grid, visited, path)

        info_text = f"Algoritmo: {mode} | Passos: {steps} | Visitados: {len(visited)}| Tempo: {last_step_time/60:.2f}s | Mem Atual: {current_mem//1024} KB | Pico: {peak_mem//1024} KB"
        text_surface = font.render(info_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, HEIGHT + 15))

        pygame.display.update()

    tracemalloc.stop()
    pygame.quit()

if __name__ == "__main__":
    main()