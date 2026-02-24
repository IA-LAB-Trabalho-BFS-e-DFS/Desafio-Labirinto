from collections import deque
from typing import Dict, List, Tuple, Set
from time import time
from typing import Iterable
import tracemalloc




# ------ 1 a 3 --------
# AQUI SÃO FUNÇÕES VOLTADAS PARA UM GRAFO


# goal = o que pediram 
# start = fazendo
# current = estado atual
# path = o balde que armazena as infromações

def reconstruct_path(parent: Dict, start, goal) -> List:
    """Reconstrói o caminho do start até o goal usando o mapa parent."""
    if goal not in parent and goal != start:
        return []  # não encontrado

    path = [goal]
    current = goal
    
    while current != start:
        current = parent[current]
        # está colocando a busca dentro da lista Path
        path.append(current)
    path.reverse()
    return path

# tuple serve para não modificar a lista é identificada por ()
def bfs(graph: Dict, start, goal) -> Tuple[bool, List]:
    """BFS clássico: retorna (encontrou?, caminho)."""
    tracemalloc.start()
    inicio = time()
    queue = deque([start])
    visited: Set = {start}
    parent: Dict = {}  # parent[v] = u (de onde viemos para chegar em v)
    
    while queue:
        u = queue.popleft()
        if u == goal:
            lista = [x for x in range(100000)]
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            for stat in top_stats[:3]:
                 print(stat)
            end = time()
            print(f"BFS Tempo gasto: {end - inicio:.4f} segundos")
            return True, reconstruct_path(parent, start, goal)
        for v in graph.get(u, []):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)

    # Seu código aqui
    lista = [x for x in range(100000)]
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    print(top_stats)
    print(f"BFS Tempo gasto: {end - inicio:.4f} segundos")
    return False, []

def dfs_iterative(graph: Dict, start, goal) -> Tuple[bool, List]:
    """DFS iterativo: retorna (encontrou?, caminho)."""
    inicio = time()
    stack = [start]
    visited: Set = {start}
    parent: Dict = {}

    while stack:
        u = stack.pop()  # LIFO
        if u == goal:
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            print(top_stats)
            end = time()
            print(f"DFS Tempo gasto: {end - inicio:.4f} segundos")
            return True, reconstruct_path(parent, start, goal)
        # Para DFS ficar mais previsível, podemos iterar vizinhos em ordem reversa
        # (assim o primeiro vizinho da lista tende a ser explorado primeiro).
        for v in reversed(graph.get(u, [])):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                stack.append(v)


# --------------------- A PARTE 4 ------------------
# AGORA SÃO FUNÇÕES VOLTADAS A UMA MATRIZ (GRID)


# 4.1 - Modelagem como espaço de estados
def find_char(grid, ch: str) -> Tuple[int, int]:
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ch:
                return (r, c)
    raise ValueError(f"Caractere {ch} não encontrado.")



# 4.2 - Função sucessora (gerar próximos estados)
def neighbors(pos: Tuple[int,int], grid) -> Iterable[Tuple[int,int]]:
    r, c = pos
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:  # cima, baixo, esq, dir
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] != '#':  # não atravessa parede
                yield (nr, nc)




# 4.3 - BFS e DFS no labirinto (com reconstrução de caminho)
def reconstruct_path_grid(parent: Dict[Tuple[int,int], Tuple[int,int]], start, goal) -> List[Tuple[int,int]]:
    if goal not in parent and goal != start:
        return []
    path = [goal]
    cur = goal
    while cur != start:
        cur = parent[cur]
        path.append(cur)
    path.reverse()
    return path

def bfs_grid(grid, start, goal):
    q = deque([start])
    visited = {start}
    parent = {}

    while q:
        u = q.popleft()
        if u == goal:
            return True, reconstruct_path_grid(parent, start, goal)

        for v in neighbors(u, grid):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                q.append(v)

    return False, []

def dfs_grid(grid, start, goal):
    stack = [start]
    visited = {start}
    parent = {}

    while stack:
        u = stack.pop()
        if u == goal:
            return True, reconstruct_path_grid(parent, start, goal)

        # ordem reversa para deixar o comportamento mais reprodutível
        for v in reversed(list(neighbors(u, grid))):
            if v not in visited:
                visited.add(v)
                parent[v] = u
                stack.append(v)

    return False, []



# 4.4 - Visualização do caminho encontrado
def draw_path(grid, path: List[Tuple[int,int]]) -> List[List[str]]:
    g = [row[:] for row in grid]
    for (r,c) in path:
        if g[r][c] not in ("S", "G"):
            g[r][c] = "*"
    return g

def print_grid(grid):
    for row in grid:
        print("".join(row))