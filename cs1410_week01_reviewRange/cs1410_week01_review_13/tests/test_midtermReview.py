# # python -m unittest discover -vbs tests

import unittest

from Dice_game import *


class TestDiceGame(unittest.TestCase):

    def test_no_doubles(self):
        # Test cases where no doubles are rolled
        self.assertEqual(dice_game([(1, 2), (3, 4), (5, 6)]), 21)
        self.assertEqual(dice_game([(2, 3), (1, 4), (6, 5)]), 21)

    def test_doubles_in_first_round(self):
        # If doubles are rolled in the first round, score should be 0
        self.assertEqual(dice_game([(1, 1), (3, 4), (5, 6)]), 0)
        self.assertEqual(dice_game([(6, 6), (1, 2), (3, 4)]), 0)

    def test_doubles_in_second_round(self):
        # If doubles are rolled in the second round, score should be 0
        self.assertEqual(dice_game([(1, 2), (3, 3), (5, 6)]), 0)
        self.assertEqual(dice_game([(2, 4), (4, 4), (3, 5)]), 0)

    def test_doubles_in_third_round(self):
        # If doubles are rolled in the third round, score should be 0
        self.assertEqual(dice_game([(1, 2), (3, 4), (5, 5)]), 0)
        self.assertEqual(dice_game([(6, 3), (2, 1), (4, 4)]), 0)

    def test_all_doubles(self):
        # If doubles are rolled in all rounds, score should be 0
        self.assertEqual(dice_game([(1, 1), (2, 2), (3, 3)]), 0)


if __name__ == "__main__":
    unittest.main()
