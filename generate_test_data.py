#!/usr/bin/env python3
"""
SeqAlignX - Gerador de Dados de Teste

Este script gera 50+ conjuntos de dados para testar alinhamento de sequências.
Inclui pares de sequências com diferentes níveis de similaridade.

Os dados de teste são COMMITADOS no GitHub.
Para dados reais, use a pasta data/ (gitignored)
"""

import random
import os
from datetime import datetime

TEST_DATA_DIR = "test_data"
NUM_DATASETS = 55


def generate_sequence(length, gc_content=0.5):
    """Gera uma sequência de DNA aleatória."""
    seq = []
    for _ in range(length):
        if random.random() < gc_content:
            seq.append(random.choice(["G", "C"]))
        else:
            seq.append(random.choice(["A", "T"]))
    return "".join(seq)


def generate_related_sequences(seq1, similarity=0.9):
    """
    Gera uma sequência relacionada a seq1 com certo nível de similaridade.

    Args:
        seq1: Sequência original
        similarity: Probabilidade de manter a base original (0.0 a 1.0)

    Returns:
        str: Sequência relacionada
    """
    seq2 = []
    bases = ["A", "T", "G", "C"]

    for base in seq1:
        if random.random() < similarity:
            seq2.append(base)
        else:
            # Substitui por uma base diferente
            new_base = random.choice([b for b in bases if b != base])
            seq2.append(new_base)

    return "".join(seq2)


def insert_gaps(sequence, gap_prob=0.1):
    """Simula deleções inserindo gaps na sequência."""
    result = []
    for base in sequence:
        if random.random() > gap_prob:
            result.append(base)
    return "".join(result)


def generate_test_datasets():
    """Gera todos os datasets de teste."""
    datasets = []

    # 1-10: Sequências idênticas (100% similaridade)
    for i in range(10):
        length = random.randint(50, 200)
        seq1 = generate_sequence(length)
        seq2 = seq1  # Idêntica
        datasets.append(
            (f"seqalignx_test_{i + 1:02d}_identical", seq1, seq2, "Identical sequences")
        )

    # 11-20: Alta similaridade (80-95%)
    for i in range(10, 20):
        length = random.randint(50, 200)
        seq1 = generate_sequence(length)
        similarity = random.uniform(0.80, 0.95)
        seq2 = generate_related_sequences(seq1, similarity)
        datasets.append(
            (
                f"seqalignx_test_{i + 1:02d}_high_similarity",
                seq1,
                seq2,
                f"High similarity ~{similarity:.0%}",
            )
        )

    # 21-30: Média similaridade (50-70%)
    for i in range(20, 30):
        length = random.randint(50, 200)
        seq1 = generate_sequence(length)
        similarity = random.uniform(0.50, 0.70)
        seq2 = generate_related_sequences(seq1, similarity)
        datasets.append(
            (
                f"seqalignx_test_{i + 1:02d}_medium_similarity",
                seq1,
                seq2,
                f"Medium similarity ~{similarity:.0%}",
            )
        )

    # 31-35: Baixa similaridade (20-40%)
    for i in range(30, 35):
        length = random.randint(50, 200)
        seq1 = generate_sequence(length)
        similarity = random.uniform(0.20, 0.40)
        seq2 = generate_related_sequences(seq1, similarity)
        datasets.append(
            (
                f"seqalignx_test_{i + 1:02d}_low_similarity",
                seq1,
                seq2,
                f"Low similarity ~{similarity:.0%}",
            )
        )

    # 36-40: Comprimentos diferentes (indels)
    for i in range(35, 40):
        length = random.randint(80, 150)
        seq1 = generate_sequence(length)
        seq2 = insert_gaps(seq1, gap_prob=0.1)
        datasets.append(
            (f"seqalignx_test_{i + 1:02d}_with_gaps", seq1, seq2, "With indels (gaps)")
        )

    # 41-45: Cenários biológicos
    # Simulando evolução conservada
    for i in range(40, 45):
        length = random.randint(100, 150)
        seq1 = generate_sequence(length, gc_content=0.5)
        # Alta conservação em regiões importantes
        seq2 = list(seq1)
        for j in range(len(seq2)):
            if j % 3 == 0:  # Menos mutações na primeira posição do códon
                if random.random() < 0.95:
                    continue
            if random.random() < 0.85:
                continue
            # Mutação
            bases = ["A", "T", "G", "C"]
            seq2[j] = random.choice([b for b in bases if b != seq2[j]])
        datasets.append(
            (
                f"seqalignx_test_{i + 1:02d}_conserved",
                seq1,
                "".join(seq2),
                "Conserved regions",
            )
        )

    # 46-50: Casos extremos
    # Sequências muito curtas
    seq1 = generate_sequence(10)
    seq2 = generate_related_sequences(seq1, 0.7)
    datasets.append(("seqalignx_test_46_very_short", seq1, seq2, "Very short (10bp)"))

    # Sequências muito longas
    seq1 = generate_sequence(500)
    seq2 = generate_related_sequences(seq1, 0.8)
    datasets.append(("seqalignx_test_47_very_long", seq1, seq2, "Very long (500bp)"))

    # Uma sequência é substring da outra
    seq1 = generate_sequence(100)
    seq2 = seq1[20:80]
    datasets.append(("seqalignx_test_48_substring", seq1, seq2, "One is substring"))

    # Complementar reversa
    seq1 = generate_sequence(50)
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    seq2 = "".join([complement[b] for b in reversed(seq1)])
    datasets.append(
        ("seqalignx_test_49_reverse_complement", seq1, seq2, "Reverse complement")
    )

    # Totalmente diferentes
    seq1 = generate_sequence(50)
    seq2 = generate_sequence(50)
    datasets.append(("seqalignx_test_50_unrelated", seq1, seq2, "Unrelated sequences"))

    # 51-55: Casos especiais
    # Sequências de aminoácidos (para testar se aceita)
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    seq1 = "".join(random.choice(amino_acids) for _ in range(30))
    seq2 = "".join(random.choice(amino_acids) for _ in range(30))
    datasets.append(
        ("seqalignx_test_51_protein", seq1, seq2, "Protein sequences (30aa)")
    )

    # Repetições
    seq1 = "ATGC" * 20
    seq2 = "ATGC" * 15 + "ATGG" * 5
    datasets.append(("seqalignx_test_52_repeats", seq1, seq2, "Tandem repeats"))

    # Homopolímeros
    seq1 = "A" * 50
    seq2 = "A" * 45 + "G" * 5
    datasets.append(
        ("seqalignx_test_53_homopolymer", seq1, seq2, "Homopolymer with variant")
    )

    # GC-rich vs AT-rich
    seq1 = generate_sequence(100, gc_content=0.8)
    seq2 = generate_sequence(100, gc_content=0.2)
    datasets.append(("seqalignx_test_54_gc_vs_at", seq1, seq2, "GC-rich vs AT-rich"))

    # Mesma sequência em fase diferente
    seq1 = generate_sequence(60)
    seq2 = seq1[1:] + seq1[0]
    datasets.append(("seqalignx_test_55_frameshift", seq1, seq2, "Frameshift by 1"))

    return datasets


def save_datasets(datasets):
    """Salva os datasets em arquivos FASTA."""
    os.makedirs(TEST_DATA_DIR, exist_ok=True)

    manifest_path = os.path.join(TEST_DATA_DIR, "MANIFEST.txt")
    with open(manifest_path, "w") as manifest:
        manifest.write("=" * 70 + "\n")
        manifest.write("SeqAlignX - Dados de Teste Sintéticos\n")
        manifest.write("=" * 70 + "\n\n")
        manifest.write(f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        manifest.write(f"Total de datasets: {len(datasets)}\n\n")
        manifest.write("ATENÇÃO: Estes são dados FABRICADOS para teste.\n")
        manifest.write("Útil para validar alinhamentos com similaridade conhecida.\n\n")
        manifest.write("Formato: Cada arquivo contém 2 sequências (seq1 e seq2)\n")
        manifest.write("Lista de arquivos:\n")
        manifest.write("-" * 70 + "\n")

        for filename, seq1, seq2, description in datasets:
            filepath = os.path.join(TEST_DATA_DIR, f"{filename}.fasta")

            with open(filepath, "w") as f:
                f.write(f">{filename}_seq1 {description}\n")
                f.write(seq1 + "\n")
                f.write(f">{filename}_seq2 {description}\n")
                f.write(seq2 + "\n")

            manifest.write(f"{filename}.fasta - {description}\n")
            manifest.write(f"  Seq1: {len(seq1)} bp, Seq2: {len(seq2)} bp\n")
            print(f"[OK] Gerado: {filename}.fasta ({len(seq1)}bp vs {len(seq2)}bp)")

    print(f"\n[OK] Manifesto salvo em: {manifest_path}")
    print(f"[OK] Total: {len(datasets)} arquivos FASTA gerados")


def main():
    print("=" * 70)
    print("SeqAlignX - Gerador de Dados de Teste")
    print("=" * 70)
    print()

    datasets = generate_test_datasets()
    save_datasets(datasets)

    print()
    print("=" * 70)
    print("Geração concluída!")
    print("=" * 70)
    print(f"\nDados em: {TEST_DATA_DIR}/")
    print("Execute: python main.py")


if __name__ == "__main__":
    main()
