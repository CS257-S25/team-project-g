"""Module for testing the Bookban class"""

import unittest

from ProductionCode.book import Book
from ProductionCode.bookban import Bookban


class TestBookban(unittest.TestCase):
    """Tests for Bookban class"""

    def setUp(self):
        book = Book(
            isbn="440236924",
            title="Kaleidoscope",
            authors=["Danielle Steel"],
            details={
                "summary": "summary",
                "cover": "cover.jpg",
                "genres": [
                    "Adult Fiction",
                    "Contemporary Romance",
                ],
                "publish_date": "2000-10-28",
                "rating": 4.0,
            },
        )

        self.bookban = Bookban(
            book=book,
            state="Florida",
            district="Martin County Schools",
            ban_year=2023,
            ban_month=3,
            ban_status="Banned from Libraries and Classrooms",
            ban_origin="Formal Challenge",
        )

    def test_string(self):
        """Tests __str__ method"""
        self.assertEqual(
            str(self.bookban),
            "Kaleidoscope by Danielle Steel (ISBN: 440236924) "
            "banned in Martin County Schools, Florida as of 3, 2023",
        )

    def test_date_to_str(self):
        """Tests date to string method"""
        self.assertEqual(self.bookban.date_to_str(), "3, 2023")
