from .. import cl
from ProductionCode import search
from ProductionCode import most_banned
import unittest
import sys

if __name__ == "__main__":
    unittest.main()


class Test_command_line(unittest.TestCase):
    """
    This class tests the command line interface of the cl.py.
    """

    def test_cl_app(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the title of a book.
        """

        sys.argv = ["cl.py", "--search-title", "Cool for the Summer"]
        cl.main()
        self.assertEqual(cl.get_title(), "Cool for the Summer")

        sys.argv = ["cl.py", "--help"]
        cl.main()
        self.assertIn(cl.get_help(), sys.stdout.get_help())

    def test_get_author(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the author of a book.
        """

    def test_get_genre(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the genre of a book.
        """

    def test_get_most_banned_districts(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned districts.
        """

        # Simulate normal test.
        self.assertEqual(most_banned.most_banned_districts(5), "Fake District: 5")

        # Simulate edge case test.
        self.assertEqual(most_banned.most_banned_districts(-5), "Fake District: 0")

    def test_get_most_banned_authors(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned authors.
        """

        # Simulate normal test.
        self.assertEqual(most_banned.most_banned_authors(3), "George Orwell: 1")

        # Simulate edge case test.
        self.assertEqual(most_banned.most_banned_authors(-3), "Fake Author: 0")

    def test_get_most_banned_states(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned states.
        """

        # Simulate normal test.
        self.assertEqual(most_banned.most_banned_states(1), "Texas: 1")

        # Simulate edge case test.
        self.assertEqual(most_banned.most_banned_states(-1), "Fake State: 0")

    def test_get_most_banned_titles(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned titles.
        """

        # Simulate normal test.
        self.assertEqual(most_banned.most_banned_titles(1), "The Hate U Give: 1")

        # Simulate edge case test.
        self.assertEqual(most_banned.most_banned_titles(0), "Fake Title: 0")

    def test_get_help(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the help message.
        """


# These are blueprints for tests.
