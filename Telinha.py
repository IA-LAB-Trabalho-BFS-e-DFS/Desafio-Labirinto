from turtle import width

import pygame
import random
from collections import deque
from typing import Tuple, Iterable
import tracemalloc
from time import time
import pandas as pd

# ===============================
# CONFIGURAÇÕES
# ===============================

rows = 30
cols = 30
cell_size = 550//cols

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

def draw_grid(screen, grid, visited, path, cell_size):
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c*cell_size, r*cell_size, cell_size, cell_size)

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
# TELINHA DE CONFIGURAÇÃO
# ===============================
def pedir_dimensoes():
    pygame.init()
    tela = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Configuração do Labirinto")
    
    # Configurações de Estilo
    BRANCO, PRETO, AZUL, CINZA = (255, 255, 255), (0, 0, 0), (0, 200, 0), (100, 149, 237)
    fonte = pygame.font.SysFont("Arial", 24)
    relogio = pygame.time.Clock()

    inputs = {"Largura": "30", "Altura": "30", "Obstáculos%": "30"}
    campo_ativo = "Largura"
    configurando = True

    while configurando:
        tela.fill(BRANCO)
        
        # Renderização de textos e caixas
        img_titulo = fonte.render("Tamanho do Labirinto", True, PRETO)
        tela.blit(img_titulo, (100, 30))

        for i, (label, valor) in enumerate(inputs.items()):
            y_pos = 100 + (i * 70)
            cor = AZUL if campo_ativo == label else CINZA
            
            # Desenha Label e Caixa
            txt_label = fonte.render(f"{label}:", True, PRETO)
            tela.blit(txt_label, (5, y_pos + 5))
            pygame.draw.rect(tela, cor, (160, y_pos, 100, 40), 2)
            
            # Desenha o número digitado
            txt_valor = fonte.render(valor, True, PRETO)
            tela.blit(txt_valor, (200, y_pos + 5))

        txt_info = fonte.render("ENTER para iniciar", True, (100, 100, 100))
        tela.blit(txt_info, (110, 300))

        # Gerenciamento de Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
           
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    # Retorna os valores como inteiros
                    return int(inputs["Largura"]), int(inputs["Altura"]), int(inputs["Obstáculos%"])/100
                
                if evento.key == pygame.K_TAB:
                    if campo_ativo == "Obstáculos%":
                        campo_ativo = "Largura"
                    elif campo_ativo == "Largura":
                        campo_ativo = "Altura"
                    elif campo_ativo == "Altura":
                        campo_ativo = "Obstáculos%"
                
                if evento.key == pygame.K_BACKSPACE:
                    inputs[campo_ativo] = inputs[campo_ativo][:-1]
                
                elif evento.unicode.isdigit() and len(inputs[campo_ativo]) < 3:
                    inputs[campo_ativo] += evento.unicode

        pygame.display.flip()
        relogio.tick(30) # Limita a 30 FPS para economizar CPU

# ===============================
# MAIN
# ===============================

def main():
    df = pd.DataFrame(columns=["Algoritmo", "Passos", "Visitados", "Tempo (s)", "Memória Atual (KB)", "Pico de Memória (KB)"])
    rows, cols,complexidade = pedir_dimensoes()
    pygame.init()
    cell_size = 550 // cols
    width = 600
    height =550
    screen = pygame.display.set_mode((width+70, height + 70))
    pygame.display.set_caption("Busca em Tempo Real - Métricas")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)

    grid = generate_maze(rows, cols,complexidade)
    start = (0, 0)
    goal = (rows-1, cols-1)

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

                if event.key == pygame.K_d:
                    tracemalloc.start()
                    structure = deque([start])
                    visited = {start}
                    parent = {}
                    running_search = True
                    found = False
                    path = []
                    mode = "BFS"
                    steps = 0

                if event.key == pygame.K_b:
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
                    rows, cols,complexidade = pedir_dimensoes()
                    grid = generate_maze(rows, cols,complexidade)
    
                    screen = pygame.display.set_mode((width+70, height + 70))
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
        draw_grid(screen, grid, visited, path, cell_size)
        
        info_text = f"Algoritmo: {mode} | Passos: {steps} | Visitados: {len(visited)}| Tempo: {last_step_time/60:.2f}s | Mem Atual: {current_mem//1024} KB | Pico: {peak_mem//1024} KB"
        df.loc[len(df)] = [mode, steps, visited, f"{last_step_time/60:.2f}", current_mem//1024, peak_mem//1024]    
        text_surface = font.render(info_text, True, (0, 0, 0))
        screen.blit(text_surface, (10, height + 15))

        pygame.display.update()

    tracemalloc.stop()
    pygame.quit()

if __name__ == "__main__":
    main()