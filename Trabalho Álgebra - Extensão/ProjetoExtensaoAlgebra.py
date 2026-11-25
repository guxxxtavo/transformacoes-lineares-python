import math
from fractions import Fraction


def formatar_num(valor: Fraction) -> str:
    """Formata números inteiros ou frações de forma limpa."""
    valor = Fraction(valor).limit_denominator()
    if valor.denominator == 1:
        return str(valor.numerator)
    return f"{valor.numerator}/{valor.denominator}"


def formatar_vetor(v: list[Fraction]) -> str:
    """Formata um vetor 2D para exibição."""
    return f"({formatar_num(v[0])}, {formatar_num(v[1])})"


def formatar_termo_param(coef: Fraction, param: str = "t") -> str:
    """Formata termos paramétricos como '-2t', 't' ou '0'."""
    if coef == 0:
        return "0"
    if coef == 1:
        return param
    if coef == -1:
        return f"-{param}"
    return f"{formatar_num(coef)}{param}"


def exibir_matriz(A: list[list[Fraction]], nome: str = "A") -> None:
    """Exibe uma matriz 2x2 formatada."""
    print(f"Matriz {nome}:")
    for linha in A:
        print(f"  [ {formatar_num(linha[0]):>4}  {formatar_num(linha[1]):>4} ]")


# 0. FUNÇÕES DE ENTRADA DO USUÁRIO (COM VALIDAÇÃO) -------------------------------------------------------------------------------------------------------------


def ler_fracao(mensagem: str) -> Fraction:
    """Lê um número inteiro, decimal (com ponto ou vírgula) ou fração do usuário."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        if not entrada:
            print("  Entrada vazia. Digite um número (ex: 2, -3, 0.5 ou 1/2).")
            continue
        try:
            return Fraction(entrada)
        except (ValueError, ZeroDivisionError):
            print("  Valor inválido. Digite um inteiro, decimal ou fração válida (ex: 1/2).")


def ler_matriz_2x2() -> list[list[Fraction]]:
    """Lê os 4 elementos de uma matriz 2x2 digitados pelo usuário."""
    print("\nDigite os valores da matriz A = [[a, b], [c, d]] (aceita inteiros, decimais ou frações):")
    a = ler_fracao("  Elemento a (linha 1, coluna 1): ")
    b = ler_fracao("  Elemento b (linha 1, coluna 2): ")
    c = ler_fracao("  Elemento c (linha 2, coluna 1): ")
    d = ler_fracao("  Elemento d (linha 2, coluna 2): ")
    matriz = [[a, b], [c, d]]
    exibir_matriz(matriz)
    return matriz


def ler_vetor_2d(nome: str = "v") -> list[Fraction]:
    """Lê as coordenadas x e y de um vetor 2D digitadas pelo usuário."""
    print(f"\nDigite as coordenadas do vetor {nome} = (x, y):")
    x = ler_fracao(f"  Coordenada x de {nome}: ")
    y = ler_fracao(f"  Coordenada y de {nome}: ")
    return [x, y]


# 1. REPRESENTAÇÃO DE MATRIZ E MULTIPLICAÇÃO POR VETOR -----------------------------------------------------------------------------------------------------------


def aplicar_transformacao(
    A: list[list[Fraction]], v: list[Fraction], mostrar_passos: bool = True
) -> list[Fraction]:
    """Calcula T(v) = A * v para uma matriz 2x2 e um vetor v = [x, y]^T."""
    a, b = A[0]
    c, d = A[1]
    x, y = v

    x_linha = a * x + b * y
    y_linha = c * x + d * y
    resultado = [x_linha, y_linha]

    if mostrar_passos:
        print("\n--- Aplicação da Transformação Linear: T(v) = A · v ---")
        exibir_matriz(A)
        print(f"Vetor inicial v = {formatar_vetor(v)}")
        print(
            f"Primeira coordenada: x' = ({formatar_num(a)})×({formatar_num(x)}) + "
            f"({formatar_num(b)})×({formatar_num(y)}) = {formatar_num(x_linha)}"
        )
        print(
            f"Segunda coordenada:  y' = ({formatar_num(c)})×({formatar_num(x)}) + "
            f"({formatar_num(d)})×({formatar_num(y)}) = {formatar_num(y_linha)}"
        )
        print(f"Vetor transformado T(v) = {formatar_vetor(resultado)}")

    return resultado


# 2. CONDIÇÕES PARA UMA TRANSFORMAÇÃO SER LINEAR ------------------------------------------------------------------------------------------------------


def verificar_linearidade(
    A: list[list[Fraction]],
    u: list[Fraction],
    v: list[Fraction],
    alpha: Fraction,
    beta: Fraction,
) -> bool:
    """Verifica Aditividade, Homogeneidade e o Princípio da Superposição."""
    print("\n--- Verificação das Condições de Linearidade ---")
    print(
        f"Vetores: u = {formatar_vetor(u)}, v = {formatar_vetor(v)} | "
        f"Escalares: α = {formatar_num(alpha)}, β = {formatar_num(beta)}"
    )

    # 1. Aditividade: T(u + v) = T(u) + T(v)
    u_mais_v = [u[0] + v[0], u[1] + v[1]]
    t_soma = aplicar_transformacao(A, u_mais_v, mostrar_passos=False)
    t_u = aplicar_transformacao(A, u, mostrar_passos=False)
    t_v = aplicar_transformacao(A, v, mostrar_passos=False)
    soma_t = [t_u[0] + t_v[0], t_u[1] + t_v[1]]
    aditividade_ok = t_soma == soma_t
    print(
        f"1. Aditividade: T(u + v) = {formatar_vetor(t_soma)}  |  "
        f"T(u) + T(v) = {formatar_vetor(soma_t)} -> {'OK' if aditividade_ok else 'Falhou'}"
    )

    # 2. Homogeneidade: T(αu) = αT(u)
    alpha_u = [alpha * u[0], alpha * u[1]]
    t_alpha_u = aplicar_transformacao(A, alpha_u, mostrar_passos=False)
    alpha_t_u = [alpha * t_u[0], alpha * t_u[1]]
    homogeneidade_ok = t_alpha_u == alpha_t_u
    print(
        f"2. Homogeneidade: T(αu) = {formatar_vetor(t_alpha_u)}  |  "
        f"αT(u) = {formatar_vetor(alpha_t_u)} -> {'OK' if homogeneidade_ok else 'Falhou'}"
    )

    # 3. Princípio da Superposição: T(αu + βv) = αT(u) + βT(v)
    comb_linear = [alpha * u[0] + beta * v[0], alpha * u[1] + beta * v[1]]
    t_comb = aplicar_transformacao(A, comb_linear, mostrar_passos=False)
    comb_t = [alpha * t_u[0] + beta * t_v[0], alpha * t_u[1] + beta * t_v[1]]
    superposicao_ok = t_comb == comb_t
    print(
        f"3. Superposição: T(αu + βv) = {formatar_vetor(t_comb)}  |  "
        f"αT(u) + βT(v) = {formatar_vetor(comb_t)} -> {'OK' if superposicao_ok else 'Falhou'}"
    )

    return aditividade_ok and homogeneidade_ok and superposicao_ok


# 3. CÁLCULO DO NÚCLEO - Ker(T) (Slides 19 e 20) ------------------------------------------------------------------------------------------------------------


def calcular_nucleo(A: list[list[Fraction]]) -> int:
    """Calcula o Núcleo Ker(T) = {v ∈ R² | T(v) = 0} seguindo os 4 passos."""
    a, b = A[0]
    c, d = A[1]
    det = a * d - b * c

    print("\n--- Cálculo do Núcleo: Ker(T) ---")
    print("Passo 1: Representar a transformação pela matriz:")
    exibir_matriz(A)

    print("Passo 2: Igualar o resultado a zero (A · v = 0):")
    print(f"  ({formatar_num(a)})x + ({formatar_num(b)})y = 0")
    print(f"  ({formatar_num(c)})x + ({formatar_num(d)})y = 0")

    print("Passo 3: Resolver o sistema linear homogêneo:")
    if a == 0 and b == 0 and c == 0 and d == 0:
        print("  Todas as equações são identicamente nulas (0 = 0). x e y são livres.")
        print("Passo 4: Resultado do núcleo:")
        print("  Base de Ker(T) = {(1, 0), (0, 1)}")
        print("  Ker(T) = {(s, t) | s, t ∈ R} = R²  (Dimensão = 2)")
        return 2

    if det != 0:
        print(
            f"  Determinante det(A) = {formatar_num(det)} ≠ 0. "
            "O sistema admite apenas a solução trivial (x = 0, y = 0)."
        )
        print("Passo 4: Resultado do núcleo:")
        print("  Base de Ker(T) = ∅")
        print("  Ker(T) = {(0, 0)}  (Dimensão = 0)")
        return 0

    linha_nao_nula = (a, b) if (a != 0 or b != 0) else (c, d)
    r1, r2 = linha_nao_nula

    if r1 != 0:
        fator = -r2 / r1
        print(f"  Isolando x na equação ({formatar_num(r1)})x + ({formatar_num(r2)})y = 0:")
        print(f"  x = {formatar_termo_param(fator, 'y')}")
        print(f"  Substituindo y = t: x = {formatar_termo_param(fator, 't')}, y = t")
        gerador = [fator, Fraction(1)]
    else:
        print(f"  Da equação ({formatar_num(r2)})y = 0, temos y = 0 e x = t livre.")
        gerador = [Fraction(1), Fraction(0)]

    print("Passo 4: Resultado do núcleo:")
    print(f"  Base de Ker(T) = {{{formatar_vetor(gerador)}}}")
    print(
        f"  Ker(T) = {{({formatar_termo_param(gerador[0], 't')}, "
        f"{formatar_termo_param(gerador[1], 't')}) | t ∈ R}}  (Dimensão = 1)"
    )
    return 1


# 4. CÁLCULO DA IMAGEM - Im(T) -----------------------------------------------------------------------------------------------------------------------------------


def calcular_imagem(A: list[list[Fraction]]) -> int:
    """Calcula a Imagem Im(T) a partir da independência linear das colunas."""
    c1 = [A[0][0], A[1][0]]
    c2 = [A[0][1], A[1][1]]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]

    print("\n--- Cálculo da Imagem: Im(T) ---")
    print("Passo 1: Identificar as colunas da matriz:")
    print(f"  C1 = {formatar_vetor(c1)}   e   C2 = {formatar_vetor(c2)}")

    print("Passo 2: Verificar se as colunas são linearmente independentes (LI):")
    if c1 == [0, 0] and c2 == [0, 0]:
        print("  Ambas as colunas são nulas (Linearmente Dependentes).")
        print("Passo 3 e 4: Base e conjunto Imagem:")
        print("  Base de Im(T) = ∅")
        print("  Im(T) = {(0, 0)}  (Dimensão = 0)")
        return 0

    if det != 0:
        print(
            f"  det(A) = {formatar_num(det)} ≠ 0 -> As colunas C1 e C2 são "
            "Linearmente Independentes (LI)."
        )
        print("Passo 3: Identificar as colunas independentes:")
        print(f"  Base da imagem = {{{formatar_vetor(c1)}, {formatar_vetor(c2)}}}")
        print("Passo 4: Resultado da imagem:")
        print("  Im(T) = R²  (Dimensão = 2)")
        return 2

    if c1 != [0, 0]:
        k = c2[0] / c1[0] if c1[0] != 0 else c2[1] / c1[1]
        print(
            f"  Dependência linear encontrada: C2 = {formatar_num(k)} × C1 "
            f"({formatar_vetor(c2)} = {formatar_num(k)} × {formatar_vetor(c1)})."
        )
        base_col = c1
    else:
        print(f"  Dependência linear encontrada: C1 = 0 × C2 ({formatar_vetor(c1)} = 0 × {formatar_vetor(c2)}).")
        base_col = c2

    print("Passo 3: Identificar a coluna independente:")
    print(f"  Base da imagem = {{{formatar_vetor(base_col)}}}")
    print("Passo 4: Resultado da imagem:")
    print(
        f"  Im(T) = {{({formatar_termo_param(base_col[0], 't')}, "
        f"{formatar_termo_param(base_col[1], 't')}) | t ∈ R}}  (Dimensão = 1)"
    )
    return 1


# 5. DEMONSTRAÇÃO DOS EXEMPLOS DOS SLIDES E TRANSFORMAÇÕES GEOMÉTRICAS ----------------------------------------------------------------------------------------


def demonstrar_exemplos_slides() -> None:
    print("=" * 66)
    print("DEMONSTRAÇÃO PRÁTICA — EXEMPLOS DOS SLIDES (UDESC)")
    print("=" * 66)

    print("\n[EXEMPLO 1] Multiplicação de Matriz por Vetor (Slides 16 e 18)")
    A1 = [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(3)]]
    v1 = [Fraction(2), Fraction(1)]
    aplicar_transformacao(A1, v1)
    verificar_linearidade(
        A1,
        u=[Fraction(2), Fraction(1)],
        v=[Fraction(1), Fraction(4)],
        alpha=Fraction(3),
        beta=Fraction(-2),
    )

    print("\n" + "-" * 66)
    print("[EXEMPLO 2] Cálculo de Núcleo e Imagem (Slides 20 e 22)")
    A2 = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
    dim_ker = calcular_nucleo(A2)
    dim_im = calcular_imagem(A2)
    print(
        f"\nTeorema do Núcleo e da Imagem: dim(Ker(T)) + dim(Im(T)) = "
        f"{dim_ker} + {dim_im} = {dim_ker + dim_im} = dim(R²)"
    )


def testar_transformacoes_geometricas(v: list[Fraction]) -> None:
    """Aplica transformações geométricas clássicas ao vetor v informado pelo usuário."""
    print("\n--- Transformações Geométricas no Plano (Slides 23 e 24) ---")
    print(f"Vetor informado: v = {formatar_vetor(v)}\n")

    transformacoes = {
        "Ampliação (escala 2x)": [[Fraction(2), Fraction(0)], [Fraction(0), Fraction(2)]],
        "Redução (escala 1/2)": [[Fraction(1, 2), Fraction(0)], [Fraction(0), Fraction(1, 2)]],
        "Reflexão em relação ao eixo X": [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(-1)]],
        "Reflexão em relação ao eixo Y": [[Fraction(-1), Fraction(0)], [Fraction(0), Fraction(1)]],
        "Rotação de 90° (anti-horário)": [[Fraction(0), Fraction(-1)], [Fraction(1), Fraction(0)]],
        "Rotação de 180°": [[Fraction(-1), Fraction(0)], [Fraction(0), Fraction(-1)]],
        "Cisalhamento horizontal (k = 2)": [[Fraction(1), Fraction(2)], [Fraction(0), Fraction(1)]],
    }

    for nome, matriz in transformacoes.items():
        res = aplicar_transformacao(matriz, v, mostrar_passos=False)
        print(f"• {nome:<32}: {formatar_vetor(v)} -> {formatar_vetor(res)}")


# 6. MENU PRINCIPAL INTERATIVO --------------------------------------------------------------------------------------------------------------------------------


def menu_interativo() -> None:
    while True:
        
        print("Transformações Lineares: Escolha as seguintes opções: ")
        print(" " * 66)
        print("1. Calcular T(v), Núcleo Ker(T) e Imagem Im(T) com meus valores")
        print("2. Verificar condições de linearidade com meus vetores e escalares")
        print("3. Aplicar transformações geométricas a um vetor meu")
        print("4. Executar exemplos prontos dos slides (Slides 16, 20 e 22)")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            A = ler_matriz_2x2()
            v = ler_vetor_2d("v")
            aplicar_transformacao(A, v)
            dim_ker = calcular_nucleo(A)
            dim_im = calcular_imagem(A)
            print(
                f"\nConferência (Teorema do Núcleo e da Imagem): "
                f"{dim_ker} + {dim_im} = {dim_ker + dim_im} = dim(R²)"
            )

        elif opcao == "2":
            A = ler_matriz_2x2()
            u = ler_vetor_2d("u")
            v = ler_vetor_2d("v")
            print("\nDigite os escalares α e β:")
            alpha = ler_fracao("  Escalar α (alpha): ")
            beta = ler_fracao("  Escalar β (beta): ")
            verificar_linearidade(A, u, v, alpha, beta)

        elif opcao == "3":
            v = ler_vetor_2d("v")
            testar_transformacoes_geometricas(v)

        elif opcao == "4":
            demonstrar_exemplos_slides()

        elif opcao == "0":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida. Escolha 1, 2, 3, 4 ou 0.")


if __name__ == "__main__":
    menu_interativo()