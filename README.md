# Transformações Lineares: Núcleo e Imagem

Projeto de extensão desenvolvido na disciplina de **Álgebra e Geometria Analítica**, com o objetivo de apresentar os conceitos de **Transformações Lineares**, **Núcleo** e **Imagem** de forma didática e acessível, unindo fundamentação teórica e implementação prática em Python.

---

## Sobre o Projeto

As transformações lineares são funções entre espaços vetoriais que preservam as operações de adição de vetores e multiplicação por escalar, sendo amplamente aplicadas em computação gráfica, desenvolvimento de jogos, robótica, engenharia e inteligência artificial.

Este repositório reúne o material de apoio e o programa interativo em Python desenvolvido para demonstrar passo a passo como uma matriz $2 \times 2$ transforma vetores no plano $\mathbb{R}^2$, além de calcular seu núcleo, sua imagem e suas interpretações geométricas.

---

## Funcionalidades do Programa

O script em Python (`transformacoes_lineares.py`) oferece um menu interativo no terminal com cálculo exato por meio da biblioteca nativa `fractions`, evitando erros de arredondamento de ponto flutuante:

1. **Aplicação de Transformação Linear ($T(v) = A \cdot v$):**
   * Recebe uma matriz $A$ de ordem $2 \times 2$ e um vetor $v = (x, y)$ digitados pelo usuário.
   * Exibe o passo a passo da multiplicação de cada linha da matriz pelas coordenadas do vetor.
2. **Verificação das Condições de Linearidade:**
   * Testa numericamente, para vetores $u, v \in \mathbb{R}^2$ e escalares $\alpha, \beta \in \mathbb{R}$ informados pelo usuário:
     * **Aditividade:** $T(u + v) = T(u) + T(v)$
     * **Homogeneidade:** $T(\alpha u) = \alpha T(u)$
     * **Princípio da Superposição:** $T(\alpha u + \beta v) = \alpha T(u) + \beta T(v)$
3. **Cálculo do Núcleo ($\text{Ker}(T)$):**
   * Resolve o sistema linear homogêneo $A \cdot v = 0$ em 4 etapas didáticas.
   * Identifica a base, a representação paramétrica e a dimensão $\dim(\text{Ker}(T))$.
4. **Cálculo da Imagem ($\text{Im}(T)$):**
   * Analisa a independência linear das colunas da matriz $A$ em 4 etapas.
   * Determina a base, o conjunto imagem e a dimensão $\dim(\text{Im}(T))$.
5. **Conferência pelo Teorema do Núcleo e da Imagem:**
   * Valida automaticamente a relação fundamental no plano:
     $$\dim(\text{Ker}(T)) + \dim(\text{Im}(T)) = \dim(\mathbb{R}^2) = 2$$
6. **Transformações Geométricas no Plano:**
   * Aplica a um vetor informado pelo usuário as matrizes clássicas de **ampliação**, **redução**, **reflexão** (eixos $X$ e $Y$), **rotação** ($90^\circ$, $180^\circ$ e $360^\circ$) e **cisalhamento**.
7. **Exemplos Prontos dos Slides:**
   * Opção dedicada para reproduzir instantaneamente os exemplos teóricos apresentados nos slides do trabalho.

---

## Pré-requisitos e Instalação

O projeto utiliza exclusivamente módulos nativos da biblioteca padrão do Python (`math` e `fractions`), **não sendo necessária a instalação de pacotes externos**.

* **Requisito:** Python $3.10$ ou superior.

### Passo a passo para executar

1. Clone este repositório ou baixe os arquivos para o seu computador:
   ```bash
   git clone https://github.com/seu-usuario/transformacoes-lineares-python.git
   cd transformacoes-lineares-python
   ```

2. Execute o programa pelo terminal:
   ```bash
   python transformacoes_lineares.py
   ```
   *(Em sistemas Linux ou macOS, utilize `python3 transformacoes_lineares.py` caso necessário.)*

---

## Como Inserir Valores

Durante a execução interativa, o programa aceita diferentes formatos numéricos para elementos de matrizes, coordenadas de vetores e escalares:

* **Números inteiros:** `2`, `-3`, `0`
* **Frações:** `1/2`, `-3/4`
* **Decimais (com ponto ou vírgula):** `0.5`, `0,5`, `-1.25`

Caso algum valor inválido seja digitado (como letras ou divisão por zero), o programa exibe um aviso e solicita novamente apenas aquele campo.

---

## Exemplo de Execução

Ao escolher a **Opção 1** no menu e inserir a matriz $A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ com o vetor $v = (2, 1)$, o terminal exibe:

```text
--- Cálculo do Núcleo: Ker(T) ---
Passo 1: Representar a transformação pela matriz:
Matriz A:
  [    1     2 ]
  [    2     4 ]
Passo 2: Igualar o resultado a zero (A · v = 0):
  (1)x + (2)y = 0
  (2)x + (4)y = 0
Passo 3: Resolver o sistema linear homogêneo:
  Isolando x na equação (1)x + (2)y = 0:
  x = -2y
  Substituindo y = t: x = -2t, y = t
Passo 4: Resultado do núcleo:
  Base de Ker(T) = {(-2, 1)}
  Ker(T) = {(-2t, t) | t ∈ R}  (Dimensão = 1)

--- Cálculo da Imagem: Im(T) ---
Passo 1: Identificar as colunas da matriz:
  C1 = (1, 2)   e   C2 = (2, 4)
Passo 2: Verificar se as colunas são linearmente independentes (LI):
  Dependência linear encontrada: C2 = 2 × C1 ((2, 4) = 2 × (1, 2)).
Passo 3: Identificar a coluna independente:
  Base da imagem = {(1, 2)}
Passo 4: Resultado da imagem:
  Im(T) = {(t, 2t) | t ∈ R}  (Dimensão = 1)

Conferência (Teorema do Núcleo e da Imagem): 1 + 1 = 2 = dim(R²)
```

---

## Estrutura Sugerida do Repositório

```text
├── transformacoes_lineares.py   # Código-fonte principal com menu interativo
├── README.md                    # Documentação geral do projeto
├── ROTEIRO_VIDEO.md             # Guia de apoio para apresentação e gravação do vídeo
└── Trabalho Algebra.pptx        # Slides teóricos do projeto de extensão
```

---

## Autores

Projeto desenvolvido pelos acadêmicos:

* **Gustavo Milczvsky Pykocz**
* **Julia Gabrielli Liebl**
* **Luis Cesar Woehl**
* **Pamela Pereira**
* **Renan Ramos**

---

## Licença

Este projeto é de uso educacional e está disponibilizado sob a licença **MIT**.