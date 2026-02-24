from algoritmos import bfs, dfs_iterative 


# Exemplo simples de grafo (não é árvore binária; é um grafo geral)
graph_example = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


found_bfs, path_bfs = bfs(graph_example, "A", "F")
found_dfs, path_dfs = dfs_iterative(graph_example, "A", "F")


print (found_bfs, path_bfs, found_dfs, path_dfs)



# 0 = Caminho livre
# 1 = Parede (Obstáculo)

maze_example = [
    [0, 1, 0, 0, 0],  # Linha 0
    [0, 1, 0, 1, 0],  # Linha 1
    [0, 0, 0, 1, 0],  # Linha 2 (Start deve ser aqui, ex: 2,0)
    [0, 1, 1, 1, 0],  # Linha 3
    [0, 0, 0, 0, 0]   # Linha 4 (Goal pode ser aqui, ex: 4,4)
]

# Para acessar a posição (Linha 2, Coluna 0):
print(maze_example[2][0])  # Saída: 0 (Livre)
print(maze_example[0][1])  # Saída: 1 (Parede)