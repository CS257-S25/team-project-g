"""Module for testing SearchSection class"""

import unittest
from Tests.mock_data import mock_search_section, mock_book


class SearchSectionTest(unittest.TestCase):
    """This class is for testing the SearchSection class."""

    def test_get_heading(self):
        """Test for get_heading method"""

        self.assertEqual(mock_search_section.get_heading(), "Title")

    def test_get_search_type(self):
        """Test for get_search_type method"""

        self.assertEqual(mock_search_section.get_search_type(), "title")

    def test_get_results(self):
        """Test for get_results method"""

        self.assertEqual(mock_search_section.get_results(), [mock_book, mock_book])
