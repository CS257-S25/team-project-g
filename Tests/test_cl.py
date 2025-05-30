"""
This file contains the unit tests for the CLI.
"""

import unittest
import sys
from io import StringIO
from unittest.mock import MagicMock, patch

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
