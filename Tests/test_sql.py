"""
This file contains the unit tests for the SQL queries.
"""

import unittest
from unittest.mock import patch
from ProductionCode.datasource import (
    books_search_title,
    search_author,
    search_title_like,
    search_genre,
    get_bans_per_year,
    get_most_common_words,
    get_most_banned_authors,
    get_keyword,
    get_most_banned_districts,
    get_most_banned_states,
    get_most_banned_titles
)

class TestSQLQueries(unittest.TestCase):
    """
    This class tests the SQL queries.
    """

    def setUp(self):
        #create mock connection
        self.mock_conn = MagicMock()
        self mock_cursor = self.mock_conn.cursor.return_value
    
    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_get_most_banned_authors(self, mock_connect):
        #link the mock connection
        mock_connect.return_value = self.mock_conn
            #set what it should return
        self.mock_cursor.fetchone.return_value = ("most_banned_authors")
        self.assertEqual(books_search_title(""), "most_bannedPauthors")