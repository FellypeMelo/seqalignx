# Product Guidelines - SeqAlignX

## Language & Prose
- **Primary Language:** Portuguese. All documentation, comments (where appropriate for education), and CLI outputs should be in Portuguese to maintain consistency with the existing README.
- **Tone:** Academic/Technical. Use precise biological and algorithmic terminology. The prose should be structured, formal, and authoritative, suitable for a scientific or educational context.

## UX & CLI Principles
- **Informative CLI:** The tool should provide clear feedback about the alignment process, explaining steps like matrix initialization and the scoring logic.
- **Quiet by Default:** While informative, the CLI should also support a "quiet" mode (e.g., via a flag) to be easily integrated into automated bioinformatics pipelines without unnecessary output.
- **Visual-First:** Prioritize visual representations of data. The scoring matrix and the final alignment should be displayed using ASCII or other text-based formatting to help users visualize the algorithm's results.

## Documentation Standards
- **Exhaustive Docstrings:** Every function, class, and major logic block must include detailed docstrings. These should explain not just *what* the code does, but *why* it does it, referencing biological or algorithmic principles where relevant.
- **Algorithmic Transparency:** Comments should be used within the code to step through the Needleman-Wunsch logic, making it easy for students to follow the implementation.
