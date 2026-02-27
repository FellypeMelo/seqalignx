import unittest
from main import create_score_matrix, fill_score_matrix, traceback

class TestTraceback(unittest.TestCase):
    def test_identical_sequences(self):
        seq1 = "GATTACA"
        seq2 = "GATTACA"
        matrix = create_score_matrix(seq1, seq2)
        matrix = fill_score_matrix(matrix, seq1, seq2)
        align1, align2 = traceback(matrix, seq1, seq2)
        self.assertEqual(align1, "GATTACA")
        self.assertEqual(align2, "GATTACA")

    def test_sequences_with_gaps(self):
        seq1 = "GATTACA"
        seq2 = "GCATGCU"
        matrix = create_score_matrix(seq1, seq2)
        matrix = fill_score_matrix(matrix, seq1, seq2)
        align1, align2 = traceback(matrix, seq1, seq2)
        
        self.assertEqual(len(align1), len(align2))
        # Ensure characters match or are gaps
        for c1, c2 in zip(align1, align2):
            self.assertTrue(c1 in seq1 or c1 == '-')
            self.assertTrue(c2 in seq2 or c2 == '-')

if __name__ == "__main__":
    unittest.main()
