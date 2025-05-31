"""Module for testing the Bookban class"""

import unittest

from Tests.mock_data import mock_ban


class TestBookban(unittest.TestCase):
    """Tests for Bookban class"""

    def setUp(self):
        self.bookban = mock_ban

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
