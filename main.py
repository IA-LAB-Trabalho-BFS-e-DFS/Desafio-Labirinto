from algoritmos import (
    generate_maze, 
    bfs_grid, 
    dfs_grid, 
    draw_path, 
    print_grid
)

# ===============================
# EXECUÇÃO DO BENCHMARK
# ===============================
def run_tests():
    sizes = [30, 100, 500]
    
    print("\n" + "="*50)
    print(" INICIANDO TESTE DE ESTRESSE: BFS vs DFS")
    print("="*50)

    for size in sizes:
        rows, cols = size, size
        start = (0, 0)
        goal = (rows - 1, cols - 1)
        
        print(f"\n Gerando matriz {rows}x{cols}... (Pode demorar)")
        maze = generate_maze(rows, cols, 0.30)
        
        found_bfs, path_bfs, time_bfs, mem_cur_bfs, mem_peak_bfs = bfs_grid(maze, start, goal)
        found_dfs, path_dfs, time_dfs, mem_cur_dfs, mem_peak_dfs = dfs_grid(maze, start, goal)
        
        if size == 30:
            if found_bfs:
                print("\n CAMINHO BFS (30x30):")
                print_grid(draw_path(maze, path_bfs))
            
            if found_dfs:
                print("\n CAMINHO DFS (30x30):")
                print_grid(draw_path(maze, path_dfs))
                
        print(f"\n RESULTADOS FINAIS [{rows}x{cols}]:")
        
        peak_bfs_mb = mem_peak_bfs / (1024 * 1024)
        peak_dfs_mb = mem_peak_dfs / (1024 * 1024)
        
        print(f"  | BFS -> Tempo: {time_bfs:.4f}s | Mem. Pico: {peak_bfs_mb:.2f} MB | Passos: {len(path_bfs)}")
        print(f"  | DFS -> Tempo: {time_dfs:.4f}s | Mem. Pico: {peak_dfs_mb:.2f} MB | Passos: {len(path_dfs)}")
        print("-" * 50)
        
    print("\n TESTES FINALIZADOS!\n")

if __name__ == "__main__":
    run_tests()