from ProductionCode.rank import Rank
import unittest

class RankTest:
    """
    Arguments: None
    Return value: None
    This class is for testing the rank function.
    """
    def test__str__(self):

        # Test the rank function
        ranked_data = Rank("Ace of Spades", 2)

        self.assertEqual("Ace of Spades: 2", ranked_data.__str__())
