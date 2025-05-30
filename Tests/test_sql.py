"""This file contains the unit tests for the SQL queries."""

import unittest
from unittest.mock import MagicMock, patch
import psycopg2

from ProductionCode.datasource import DataSource

from ProductionCode.rank import Rank

from Tests.mock_data import mock_book
from Tests.mock_data import mock_ban


class TestSQLSearchMethods(unittest.TestCase):
    """This class tests search methods for SQL queries"""

    def setUp(self):
        """Create a mock prostgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_title(self, mock_connect):
        """Tests search title method for the books database"""
        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = [
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        ]

        expected = [mock_book]

        self.mock_cursor.fetchall.return_value = response

        results = ds.books_search_title("Kaleidoscope")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_author(self, mock_connect):
        """Tests search author method for books database"""
        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = [
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        ]

        expected = [mock_book]

        self.mock_cursor.fetchall.return_value = response

        results = ds.books_search_author("Danielle Steel")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_genre(self, mock_connect):
        """Tests search genre method for books database"""

        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = [
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        ]

        expected = [mock_book]

        self.mock_cursor.fetchall.return_value = response

        results = ds.books_search_genre("Mystery")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))


class TestSQLFromISBNMethods(unittest.TestCase):
    """This class tests methods from isbn for SQL queries"""

    def setUp(self):
        """Create a mock postgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_book_from_isbn(self, mock_connect):
        """Tests search book by isbn method for book database"""
        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = (
            "440236924",
            "Kaleidoscope",
            ["Danielle Steel"],
            "summary",
            "url.jpg",
            ["Mystery", "Fantasy"],
            "2020-10-27",
            3.9,
        )

        expected = mock_book

        self.mock_cursor.fetchone.return_value = response

        results = ds.book_from_isbn("440236924")

        self.assertEqual(str(results), str(expected))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_book_from_isbn_no_results(self, mock_connect):
        """Tests search book by isbn method for book database"""
        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = None

        expected = None
        self.mock_cursor.fetchone.return_value = response

        results = ds.book_from_isbn("440236924")

        self.assertEqual(str(results), str(expected))

    @patch("ProductionCode.datasource.DataSource.database_row_list_to_bookban_list")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_bans_from_isbn(self, mock_connect, mock_database_row_list_to_bookban_list):
        """Tests search book bans by isbn method for bookbans database"""
        mock_connect.return_value = self.mock_conn

        mock_database_row_list_to_bookban_list.return_value = [mock_ban]

        ds = DataSource()

        response = [
            (
                "440236924",
                "Florida",
                "Martin County Schools",
                2023,
                3,
                "Banned from Libraries and Classrooms",
                "Formal Challenge",
            )
        ]

        expected = [mock_ban]
        self.mock_cursor.fetchall.return_value = response

        results = ds.bans_from_isbn("440236924")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))


class TestSQLHelperMethods(unittest.TestCase):
    """This class tests the helper methods for SQL queries"""

    def setUp(self):
        """Create a mock postgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_to_book(self, _mock_connect):
        """Converting database row to book object test"""

        ds = DataSource()

        expected = mock_book

        results = ds.database_row_to_book(
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        )

        self.assertEqual(str(results), str(expected))

    @patch("ProductionCode.datasource.DataSource.database_row_to_book")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_list_to_book_list(
        self, mock_connect, mock_database_row_to_book
    ):
        """Converting database row to book object list test"""
        mock_connect.return_value = self.mock_conn

        mock_database_row_to_book.return_value = mock_book

        ds = DataSource()

        expected = [mock_book, mock_book]

        results = ds.database_row_list_to_book_list(
            [
                (
                    "440236924",
                    "Kaleidoscope",
                    ["Danielle Steel"],
                    "summary",
                    "url.jpg",
                    ["Mystery", "Fantasy"],
                    "2020-10-27",
                    3.9,
                ),
                (
                    "440236924",
                    "Kaleidoscope",
                    ["Danielle Steel"],
                    "summary",
                    "url.jpg",
                    ["Mystery", "Fantasy"],
                    "2020-10-27",
                    3.9,
                ),
            ]
        )

        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.DataSource.book_from_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_to_bookban(self, mock_connect, mock_book_from_isbn):
        """Test for helper method converting database row to bookban"""
        mock_connect.return_value = self.mock_conn

        mock_book_from_isbn.return_value = mock_book

        ds = DataSource()

        expected = (
            "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
            " banned in Martin County Schools, Florida as of 3, 2023"
        )

        result = ds.database_row_to_bookban(
            (
                "440236924",
                "Florida",
                "Martin County Schools",
                2023,
                3,
                "Banned from Libraries and Classrooms",
                "Formal Challenge",
            )
        )

        self.assertEqual(str(result), expected)

    @patch("ProductionCode.datasource.DataSource.database_row_to_bookban")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_list_to_bookban_list(
        self, mock_connect, mock_database_row_to_bookban
    ):
        """Test for helper method converting database row to bookban"""
        mock_connect.return_value = self.mock_conn

        mock_database_row_to_bookban.return_value = mock_ban

        ds = DataSource()

        expected = [
            "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
            " banned in Martin County Schools, Florida as of 3, 2023",
            "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
            " banned in Martin County Schools, Florida as of 3, 2023",
        ]

        result = ds.database_row_list_to_bookban_list(
            [
                (
                    "440236924",
                    "Florida",
                    "Martin County Schools",
                    2023,
                    3,
                    "Banned from Libraries and Classrooms",
                    "Formal Challenge",
                ),
                (
                    "440236924",
                    "Florida",
                    "Martin County Schools",
                    2023,
                    3,
                    "Banned from Libraries and Classrooms",
                    "Formal Challenge",
                ),
            ]
        )

        self.assertEqual(list(map(str, result)), expected)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_to_rank(self, _mock_connect):
        """Converting database row to rank object test"""
        ds = DataSource()

        expected = Rank("Florida", 50)

        result = ds.database_row_to_rank(("Florida", 50))

        self.assertEqual(str(expected), str(result))

    @patch("ProductionCode.datasource.DataSource.database_row_to_rank")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_list_to_rank_list(
        self, mock_connect, mock_database_row_to_rank
    ):
        """Converting database row list to rank object list test"""
        mock_connect.return_value = self.mock_conn
        mock_database_row_to_rank.return_value = Rank("Florida", 50)

        ds = DataSource()

        expected = [Rank("Florida", 50), Rank("Florida", 50)]

        result = ds.database_row_list_to_rank_list([("Florida", 50), ("Florida", 50)])

        self.assertEqual(list(map(str, result)), list(map(str, expected)))


class TestSQLMostBannedMethods(unittest.TestCase):
    """Tests for most_banned methods"""

    def setUp(self):
        """Create a mock prostgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_authors(self, mock_connect):
        """Test get_most_banned_authors"""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [(["Sarah J. Maas"], 52)]
        expected = ["['Sarah J. Maas']: 52"]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_authors(1)
        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_districts(self, mock_connect):
        """Test get_most_banned_districts"""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [("Escambia County Public Schools", 23)]
        expected = ["Escambia County Public Schools: 23"]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_districts(1)
        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states(self, mock_connect):
        """Test get_most_banned_states"""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [("Florida", 87)]
        expected = ["Florida: 87"]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_states(1)
        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states_with_isbn(self, mock_connect):
        """Test get_most_banned_states"""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [("Florida", 2)]
        expected = ["Florida: 2"]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_states_with_isbn(1, "1534430652")
        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_titles(self, mock_connect):
        """Test get_most_banned_titles"""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [("Kingdom of Ash", 52)]
        expected = ["Kingdom of Ash: 52"]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_titles(1)
        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.DataSource.book_from_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_books(self, mock_connect, mock_book_from_isbn):
        """Test get_most_banned_books with a limit of 1."""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [("1639731067", 52)]
        expected = [(52, "Kingdom of Ash by Sarah J. Maas (ISBN: 1639731067)")]
        self.mock_cursor.fetchall.return_value = response
        mock_book_from_isbn.return_value = (
            "Kingdom of Ash by Sarah J. Maas (ISBN: 1639731067)"
        )
        results = ds.get_most_banned_books(1)

        self.assertEqual(results, expected)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_genres(self, mock_connect):
        """Test get_most_banned_genres with a limit of 1."""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [("Fiction", 120)]
        expected = ["Fiction: 120"]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_genres(1)

        self.assertEqual(list(map(str, results)), expected)


class TestSQLExceptionBranches(unittest.TestCase):
    """Tests for Errors"""

    def setUp(self):
        """Setup mock psql connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    def test_connect_error(self):
        """Test connection error"""
        with self.assertRaises(SystemExit):
            DataSource()

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_book_from_isbn_error(self, mock_connect):
        """If the SELECT fails, we sys.exit() in book_from_isbn"""
        mock_connect.return_value = self.mock_conn

        self.mock_cursor.execute.side_effect = psycopg2.Error("boom")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.book_from_isbn("12345")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_title_error(self, mock_connect):
        """Trigger the except-clause in books_search_title"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("oh no")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.books_search_title("anything")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_author_error(self, mock_connect):
        """Trigger the except-clause in books_search_author"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("fail")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.books_search_author("someone")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_genre_error(self, mock_connect):
        """Trigger the except-clause in books_search_genre"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("oops")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.books_search_genre("fantasy")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_bans_from_isbn_error(self, mock_connect):
        """Trigger the except-clause in bans_from_isbn"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("nope")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.bans_from_isbn("440236924")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_author_error(self, mock_connect):
        """Trigger the except-clause in get_most_banned_authors"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_authors(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_districts_error(self, mock_connect):
        """Trigger the except-clause in get_most_banned_districts"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_districts(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states_error(self, mock_connect):
        """Trigger the except-clause in get_most_banned_states"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_states(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states_with_isbn_error(self, mock_connect):
        """Trigger the except-clause in get_most_banned_states"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_states_with_isbn(1, "1534430652")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_titles_error(self, mock_connect):
        """Trigger the except-clause in get_most_banned_titles"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_titles(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_books_error(self, mock_connect):
        """Trigger the except-clause in get_most_banned_books"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_books(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_genres_error(self, mock_connect):
        """Trigger the except-clause in get_most_banned_genres"""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_genres(1)


class TestSingleton(unittest.TestCase):
    """This class tests singleton functionality of datasource"""

    def setUp(self):
        """Create a mock prostgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_singleton(self, mock_connect):
        """Test singleton functionality of datasource"""
        mock_connect.return_value = self.mock_conn

        ds1 = DataSource()
        ds2 = DataSource()
        self.assertEqual(id(ds1), id(ds2))
