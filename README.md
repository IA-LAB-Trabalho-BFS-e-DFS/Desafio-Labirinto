# 📌 Desafio Labirinto – Comparação de BFS e DFS

Este projeto implementa os algoritmos de busca **Breadth-First Search (BFS)** e **Depth-First Search (DFS)** para resolver um labirinto representado como uma matriz bidimensional, comparando desempenho, uso de memória e os caminhos encontrados.

---

## 🧠 Sobre o Projeto

O objetivo é comparar dois algoritmos clássicos de busca em grafos:

- **BFS (Busca em Largura):** Explora o labirinto por “ondas”, garantindo o menor caminho em número de passos.
- **DFS (Busca em Profundidade):** Explora caminhos até não poder mais e só então volta; não garante menor caminho.

O projeto mede, além do caminho:
- Tempo de execução
- Consumo de memória

---

## 🧱 Representação do Labirinto

O labirinto é uma matriz 2D onde cada célula pode ser:

| Símbolo | Significado        |
|----------|-------------------|
| S        | Ponto inicial     |
| G        | Objetivo/saída    |
| .        | Caminho livre     |
| #        | Obstáculo         |
| *        | Caminho encontrado|

Movimentos permitidos incluem **8 direções** (ortogonais + diagonais).

---

## 🚀 Funcionalidades

✔ Geração de labirinto 20×20 com obstáculos aleatórios  
✔ Execução de BFS e DFS  
✔ Medição de tempo e memória  
✔ Exibição do caminho no terminal  

---

## 🧪 Como Executar

### 🔧 Requisitos
- Python 3.8+

### ▶️ Execução

```bash
python main.py