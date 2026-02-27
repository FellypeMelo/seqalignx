import unittest
import subprocess
import os

class TestIntegration(unittest.TestCase):
    def test_run_with_identical_fasta(self):
        cmd = [
            "python", "main.py",
            "--seq1", "test_data/seqalignx_test_01_identical.fasta",
            "--seq2", "test_data/seqalignx_test_01_identical.fasta",
            "--quiet"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Score de Alinhamento: 120", result.stdout)
        self.assertIn("Alinhamento concluído!", result.stdout)

    def test_run_with_different_fasta(self):
        cmd = [
            "python", "main.py",
            "--seq1", "test_data/seqalignx_test_01_identical.fasta",
            "--seq2", "test_data/seqalignx_test_11_high_similarity.fasta",
            "--quiet"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Score de Alinhamento:", result.stdout)
        self.assertIn("Alinhamento concluído!", result.stdout)

    def test_invalid_file(self):
        cmd = [
            "python", "main.py",
            "--seq1", "non_existent.fasta",
            "--seq2", "test_data/seqalignx_test_01_identical.fasta"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        # Should exit with non-zero code or print error
        self.assertIn("Erro", result.stdout + result.stderr)

if __name__ == "__main__":
    unittest.main()
