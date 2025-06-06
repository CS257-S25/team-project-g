"""Module for testing Rank class"""

import unittest
from ProductionCode.rank import Rank


class RankTest(unittest.TestCase):
    """This class is for testing the Rank Class."""

    def setUp(self) -> None:
        self.mock_rank = Rank("Ace of Spades", 2)

    def test__str__(self):
        """Test for string method"""

        self.assertEqual("Ace of Spades: 2", str(self.mock_rank))

    def test_get_name(self):
        """Test for get_name method"""

        self.assertEqual("Ace of Spades", self.mock_rank.get_name())

    def test_get_bans(self):
        """Test for get_name method"""

        self.assertEqual(2, self.mock_rank.get_bans())
