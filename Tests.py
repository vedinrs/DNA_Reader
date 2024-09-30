import unittest
import main
import DNAReader

# TODO: tests not working with graphical implementation
class DNAtoAAReaderTest(unittest.TestCase):

    def test_empty(self):
        result = DNAReader.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\empty.txt", "")
        self.assertEqual(result, [])

    def test_lysine(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\Lysine.txt", "K")
        self.assertEqual(result, [1])

    def test_lysine_variant(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\AAG.txt", "K")
        self.assertEqual(result, [1])

    def test_no_match(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\basic.txt", "K")
        self.assertEqual(result, [])

    def test_two_aa(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\two_aa.txt", "KG")
        self.assertEqual(result, [1])

    def test_overlap(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\overlap.txt", "K")
        self.assertEqual(result, [1, 2])

    def test_kkkrk_fail(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\KKKRK_fail.txt", "KKKRK")
        self.assertEqual(result, [])

    def test_kkkrk_simple(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\KKKRK_simple.txt", "KKKRK")
        self.assertEqual(result, [4])

    def test_kkkrk(self):
        result = main.dna_to_aa_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\KKKRK.txt", "KKKRK")
        self.assertEqual(result, [47, 122])


class DNAReaderTest(unittest.TestCase):

    def test_empty(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\empty.txt", "")
        self.assertEqual(result, [])

    def test_empty_file(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\empty.txt", "A")
        self.assertEqual(result, [])

    def test_empty_to_find(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\basic.txt", "")
        self.assertEqual(result, [])

    def test_basic_match(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\basic.txt", "ACTG")
        self.assertEqual(result, [1])

    def test_basic_no_match(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\basic.txt", "AACTG")
        self.assertEqual(result, [])

    def test_two_matches(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\double.txt", "ACTG")
        self.assertEqual(result, [1, 5])

    def test_two_matches_filler(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\double.txt", "CT")
        self.assertEqual(result, [2, 6])

    def test_no_overflow(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\double.txt", "GA")
        self.assertEqual(result, [4])

    def test_complex(self):
        result = main.dna_reader("C:\\Users\\vedin\\Downloads\\DNAReader\\complex.txt", "GATACA")
        self.assertEqual(result, [108, 199, 380])


if __name__ == '__main__':
    unittest.main()
