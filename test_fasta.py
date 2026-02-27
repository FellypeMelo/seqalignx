import unittest
import os
from main import read_fasta

class TestFastaParsing(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_temp.fasta"
        
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_valid_fasta(self):
        content = ">seq1\nACGT\n>seq2\nTGCA\n"
        with open(self.test_file, "w") as f:
            f.write(content)
        
        sequences = read_fasta(self.test_file)
        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0], "ACGT")
        self.assertEqual(sequences[1], "TGCA")

    def test_read_multiline_fasta(self):
        content = ">seq1\nACGT\nACGT\n>seq2\nTGCA\nTGCA\n"
        with open(self.test_file, "w") as f:
            f.write(content)
        
        sequences = read_fasta(self.test_file)
        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0], "ACGTACGT")
        self.assertEqual(sequences[1], "TGCATGCA")

    def test_read_single_sequence(self):
        content = ">seq1\nACGT\n"
        with open(self.test_file, "w") as f:
            f.write(content)
        
        sequences = read_fasta(self.test_file)
        self.assertEqual(len(sequences), 1)
        self.assertEqual(sequences[0], "ACGT")

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_fasta("non_existent.fasta")

if __name__ == "__main__":
    unittest.main()
