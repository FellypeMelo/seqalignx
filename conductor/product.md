# Initial Concept
SeqAlignX is an educational implementation of the Needleman-Wunsch algorithm for global alignment of biological sequences.

# Product Guide - SeqAlignX

## Vision
SeqAlignX aims to be the go-to educational and practical tool for understanding and performing global biological sequence alignment using the Needleman-Wunsch algorithm. It balances algorithmic transparency with enough functional power to be useful for real-world research tasks.

## Target Users
- **Students/Educators:** Those learning or teaching the fundamentals of bioinformatics algorithms.
- **Bioinformaticians:** Professionals looking for a lightweight, reliable tool for quick alignment tasks without heavy dependencies.
- **Researchers:** Scientists who need a customizable base for experimenting with sequence alignment variants.

## Core Goals
- **Educational Clarity:** Keep the code readable and well-documented to serve as a learning resource.
- **Algorithm Completion:** (Completed) Fully implement the Needleman-Wunsch algorithm, including the critical traceback step.
- **Practical Utility:** Move beyond simple hardcoded strings to supporting industry-standard file formats and scoring systems.

## Key Features
- **Traceback Implementation:** (Implemented) Reconstruct and visualize the optimal alignment between two sequences with professional biological formatting.
- **FASTA Support:** (Implemented) Directly read and process DNA/RNA/Protein sequence data from .fasta files, supporting multiline sequences.
- **CLI Interface:** (Implemented) Interactive command-line interface for specifying input files and custom scoring parameters.
- **Substitution Matrices:** Support for advanced scoring systems like BLOSUM and PAM for more accurate protein alignments.
- **Dynamic Programming Visualization:** (Existing) Clear display of the scoring matrix to demystify the algorithm's internal state.

## Usage Scenarios
- **Homology Detection:** Comparing genes or proteins across different species to find evolutionary relationships.
- **Mutation Analysis:** pinpointing specific insertions, deletions, or substitutions between a reference and a sample sequence.
- **Algorithmic Learning:** Stepping through the matrix fill and traceback process to master dynamic programming concepts.
