# Specification - Implement FASTA Support and CLI Interface

## Context
SeqAlignX currently requires manual editing of the main.py file to change sequences. To be practically useful, it needs to support standard biological file formats (FASTA) and command-line interaction.

## Goal
Implement a FASTA file parser and a command-line interface using rgparse to allow users to specify input files and scoring parameters via the terminal.

## Requirements
- **FASTA Parser:** A robust function to read DNA/RNA/Protein sequences from .fasta files, handling multiline sequences and header lines.
- **CLI Interface:** Use rgparse to support:
    - --seq1 and --seq2: Paths to FASTA files (mandatory).
    - --match, --mismatch, --gap: Custom scoring parameters (optional, with defaults).
    - --quiet: Boolean flag to suppress the scoring matrix visualization.
- **Error Handling:** Graceful handling of missing files or invalid FASTA formats.

## Technical Constraints
- Use only Python Standard Library (rgparse, os).
- Adhere to the XP + AI-Augmented workflow (TDD mandatory).
