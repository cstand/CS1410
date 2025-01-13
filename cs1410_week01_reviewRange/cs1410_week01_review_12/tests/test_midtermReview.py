# # python -m unittest discover -vbs tests

import unittest

from MissingLetters import *


class TestMissingLetters(unittest.TestCase):

    def test_all_present(self):
        # When all letters are present, the result should be an empty string
        self.assertEqual(missingLetters("abcdefghijklmnopqrstuvwxyz"), "")

    def test_none_present(self):
        # When no letters are present, the result should be the entire alphabet
        self.assertEqual(missingLetters(""), "abcdefghijklmnopqrstuvwxyz")

    def test_some_missing(self):
        # Test cases with specific missing letters
        self.assertEqual(missingLetters("abc"), "defghijklmnopqrstuvwxyz")
        self.assertEqual(missingLetters("mnop"), "abcdefghijklqrstuvwxyz")
        self.assertEqual(missingLetters("acegikmoqsuwy"), "bdfhjlnprtvxz")


if __name__ == "__main__":
    unittest.main()
