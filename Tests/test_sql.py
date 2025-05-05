"""
This file contains the unit tests for the SQL queries.
"""

import unittest

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
        self.assertEqual(get_most_banned_authors(5), "most_bannedPauthors")