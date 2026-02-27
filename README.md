# 📌 Desafio Labirinto – Comparação de BFS e DFS  

*Trabalho de Inteligência Artificial – IA-LAB*

---

## 👥 Integrantes

| Nome | RA |
|------|----|
| Sydhiney Silva | G75EJI5 |
| Eduardo Theodoro | R153FJ3 |
| Ariane Veras | R197123 |
| Victor Donadi | G593IC1 |

---

## 🧠 Sobre o Projeto

Este projeto tem como objetivo implementar e comparar os algoritmos de busca:

- *BFS (Breadth-First Search – Busca em Largura)*
- *DFS (Depth-First Search – Busca em Profundidade)*

Os algoritmos foram aplicados na resolução de um labirinto representado como matriz bidimensional, analisando:

- ✔ Tempo de execução  
- ✔ Consumo de memória  
- ✔ Caminho encontrado  

O trabalho demonstra, na prática, conceitos fundamentais de busca em grafos dentro da área de Inteligência Artificial.

---

## 🔎 Conceitos Utilizados

### 🔹 BFS (Busca em Largura)
Explora o labirinto por níveis, visitando todos os vizinhos antes de avançar.  
Garante o menor caminho em número de passos até o objetivo.

### 🔹 DFS (Busca em Profundidade)
Explora um caminho até o máximo possível antes de retroceder.  
Pode encontrar caminhos mais longos, porém pode utilizar menos memória dependendo do cenário.

---

## 🧱 Representação do Labirinto

O labirinto é representado por uma matriz 2D onde:

| Símbolo | Significado |
|----------|-------------|
| S | Ponto inicial |
| G | Objetivo (saída) |
| . | Caminho livre |
| # | Obstáculo |
| * | Caminho encontrado |

Movimentação permitida:
- Direita
- Esquerda
- Cima
- Baixo
- Diagonais (quando aplicável)

---

## ⚙️ Funcionalidades

- ✅ Geração de labirinto 20x20 com obstáculos aleatórios  
- ✅ Execução dos algoritmos BFS e DFS  
- ✅ Comparação de desempenho  
- ✅ Exibição do caminho encontrado  
- ✅ Medição de tempo e memória  

---

## ▶️ Como Executar

### 📌 Pré-requisitos

- Python 3.8 ou superior instalado

### 📌 Execução

Abra o terminal na pasta do projeto e execute:

bash
python main.py

# COMANDOS

B → iniciar BFS

D → iniciar DFS

R → gerar novo labirinto

ESC → sair


---

## 📁 Estrutura do Projeto


Desafio-Labirinto/
│
├── README.md
├── main.py
├── algoritmos.py
├── Telinha.py
└── __pycache__/


---

## 📊 Objetivo Acadêmico

O principal objetivo deste trabalho é analisar, na prática, as diferenças entre os algoritmos BFS e DFS, observando:

- Eficiência
- Qualidade do caminho encontrado
- Custo computacional

Demonstrando como estratégias diferentes impactam diretamente na solução de problemas
