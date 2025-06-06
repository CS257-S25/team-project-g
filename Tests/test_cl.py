"""
This file contains the unit tests for the CLI.
"""

import unittest
import sys
from io import StringIO
from unittest.mock import MagicMock, patch

from ProductionCode.rank import Rank
import cl

from Tests.mock_data import mock_book


class TestCommandLine(unittest.TestCase):
    """Tests for Command Line Functionality"""

    def setUp(self):
        """Create a mock postgress connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.DataSource.books_search_title")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search_title(self, mock_connect, mock_books_search_title):
        """
        Tests for title search
        Acceptance test for search by title User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_books_search_title.return_value = [mock_book]
        sys.argv = ["cl.py", "--st", "Kaleidoscope"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Kaleidoscope by Danielle Steel (ISBN: 440236924)\n")

    @patch("ProductionCode.datasource.DataSource.books_search_author")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search_author(self, mock_connect, mock_books_search_author):
        """
        Tests for author search
        Acceptance test for search by author User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_books_search_author.return_value = [mock_book]
        sys.argv = ["cl.py", "--sa", "Danielle Steel"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Kaleidoscope by Danielle Steel (ISBN: 440236924)\n")

    @patch("ProductionCode.datasource.DataSource.books_search_genre")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search_genre(self, mock_connect, mock_books_search_genre):
        """
        Tests for genre search
        Acceptance test for search by genre User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_books_search_genre.return_value = [mock_book]
        sys.argv = ["cl.py", "--sg", "Mystery"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Kaleidoscope by Danielle Steel (ISBN: 440236924)\n")

    @patch("ProductionCode.datasource.DataSource.books_search_title")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search_title_no_results(self, mock_connect, mock_books_search_title):
        """
        Tests for title search no results
        Acceptance test for results not found for search User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_books_search_title.return_value = []
        sys.argv = ["cl.py", "--st", "Kaleidoscope"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "No results found\n")

    @patch("ProductionCode.datasource.DataSource.get_most_banned_titles")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_titles(self, mock_connect, mock_get_most_banned_titles):
        """
        Tests for most_banned_titles
        Acceptance test for most banned books User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_titles.return_value = [Rank("Kaleidoscope", 4)]
        sys.argv = ["cl.py", "--mbt", "1"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Kaleidoscope: 4\n")

    @patch("ProductionCode.datasource.DataSource.get_most_banned_authors")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_authors(self, mock_connect, mock_get_most_banned_authors):
        """
        Tests for most_banned_authors
        Acceptance test for most banned authors User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_authors.return_value = [Rank("Sarah J. Maas", 52)]
        sys.argv = ["cl.py", "--mba", "1"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Sarah J. Maas: 52\n")

    @patch("ProductionCode.datasource.DataSource.get_most_banned_states")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_states(self, mock_connect, mock_get_most_banned_states):
        """
        Tests for most_banned_states
        Acceptance test for most banned states User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_states.return_value = [Rank("Florida", 80)]
        sys.argv = ["cl.py", "--mbs", "1"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Florida: 80\n")

    @patch("ProductionCode.datasource.DataSource.get_most_banned_states")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_states_multiple(
        self, mock_connect, mock_get_most_banned_states
    ):
        """
        Tests for most_banned_states for multiple states
        Acceptance test for displays subcategory in a
        sorted list by number of bans User Story
        """
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_states.return_value = [
            Rank("Florida", 80),
            Rank("Texas", 50),
        ]
        sys.argv = ["cl.py", "--mbs", "2"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertEqual(printed, "Florida: 80\nTexas: 50\n")

    @patch("ProductionCode.datasource.DataSource.get_most_banned_states")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_states_with_number_of_bans(
        self, mock_connect, mock_get_most_banned_states
    ):
        """
        Tests for most_banned_states for displaying number of bans
        Acceptance test for displays number of bans for each subcategory
        """
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_states.return_value = [
            Rank("Florida", 80),
        ]
        sys.argv = ["cl.py", "--mbs", "1"]
        sys.stdout = StringIO()
        cl.main()
        printed = sys.stdout.getvalue()
        self.assertIn("80", printed)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_help(self, mock_connect):
        """Test for help message"""
        mock_connect.return_value = self.mock_conn

        sys.argv = ["cl.py"]
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as cm:
            cl.main()
        self.assertEqual(cm.exception.code, 1)


if __name__ == "__main__":
    unittest.main()
