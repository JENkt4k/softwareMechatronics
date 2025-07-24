# test_kmp.py
import unittest
from algorithms.string.kmp import kmp_search

class TestKMP(unittest.TestCase):
    def test_basic_match(self):
        text = "ABABDABACDABABCABAB"
        pattern = "ABABCABAB"
        matches = kmp_search(text, pattern)
        self.assertEqual(matches, [10])

    def test_no_match(self):
        text = "ABCDEFG"
        pattern = "HIJ"
        matches = kmp_search(text, pattern)
        self.assertEqual(matches, [])

    def test_multiple_matches(self):
        text = "AAAAABAAABA"
        pattern = "AAAA"
        matches = kmp_search(text, pattern)
        self.assertEqual(matches, [0, 1])

    def test_empty_pattern(self):
        text = "ABC"
        pattern = ""
        matches = kmp_search(text, pattern)
        self.assertEqual(matches, [])

if __name__ == "__main__":
    unittest.main()
