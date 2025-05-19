"""Module for testing Book class"""

import unittest

from Tests.mock_data import mock_book


class TestBook(unittest.TestCase):
    """Tests for Book class"""

    def setUp(self):
        self.book = mock_book

    def test_string(self):
        """Tests __str__ method"""
        self.assertEqual(
            str(self.book), "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
        )

    def test_authors_to_string(self):
        """Tests to string method for authors"""
        self.assertEqual(str(self.book.authors_to_string()), "Danielle Steel")

    def test_genres_to_string(self):
        """Tests to string method for genres"""
        self.assertEqual(str(self.book.genres_to_string()), "Mystery, Fantasy")
