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

# 🧠 Sobre o Projeto

---

Este projeto tem como objetivo implementar e comparar os algoritmos de busca:

BFS (Breadth-First Search – Busca em Largura)

DFS (Depth-First Search – Busca em Profundidade)

Os algoritmos foram aplicados na resolução de um labirinto representado como matriz bidimensional, analisando:

✔ Tempo de execução

✔ Consumo de memória

✔ Caminho encontrado

✔ Complexidade assintótica (Big-O)

O trabalho demonstra, na prática, conceitos fundamentais de busca em grafos dentro da área de Inteligência Artificial.

---

# 🖥️ Parte Principal – Telinha.py
---
O arquivo Telinha.py é responsável pela interface gráfica do projeto e pela execução interativa dos algoritmos.

Ele permite:

Definir largura do labirinto

Definir altura do labirinto

Definir porcentagem de obstáculos

Executar BFS ou DFS

Resetar o sistema

## ▶️ Como Usar o Telinha.py

Execute no terminal:

python Telinha.py
## 📌 Inserindo os valores

Ao abrir o programa:

Na primeira caixa (largura).

Para alterar o número:

⚠ Apague o número atual primeiro

Depois digite o novo valor.

Para ir para a próxima caixa (altura):

Pressione TAB

Repita o mesmo processo:

Apague o número

Digite o novo valor

Para ir para a próxima caixa (porcentagem de labirinto):

Pressione TAB novamente

Apague o valor atual

Digite o novo valor

## 🎮 Comandos Durante a Execução

Após gerar o labirinto:

Tecla	Função

D	Executa o DFS

B	Executa o BFS

R	Reseta e volta para a tela inicial

ESC	Fecha o programa

Quando:

Pressionar D, o algoritmo BFS será executado.

Pressionar B, o algoritmo DFS será executado.

Pressionar R, o programa retorna para a tela de configuração de largura, altura e porcentagem.

---

# 🔎 Conceitos Utilizados

---

## 🔹 BFS (Busca em Largura)

Explora o labirinto por níveis, visitando todos os vizinhos antes de avançar para o próximo nível.

Utiliza fila (Queue)

Garante o menor caminho em número de passos

Pode consumir mais memória dependendo do tamanho do labirinto

## 🔹 DFS (Busca em Profundidade)

Explora um caminho até o máximo possível antes de retroceder.

Utiliza pilha (Stack) ou recursão

Pode encontrar caminhos mais longos

Em alguns casos pode utilizar menos memória que o BFS

## 🧱 Representação do Labirinto

O labirinto é representado por uma matriz 2D onde:

### Símbolo	Significado:

'S'	Ponto inicial

'G'	Objetivo (saída)

'.'	Caminho livre

'#' Obstaculo

'*'	Caminho encontrado

### Movimentação permitida:

Direita

Esquerda

Cima

Baixo

---

# 📊 Gráfico - analise_big_o.py

---

A pasta analise_big_o contém o arquivo responsável por gerar o gráfico comparativo de desempenho dos algoritmos.

Para executar:

python analise_big_o.py
## 📈 Sobre o Gráfico Gerado

O script gera um gráfico que demonstra:

Crescimento do tempo de execução

Comportamento dos algoritmos conforme o tamanho do labirinto aumenta

O gráfico evidencia que tanto o BFS quanto o DFS possuem complexidade:

## 🧮 O(N²)

Isso ocorre porque:

O labirinto é representado por uma matriz N x N

No pior caso, todos os nós (células) precisam ser visitados

Logo, o número total de operações cresce proporcionalmente ao número de células da matriz

Se temos um labirinto 20x20:

Total de posições = 400

Complexidade proporcional a N²

---
#  ▶️ Execução do Programa - main.py
---

A execução da aplicação é iniciada na função main, que atua como ponto central de controle do sistema. Essa função é responsável por configurar o ambiente de execução, coletar os parâmetros necessários, gerar o labirinto e executar o algoritmo de busca escolhido pelo usuário.

## Responsabilidades da função main

A função main realiza, de forma sequencial, as seguintes operações:

### Definição dos parâmetros do labirinto
O usuário informa:

Altura do labirinto.

Largura do labirinto.

Porcentagem de chance de bloqueios nas células.

Esses parâmetros determinam o tamanho do espaço de busca e influenciam diretamente a complexidade do problema.

### Geração do labirinto
A partir dos valores informados, o sistema cria um labirinto bidimensional contendo:

Caminhos livres.

Bloqueios gerados de forma probabilística.

Ponto inicial (origem).

Ponto objetivo (destino).

### Escolha do algoritmo de busca
O usuário seleciona qual estratégia será utilizada para percorrer o labirinto:

D — Executa DFS (Depth-First Search), priorizando exploração em profundidade.

B — Executa BFS (Breadth-First Search), priorizando exploração por níveis.

### Execução da busca
O algoritmo selecionado é executado sobre o labirinto gerado. Durante a execução, o sistema processa os nós visitados, controla a fronteira de exploração e reconstrói o caminho até o objetivo quando uma solução é encontrada.

### Exibição dos resultados
Ao final da execução, o programa apresenta:

O labirinto gerado.

O caminho encontrado (quando existente).

Indicação de falha quando não há solução possível.

## Estrutura de inicialização

A aplicação utiliza a estrutura padrão de entrada em Python:

if __name__ == "__main__":
    main()

Essa abordagem garante que a função main seja executada apenas quando o arquivo é executado diretamente, permitindo que os módulos do projeto sejam reutilizados sem disparar a execução automática.

## Observações sobre complexidade

Os parâmetros definidos na main impactam diretamente o custo computacional:

Labirintos maiores aumentam o espaço de estados.

Maior porcentagem de bloqueios tende a:

Aumentar a dificuldade da busca.

Elevar o número de tentativas exploratórias.

Possivelmente impedir a existência de solução.

A escolha entre BFS e DFS altera o comportamento:

BFS tende a encontrar o menor caminho, porém consome mais memória.

DFS utiliza menos memória, mas pode explorar caminhos longos antes de encontrar a solução.

Assim, a função main não apenas inicia o programa, mas define as condições que determinam o desempenho e a complexidade da execução.

---

# 🧠 Algoritmos (BackEnd)- algoritmos.py 

---

O arquivo algoritmos.py representa o núcleo lógico da aplicação, funcionando como o backend responsável pela inteligência de busca no labirinto.
Enquanto a interface (ex.: telinha.py) cuida da interação com o usuário e visualização, este módulo implementa as regras, estruturas de dados e algoritmos que resolvem o problema.

Em outras palavras, é neste arquivo que ocorre o processamento principal da busca por caminhos.

## 🎯 Responsabilidade do módulo

O algoritmos.py é responsável por:

Implementar os algoritmos de busca (BFS e DFS).

Definir a lógica de exploração do labirinto.

Controlar nós visitados.

Gerenciar a fronteira de busca.

Reconstruir o caminho encontrado.

Retornar resultados para a camada de interface.

Esse desacoplamento caracteriza uma separação clara entre interface (frontend) e lógica (backend), tornando o projeto mais organizado, reutilizável e fácil de manter.

## 🧩 Estruturas e conceitos utilizados

O módulo normalmente trabalha com conceitos clássicos de busca em grafos:

Estado / nó → posição atual no labirinto.

Vizinhos → células adjacentes válidas.

Fronteira → conjunto de estados a explorar.

Visitados → evita ciclos e repetição.

Pais (parent) → permite reconstruir o caminho final.

Esses elementos formam a base para ambos os algoritmos.

## 🔎 BFS — Breadth-First Search

A BFS realiza uma busca em largura, explorando o labirinto por camadas.

### Características:

Utiliza fila (queue).

Garante o menor caminho em grafos não ponderados.

Explora todos os vizinhos antes de aprofundar.

Consome mais memória.

### Papel no projeto:

No contexto do labirinto, a BFS é utilizada quando o objetivo é encontrar o caminho mais curto entre origem e destino.

## 🌲 DFS — Depth-First Search

A DFS realiza uma busca em profundidade, avançando o máximo possível antes de retroceder.

### Características:

Utiliza pilha (stack) ou recursão.

Pode encontrar uma solução rapidamente.

Não garante o menor caminho.

Geralmente usa menos memória.

### Papel no projeto:

A DFS é útil para explorar rapidamente o espaço de busca e visualizar comportamentos diferentes de exploração no labirinto.

## 🧭 Reconstrução de caminho

Uma parte essencial do backend é a reconstrução do caminho.

O módulo mantém um mapeamento de pais (parent map), que registra de onde cada nó foi alcançado. Quando o objetivo é encontrado, o caminho é reconstruído percorrendo esse mapa do destino até a origem.

Isso permite que a interface visualize o trajeto final.

## 🔄 Comunicação com a interface

O algoritmos.py não lida com entrada do usuário nem renderização.
Ele recebe dados e devolve resultados, por exemplo:

Labirinto.

Posição inicial.

Posição final.

Caminho encontrado.

Estados visitados.

Essa abordagem caracteriza o módulo como backend lógico, enquanto telinha.py atua como camada de apresentação.

## ⚙️ Impacto na complexidade

O desempenho dos algoritmos implementados neste arquivo depende diretamente de:

Tamanho do labirinto.

Densidade de bloqueios.

Estrutura do grafo gerado.

Algoritmo selecionado (BFS vs DFS).

Em termos gerais:

BFS → maior uso de memória, menor caminho garantido.

DFS → menor memória, solução não necessariamente ótima.

---

# 📁 Estrutura do Projeto

---
Desafio-Labirinto/

│

├── README.md

├── Telinha.py

├── algoritmos.py

├── analise_big_o/

│   └── analise_big_o.py

└── __pycache__/

---

# 🎯 Objetivo Acadêmico

---

O principal objetivo deste trabalho é analisar, na prática, as diferenças entre os algoritmos BFS e DFS, observando:

Eficiência

Qualidade do caminho encontrado

Custo computacional

Crescimento assintótico (Big-O)

Demonstrando como estratégias diferentes impactam diretamente na solução de problemas dentro da Inteligência Artificial.
