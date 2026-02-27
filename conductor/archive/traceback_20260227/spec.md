# Specification - Implement Traceback and Alignment Reconstruction

## Context
The current implementation of SeqAlignX calculates the optimal alignment score and displays the scoring matrix but does not yet reconstruct the actual sequence alignment (the "traceback" step). This track aims to complete the Needleman-Wunsch implementation.

## Goal
Implement the traceback algorithm to reconstruct the optimal alignment between two sequences, including gaps, and display the result to the user.

## Requirements
- **Traceback Logic:** Correctly navigate from the bottom-right of the scoring matrix back to the top-left (0,0).
- **Alignment Strings:** Generate two strings representing the aligned sequences, with '-' representing gaps.
- **CLI Display:** Output the reconstructed alignment in a clear, readable format.
- **Verification:** Ensure the reconstructed alignment matches the calculated score.

## Technical Constraints
- Use only Python Standard Library.
- Maintain existing scoring system (+1 match, -1 mismatch, -1 gap).
