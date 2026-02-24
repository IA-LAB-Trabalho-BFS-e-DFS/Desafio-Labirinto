README — Comparação de BFS e DFS em Labirinto com Movimentos Diagonais
1. Descrição do Projeto

Este projeto implementa os algoritmos de busca BFS (Breadth-First Search) e DFS (Depth-First Search) para resolver um labirinto representado como uma matriz bidimensional.

O sistema:

Gera um labirinto 20x20 com obstáculos aleatórios

Permite movimentos ortogonais e diagonais (8 direções)

Encontra caminho do ponto inicial S até o objetivo G

Mede tempo de execução

Compara número de passos entre BFS e DFS

Exibe visualmente o caminho encontrado

2. Objetivos

Comparar comportamento de BFS e DFS

Analisar diferença de desempenho

Verificar impacto de obstáculos

Avaliar complexidade assintótica (Big-O)

Estudar consumo de memória

3. Representação do Labirinto

O labirinto é uma matriz onde:

S → Ponto inicial

G → Objetivo

. → Caminho livre

# → Obstáculo

* → Caminho encontrado

Exemplo:

S..#.#.
.##.#..
..###..
##.##.#
...#..G
4. Movimentos Permitidos

O algoritmo permite 8 direções:

Cima

Baixo

Esquerda

Direita

Diagonal superior esquerda

Diagonal superior direita

Diagonal inferior esquerda

Diagonal inferior direita

5. Como Executar
Requisitos

Python 3.8 ou superior

Execução

No terminal:

python main.py

O programa irá:

Gerar o labirinto

Executar BFS

Executar DFS

Mostrar resultados no terminal

6. Estrutura do Projeto
project/
│
├── main.py
├── README.md

Funções principais:

generate_maze() → cria labirinto aleatório

neighbors() → gera estados sucessores

bfs_grid() → busca em largura

dfs_grid() → busca em profundidade

reconstruct_path() → reconstrói o caminho

draw_path() → desenha caminho encontrado

7. Comparação BFS vs DFS
Critério	BFS	DFS
Garante menor caminho	Sim	Não
Estrutura usada	Fila	Pilha
Consumo de memória	Maior	Menor
Pode se perder em caminhos longos	Não	Sim
Performance prática	Estável	Depende da ordem
8. Complexidade Assintótica (Big-O)

Considere:

V = número de células livres

E = número de conexões possíveis

Complexidade de Tempo

Para ambos:

O(V + E)

Como em grid cada célula tem no máximo 8 vizinhos:

E ≤ 8V

Logo:

O(V)
Complexidade de Memória

BFS → O(V) (armazenamento da fila)

DFS → O(V) (armazenamento da pilha)

Na prática:

BFS consome mais memória

DFS consome menos memória, mas pode explorar caminhos longos desnecessários

9. Experimento Realizado

O programa mede:

Tempo de execução

Número de passos do caminho

Resultados típicos:

BFS -> Encontrou: True | Passos: 24 | Tempo: 0.00041s | Memória atual: 12.45 KB | Pico memória: 18.72 KB
DFS -> Encontrou: True | Passos: 51 | Tempo: 0.00039s | Memória atual: 8.11 KB | Pico memória: 12.03 KB

Observação:

BFS tende a produzir menor número de passos.

DFS pode produzir caminhos significativamente maiores.

10. Conclusão

BFS é mais indicado quando é necessário o menor caminho.

DFS é mais simples e pode ser útil quando memória é limitada.

Ambos possuem mesma complexidade assintótica.

Diferença prática depende da estrutura do labirinto.
