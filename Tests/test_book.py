"""Module for testing Book class"""

import unittest

from ProductionCode.book import Book

from Tests.mock_data import mock_book


class TestBook(unittest.TestCase):
    """Tests for Book class"""

    def setUp(self):
        self.book = mock_book

        self.mock_book_no_genres = Book(
            isbn="1639731067",
            title="Kingdom of Ash",
            authors=["Sarah J. Maas"],
            details={
                "summary": "summary",
                "cover": "cover.jpg",
                "genres": [],
                "publish_date": "2019-09-19",
                "rating": 3.7,
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
        """Tests to string method for genres"""
        self.assertEqual(str(self.book.genres_to_string()), "Mystery, Fantasy")

    def test_genres_to_string_empty(self):
        """Tests to string method for genres"""
        self.assertEqual(str(self.mock_book_no_genres.genres_to_string()), "")
