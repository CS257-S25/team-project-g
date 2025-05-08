"""
This file contains the unit tests for the SQL queries.
"""

import unittest
from unittest.mock import MagicMock, patch
from ProductionCode.datasource import (
    books_search_title,
    book_from_isbn,
    books_search_author,
    books_search_genre,
    get_most_banned_authors,
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
        self.mock_cursor = self.mock_conn.cursor.return_value
    
    @patch('ProductionCode.datasource.psycopg2.connect')
    def test_book_search_title_killing(self, mock_connect):
        response = (
            "Killing Jesus: A History by Martin Dugard, Bill O'Reilly (ISBN: 1250142202)"
            "Killing Mr. Griffin by Lois Duncan (ISBN: None)"
            "Killing Reagan: The Violent Assault That Changed a Presidency by Martin Dugard, Bill O'Reilly (ISBN: 1427274908)"
            "Killing Time in Crystal City by Chris    Lynch (ISBN: 1442440112)"
            "Killing Lincoln: The Shocking Assassination that Changed America Forever by Martin Dugard, Bill O'Reilly (ISBN: 805093079)")
        #link the mock connection
        mock_connect.return_value = self.mock_conn
            #set what it should return
        self.mock_cursor.fetchone.return_value = (response)
        self.assertEqual(books_search_title('Killing Jesus: '), response)

    def test_search_isbn(self, mock_connect):
        response = ()
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = response
        self.asseertEqual(book_from_isbn(440236924), response)

    def test_search_author(self, mock_connect):
        response = ()
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = response
        self.asseertEqual(books_search_author('Kaleidoscope'), response)

    def test_search_genre(self, mock_connect):
        response = ()
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = response
        self.assertEqual(books_search_genre('Animal Fiction'), response)

    def test_get_most_banned_authors(self, mock_connect):
        response = ()
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = response
        self.assertEqual(get_most_banned_authors(1), response)

    def test_get_most_banned_districts(self, mock_connect):
        response = ()
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = response
        self.assertEqual(get_most_banned_districts(1), response)

    def test_get_most_banned_states(self, mock_connect):
        response = ()
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = response
        self.assertEqual(get_most_banned_states(1), response)

    def test_get_most_banned_titles(self, mock_connect):
        response = ()
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.fetchone.return_value = response
        self.assertEqual(get_most_banned_titles(1), response)