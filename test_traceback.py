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

    def test_alignment_formatting(self):
        from main import format_alignment
        align1 = "G-ATTACA"
        align2 = "GCA-TGCU"
        # G vs G: |
        # - vs C:  
        # A vs A: |
        # T vs -:  
        # T vs T: |
        # A vs G:  
        # C vs C: |
        # A vs U:  
        expected_middle = "| | | | "
        output = format_alignment(align1, align2)
        lines = output.split('\n')
        self.assertEqual(lines[0].strip(), "G - A T T A C A")
        self.assertEqual(lines[1].strip(), "|   |   |   |")
        self.assertEqual(lines[2].strip(), "G C A - T G C U")

    def test_needleman_wunsch(self):
        from main import needleman_wunsch
        seq1 = "GATTACA"
        seq2 = "GCATGCU"
        score = needleman_wunsch(seq1, seq2)
        self.assertEqual(score, 0)

    def test_print_matrix(self):
        from main import print_matrix, create_score_matrix
        import io
        from contextlib import redirect_stdout
        seq1 = "A"
        seq2 = "G"
        matrix = [[0, -1], [-1, -1]]
        f = io.StringIO()
        with redirect_stdout(f):
            print_matrix(matrix, seq1, seq2)
        output = f.getvalue()
        self.assertIn("Matriz de Pontuação:", output)
        self.assertIn("G", output)
        self.assertIn("A", output)

if __name__ == "__main__":
    unittest.main()
