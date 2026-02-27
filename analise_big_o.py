import matplotlib.pyplot as plt
import numpy as np
from algoritmos import generate_maze, bfs_grid

# =============================
# TAMANHOS PARA TESTE
# =============================
tamanhos = [50, 100, 200, 400, 800]

tempos_bfs = []

# =============================
# COLETANDO TEMPOS REAIS
# =============================
for n in tamanhos:
    print(f"Testando {n}x{n}")
    
    maze = generate_maze(n, n, 0.30)
    start = (0, 0)
    goal = (n - 1, n - 1)

    found, path, tempo, mem_current, mem_peak = bfs_grid(maze, start, goal)
    
    tempos_bfs.append(tempo)

# =============================
# FUNÇÕES TEÓRICAS
# =============================
f_n = [n for n in tamanhos]
f_nlogn = [n * np.log(n) for n in tamanhos]
f_n2 = [n**2 for n in tamanhos]

# =============================
# ESCALANDO CURVAS
# =============================
def escalar(func, dados_reais):
    fator = dados_reais[-1] / func[-1]
    return [fator * x for x in func]

f_n_s = escalar(f_n, tempos_bfs)
f_nlogn_s = escalar(f_nlogn, tempos_bfs)
f_n2_s = escalar(f_n2, tempos_bfs)

# =============================
# GRÁFICO COMPARATIVO
# =============================
plt.figure(figsize=(10,6))

plt.plot(tamanhos, tempos_bfs, 'o-', label="Tempo Real BFS", linewidth=3)

plt.plot(tamanhos, f_n_s, '--', label="O(N)")
plt.plot(tamanhos, f_nlogn_s, '--', label="O(N log N)")
plt.plot(tamanhos, f_n2_s, '--', label="O(N²)")

plt.xlabel("Tamanho do Labirinto (N)")
plt.ylabel("Tempo (segundos)")
plt.title("Comparação Experimental com Notações Big-O")
plt.legend()
plt.grid(True)
plt.show()