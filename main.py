"""
SeqAlignX - Alinhamento Global

Propósito: Implementação do algoritmo Needleman-Wunsch para alinhamento
global de duas sequências biológicas.

O algoritmo utiliza programação dinâmica para encontrar o melhor
alinhamento possível entre duas sequências.
"""

# Constantes de pontuação
MATCH_SCORE = 1
MISMATCH_SCORE = -1
GAP_SCORE = -1


def create_score_matrix(seq1, seq2):
    """
    Cria e inicializa a matriz de pontuação.

    Args:
        seq1: Primeira sequência
        seq2: Segunda sequência

    Returns:
        list: Matriz de pontuação inicializada
    """
    m, n = len(seq1), len(seq2)

    # Inicializa matriz com zeros
    score_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Preenche primeira coluna (gaps na sequência 2)
    for i in range(1, m + 1):
        score_matrix[i][0] = score_matrix[i - 1][0] + GAP_SCORE

    # Preenche primeira linha (gaps na sequência 1)
    for j in range(1, n + 1):
        score_matrix[0][j] = score_matrix[0][j - 1] + GAP_SCORE

    return score_matrix


def fill_score_matrix(score_matrix, seq1, seq2):
    """
    Preenche a matriz de pontuação usando o algoritmo Needleman-Wunsch.

    Args:
        score_matrix: Matriz inicializada
        seq1: Primeira sequência
        seq2: Segunda sequência

    Returns:
        list: Matriz completamente preenchida
    """
    m, n = len(seq1), len(seq2)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calcula pontuação do match/mismatch
            match = MATCH_SCORE if seq1[i - 1] == seq2[j - 1] else MISMATCH_SCORE

            # Calcula três possibilidades
            diagonal = score_matrix[i - 1][j - 1] + match  # Match/Mismatch
            up = score_matrix[i - 1][j] + GAP_SCORE  # Gap em seq2
            left = score_matrix[i][j - 1] + GAP_SCORE  # Gap em seq1

            # Escolhe o máximo
            score_matrix[i][j] = max(diagonal, up, left)

    return score_matrix


def get_alignment_score(score_matrix):
    """
    Retorna o score final do alinhamento.

    Args:
        score_matrix: Matriz de pontuação preenchida

    Returns:
        int: Score do alinhamento ótimo
    """
    return score_matrix[-1][-1]


def needleman_wunsch(seq1, seq2):
    """
    Executa o algoritmo completo de Needleman-Wunsch.

    Args:
        seq1: Primeira sequência
        seq2: Segunda sequência

    Returns:
        int: Score do melhor alinhamento global
    """
    # Cria e preenche matriz
    score_matrix = create_score_matrix(seq1, seq2)
    score_matrix = fill_score_matrix(score_matrix, seq1, seq2)

    return get_alignment_score(score_matrix)


def traceback(score_matrix, seq1, seq2):
    """
    Reconstrói o alinhamento ótimo a partir da matriz de pontuação.

    Args:
        score_matrix: Matriz de pontuação preenchida
        seq1: Primeira sequência original
        seq2: Segunda sequência original

    Returns:
        tuple: (aligned_seq1, aligned_seq2)
    """
    aligned_seq1 = []
    aligned_seq2 = []

    i, j = len(seq1), len(seq2)

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            # Verifica se veio da diagonal (match ou mismatch)
            match = MATCH_SCORE if seq1[i - 1] == seq2[j - 1] else MISMATCH_SCORE
            if score_matrix[i][j] == score_matrix[i - 1][j - 1] + match:
                aligned_seq1.append(seq1[i - 1])
                aligned_seq2.append(seq2[j - 1])
                i -= 1
                j -= 1
                continue

        if i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + GAP_SCORE:
            # Veio de cima (gap na seq2)
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append("-")
            i -= 1
        else:
            # Veio da esquerda (gap na seq1)
            aligned_seq1.append("-")
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    return "".join(reversed(aligned_seq1)), "".join(reversed(aligned_seq2))


def format_alignment(align1, align2):
    """
    Formata o alinhamento para exibição visual.

    Args:
        align1: Primeira sequência alinhada (com gaps)
        align2: Segunda sequência alinhada (com gaps)

    Returns:
        str: String formatada com barras verticais para matches
    """
    matches = []
    for c1, c2 in zip(align1, align2):
        if c1 == c2 and c1 != "-":
            matches.append("|")
        else:
            matches.append(" ")

    line1 = " ".join(align1)
    line2 = " ".join(matches)
    line3 = " ".join(align2)

    return f"{line1}\n{line2}\n{line3}"


def print_matrix(score_matrix, seq1, seq2):
    """
    Imprime a matriz de pontuação formatada (para debug).
    """
    print("\nMatriz de Pontuação:")
    print("     " + "  ".join(f" {c} " for c in " " + seq2))

    for i, row in enumerate(score_matrix):
        prefix = " " if i == 0 else seq1[i - 1]
        print(f"{prefix} " + " ".join(f"{val:3d}" for val in row))


def main():
    """Função principal do programa."""
    # Sequências de exemplo
    seq1 = "GATTACA"
    seq2 = "GCATGCU"

    print("=" * 60)
    print("SeqAlignX - Alinhamento Global (Needleman-Wunsch)")
    print("=" * 60)
    print(f"\nSequência 1: {seq1}")
    print(f"Sequência 2: {seq2}")

    # Cria e preenche matriz
    score_matrix = create_score_matrix(seq1, seq2)
    score_matrix = fill_score_matrix(score_matrix, seq1, seq2)

    # Calcula score
    score = get_alignment_score(score_matrix)
    print(f"\nScore de Alinhamento: {score}")

    # Reconstrói alinhamento
    align1, align2 = traceback(score_matrix, seq1, seq2)
    print("\nAlinhamento Reconstruído:")
    print(format_alignment(align1, align2))

    # Mostra matriz (opcional, para demonstração)
    print_matrix(score_matrix, seq1, seq2)

    print("\nAlinhamento concluído!")


if __name__ == "__main__":
    main()
