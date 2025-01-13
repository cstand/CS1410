# # python -m unittest discover -vbs tests

import unittest

from ListMultiples import *


class TestListMultiples(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(listMultiples(7, 5), [7, 14, 21, 28, 35])
        self.assertEqual(
            listMultiples(12, 10), [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
        )
        self.assertEqual(listMultiples(17, 6), [17, 34, 51, 68, 85, 102])

    def test_length_one(self):
        self.assertEqual(listMultiples(5, 1), [5])

    def test_zero_cases(self):
        self.assertEqual(listMultiples(0, 5), [0, 0, 0, 0, 0])

    def test_negative_numbers(self):
        self.assertEqual(listMultiples(-3, 4), [-3, -6, -9, -12])
        self.assertEqual(listMultiples(-10, 3), [-10, -20, -30])

    def test_large_numbers(self):
        self.assertEqual(listMultiples(1000, 3), [1000, 2000, 3000])


if __name__ == "__main__":
    unittest.main()
