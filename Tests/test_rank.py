"""Module for testing Rank class"""

import unittest
from ProductionCode.rank import Rank


class RankTest(unittest.TestCase):
    """This class is for testing the Rank Class."""

    def test__str__(self):
        """Test for string method"""
        # Test the rank function
        ranked_data = Rank("Ace of Spades", 2)

        self.assertEqual("Ace of Spades: 2", str(ranked_data))
