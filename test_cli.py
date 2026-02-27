import unittest
from main import parse_args

class TestCLI(unittest.TestCase):
    def test_default_args(self):
        args = parse_args(["--seq1", "file1.fasta", "--seq2", "file2.fasta"])
        self.assertEqual(args.seq1, "file1.fasta")
        self.assertEqual(args.seq2, "file2.fasta")
        self.assertEqual(args.match, 1)
        self.assertEqual(args.mismatch, -1)
        self.assertEqual(args.gap, -1)
        self.assertFalse(args.quiet)

    def test_custom_scores(self):
        args = parse_args([
            "--seq1", "f1.fasta", 
            "--seq2", "f2.fasta", 
            "--match", "2", 
            "--mismatch", "-2", 
            "--gap", "-3",
            "--quiet"
        ])
        self.assertEqual(args.match, 2)
        self.assertEqual(args.mismatch, -2)
        self.assertEqual(args.gap, -3)
        self.assertTrue(args.quiet)

    def test_missing_required(self):
        # argparse usually exits on missing required args, 
        # but we can test if it raises a SystemExit
        with self.assertRaises(SystemExit):
            parse_args(["--seq1", "file1.fasta"])

if __name__ == "__main__":
    unittest.main()
