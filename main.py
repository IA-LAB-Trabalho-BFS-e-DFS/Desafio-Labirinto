from algoritmos import (
    generate_maze,
    bfs_grid,
    dfs_grid,
    draw_path,
    print_grid
)

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