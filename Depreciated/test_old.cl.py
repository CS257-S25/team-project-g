"""
This file contains the unit tests for the CLI.
"""

import unittest
import sys
from io import StringIO

import cl

from Depreciated.search import search_title, search_author, search_genre
from Depreciated.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles,
)


class TestCL(unittest.TestCase):
    """Tests for command line functionality"""

    def setUp(self):
        """redirect stdout and stderr to a buffer"""
        self._orig_stdout = sys.stdout
        self._orig_stderr = sys.stderr
        self._buffer = StringIO()
        sys.stdout = self._buffer
        sys.stderr = self._buffer

    def tearDown(self):
        """restore stdout and stderr to their original state"""
        sys.stdout = self._orig_stdout
        sys.stderr = self._orig_stderr

    # def test_no_arguments(self):
    #     """No args: prints usage and exits(1)."""
    #     sys.argv = ["cl.py"]
    #     with self.assertRaises(SystemExit) as cm:
    #         cl.main()
    #     self.assertEqual(cm.exception.code, 1)
    #     output = self._buffer.getvalue().lower()
    #     self.assertIn("usage:", output)

    def test_invalid_argument(self):
        """Unknown flag: prints usage and exits with error code."""
        sys.argv = ["cl.py", "--not-a-flag"]
        with self.assertRaises(SystemExit) as cm:
            cl.main()
        self.assertIn(cm.exception.code, (1, 2))
        output = self._buffer.getvalue().lower()
        self.assertIn("usage:", output)

    def test_help_flag(self):
        """-h/--help prints the help message and exits(0)."""
        for flag in ("-h", "--help"):
            with self.subTest(flag=flag):
                sys.argv = ["cl.py", flag]
                with self.assertRaises(SystemExit) as cm:
                    cl.main()
                self.assertEqual(cm.exception.code, 0)
                output = self._buffer.getvalue().lower()
                self.assertIn("command line interface for the project", output)
                self._buffer.truncate(0)
                self._buffer.seek(0)


class TestSearchFunctions(unittest.TestCase):
    """Tests for search functions"""

    def test_search_genre_horror(self):
        """Searching genre 'horror' returns exactly the expected five titles."""
        expected = [
            "Killing Mr. Griffin by Lois Duncan (ISBN not found)",
            "Kill or be Killed, Vol. 1 by Elizabeth Breitweiser, Sean Phillips, Ed Brubaker"
            " (ISBN: 1534300287)",
            "Kill or be Killed, Vol. 2 by Elizabeth Breitweiser, Sean Phillips, Ed Brubaker"
            " (ISBN: 153430228X)",
            "Kingdom Of The Wicked by Ian Edginton, D'Israeli (ISBN: 1782760563)",
            "King Kong by Ian Thorne (ISBN: 0913940690)",
        ]
        results = list(search_genre("horror"))
        self.assertEqual(results, expected)

    def test_search_author_stan(self):
        """Searching author 'Stan' returns the single expected title."""
        expected = [
            "Karakuridôji Ultimo, #1 by Hiroyuki Takei, Stan Lee (ISBN: 1421531321)"
        ]
        results = list(search_author("Stan"))
        self.assertEqual(results, expected)

    def test_search_title_killing_jesus(self):
        """Searching title 'killing jesus' returns the single expected title."""
        expected = [
            "Killing Jesus: A History by Martin Dugard, Bill O'Reilly (ISBN: 1250142202)"
        ]
        results = list(search_title("killing jesus"))
        self.assertEqual(results, expected)

    def test_search_title_no_match(self):
        """search_title on gibberish yields empty list."""
        results = list(search_title("***no_such_title***"))
        self.assertEqual(results, [])

    def test_search_author_no_match(self):
        """search_author on gibberish yields empty list."""
        results = list(search_author("***no_such_author***"))
        self.assertEqual(results, [])

    def test_search_genre_no_match(self):
        """search_genre on gibberish yields empty list."""
        results = list(search_genre("***no_such_genre***"))
        self.assertEqual(results, [])


class TestMostBannedFunctions(unittest.TestCase):
    """Tests for most banned functions"""

    def test_most_banned_districts_top3(self):
        """Top 3 most banned districts."""
        expected = [
            "Escambia County Public Schools: 1787",
            "Clay County School District: 864",
            "Orange County Public Schools: 734",
        ]
        results = list(most_banned_districts(3))
        self.assertEqual(results, expected)

    def test_most_banned_authors_top3(self):
        """Top 3 most banned authors."""
        expected = [
            "Ellen Hopkins: 791",
            "Sarah J. Maas: 657",
            "Jodi Picoult: 213",
        ]
        results = list(most_banned_authors(3))
        self.assertEqual(results, expected)

    def test_most_banned_states_top3(self):
        """Top 3 most banned states."""
        expected = [
            "Florida: 6533",
            "Iowa: 3685",
            "Texas: 1964",
        ]
        results = list(most_banned_states(3))
        self.assertEqual(results, expected)

    def test_most_banned_titles_top3(self):
        """Top 3 most banned titles."""
        expected = [
            "Looking for Alaska: 135",
            "Nineteen Minutes: 126",
            "The Perks of Being a Wallflower: 118",
        ]
        results = list(most_banned_titles(3))
        self.assertEqual(results, expected)
