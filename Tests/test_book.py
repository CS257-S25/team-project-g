"""Module for testing Book class"""

import unittest

from ProductionCode.book import Book


class TestBook(unittest.TestCase):
    """Tests for Book class"""

    def setUp(self):
        self.book = Book(
            isbn="440236924",
            title="Kaleidoscope",
            authors=["Danielle Steel"],
            details={
                "summary": "summary",
                "cover": "cover.url",
                "genres": [
                    "Adult Fiction",
                    "Contemporary Romance",
                ],
                "publish_date": "2000-10-28",
                "rating": 4.0,
            },
        )

    def test_string(self):
        """Tests __str__ method"""
        self.assertEqual(
            str(self.book), "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
        )

    def test_authors_to_string(self):
        """Tests to string method for authors"""
        self.assertEqual(str(self.book.authors_to_string()), "Danielle Steel")
    def test_genres_to_string(self):
        """Tests to string method for authors"""
        self.assertEqual(str(self.book.genres_to_string()), "Adult Fiction, Contemporary Romance")
