"""
This file contains the unit tests for the Flask application.
"""

import unittest
from unittest.mock import MagicMock, patch

import psycopg2

from app import app

from ProductionCode.rank import Rank

from Tests.mock_data import mock_book, mock_ban, mock_search_section


class TestAppPages(unittest.TestCase):
    """Tests for webpages"""

    def setUp(self):
        """Create a mock psql connection and app"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        self.app = app.test_client()

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_index(self, mock_connect):
        """Tests index page"""
        mock_connect.return_value = self.mock_conn

        response = self.app.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>The Forbidden Library</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.book_from_isbn")
    @patch("ProductionCode.datasource.DataSource.bans_from_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_details(self, mock_connect, mock_bans_from_isbn, mock_book_from_isbn):
        """Tests details page"""
        mock_connect.return_value = self.mock_conn
        mock_book_from_isbn.return_value = mock_book
        mock_bans_from_isbn.return_value = [mock_ban]

        response = self.app.get("details/440236924")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2 class="right-title">Kaleidoscope</h2>', response.data)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_map(self, mock_connect):
        """Tests map page"""
        mock_connect.return_value = self.mock_conn

        response = self.app.get("map")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Banned Books in the United States</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.books_search_author")
    @patch("ProductionCode.datasource.DataSource.books_search_title")
    @patch("ProductionCode.datasource.DataSource.book_from_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search(
        self,
        mock_connect,
        mock_book_from_isbn,
        mock_books_search_title,
        mock_books_search_author,
    ):
        """Tests search page with no type"""
        mock_connect.return_value = self.mock_conn
        mock_book_from_isbn.return_value = mock_book
        mock_books_search_title.return_value = [mock_book]
        mock_books_search_author.return_value = [mock_book]

        response = self.app.get("search?searchterm=a")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Search Results for "a":</h1>', response.data)

    @patch("ProductionCode.datasource.DataSource.books_search_title")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search_title(
        self,
        mock_connect,
        mock_books_search_title,
    ):
        """Tests search page for title"""
        mock_connect.return_value = self.mock_conn
        mock_books_search_title.return_value = [mock_book]

        response = self.app.get("search?searchterm=Kaleidoscope&type=title")

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'<p class="book-title"><a href="details/440236924">Kaleidoscope </a>',
            response.data,
        )
        print(response.data.decode())

    # TODO: FIX THIS TEST
    @patch("ProductionCode.datasource.DataSource.books_search_author")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search_author(
        self,
        mock_connect,
        mock_books_search_author,
    ):
        """Tests search page for author"""
        mock_connect.return_value = self.mock_conn
        mock_books_search_author.return_value = [mock_book]

        response = self.app.get("search?searchterm=Steel&type=author")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p class="book-authors">Danielle Steel</p>', response.data)

    @patch("ProductionCode.datasource.DataSource.books_search_title")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books(
        self,
        mock_connect,
        mock_books_search_title,
    ):
        """Tests books page"""
        mock_connect.return_value = self.mock_conn
        mock_books_search_title.return_value = [mock_book]

        response = self.app.get("books")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Banned Books</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.books_search_genre")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_genres(
        self,
        mock_connect,
        mock_books_search_title,
    ):
        """Tests genres page"""
        mock_connect.return_value = self.mock_conn
        mock_books_search_title.return_value = [mock_book]

        response = self.app.get("genre/Fiction")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Fiction</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.books_search_genre")
    @patch("ProductionCode.datasource.DataSource.books_search_title")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_genres_list(
        self, mock_connect, mock_books_search_title, mock_books_search_genre
    ):
        """Tests overall genres page"""
        mock_connect.return_value = self.mock_conn
        mock_books_search_title.return_value = [mock_book]
        mock_books_search_genre.return_value = [mock_book]

        response = self.app.get("genres")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h2>Genres</h2>", response.data)

    @patch("ProductionCode.datasource.DataSource.books_search_author")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_authors(
        self,
        mock_connect,
        mock_books_search_author,
    ):
        """Tests authors page"""
        mock_connect.return_value = self.mock_conn
        mock_books_search_author.return_value = [mock_book]

        response = self.app.get("author/Danielle Steel")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h1>Danielle Steel</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.books_search_title")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_authors_list(
        self,
        mock_connect,
        mock_books_search_title,
    ):
        """Tests authors page"""
        mock_connect.return_value = self.mock_conn
        mock_books_search_title.return_value = [mock_book]

        response = self.app.get("authors")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<h3>Authors</h3>", response.data)

    @patch("ProductionCode.datasource.DataSource.get_most_banned_authors")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_authors(
        self,
        mock_connect,
        mock_get_most_banned_authors,
    ):
        """Tests most banned authors page"""
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_authors.return_value = [Rank("Danielle Steel", 50)]

        response = self.app.get("most-banned-authors")

        self.assertIn(b"<h1>Most Banned Authors</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.get_most_banned_states")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_states(
        self,
        mock_connect,
        mock_get_most_banned_states,
    ):
        """Tests most banned states page"""
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_states.return_value = [Rank("Florida", 50)]

        response = self.app.get("most-banned-states")

        self.assertIn(b"<h1>Most Banned States</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.get_most_banned_districts")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_districts(
        self,
        mock_connect,
        mock_get_most_banned_districts,
    ):
        """Tests most banned districts page"""
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_districts.return_value = [Rank("Florida County", 50)]

        response = self.app.get("most-banned-districts")

        self.assertIn(b"<h1>Most Banned Districts</h1>", response.data)

    @patch("ProductionCode.datasource.DataSource.get_most_banned_books")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_most_banned_books(
        self,
        mock_connect,
        mock_get_most_banned_books,
    ):
        """Tests most banned books page"""
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_books.return_value = [(50, mock_book)]

        response = self.app.get("most-banned-books")

        self.assertIn(b"<h1>Most Banned Books</h1>", response.data)


class TestAppError(unittest.TestCase):
    """Tests for Errors"""

    @app.route("/mock-error")
    def mock_error(self):
        """Helper method to raise a mock error"""
        raise psycopg2.Error("Mock Error")

    def setUp(self):
        """Create mock psql connection and app"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        self.app = app.test_client()

    def test_404(self):
        """Tests 404 page"""
        response = self.app.get("/not-a-real-page", follow_redirects=True)
        self.assertIn(b"404", response.data)

    @patch("app.map_page", side_effect=Exception("Mock Error"))
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_500(self, _mock_connect, _mock_map):
        """Tests 500 page"""
        response = self.app.get("/mock-error")
        self.assertIn(b"500", response.data)


class TestAppAPI(unittest.TestCase):
    """Tests for API endpoints"""

    def setUp(self):
        """Create mock psql connection and app"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        self.app = app.test_client()

    @patch("ProductionCode.datasource.DataSource.get_most_banned_states")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states(self, mock_connect, mock_get_most_banned_states):
        """Test get-most-banned-states endpoint"""
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_states.return_value = [
            Rank("Florida", 500),
            Rank("Texas", 400),
        ]

        response = self.app.get("get-most-banned-states")

        expected = b'[{"name": "Florida", "bans": 500}, {"name": "Texas", "bans": 400}]'

        self.assertEqual(response.data, expected)

    @patch("ProductionCode.datasource.DataSource.get_most_banned_states_with_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states_with_isbn(
        self, mock_connect, mock_get_most_banned_states_with_isbn
    ):
        """Test get-most-banned-states endpoint"""
        mock_connect.return_value = self.mock_conn
        mock_get_most_banned_states_with_isbn.return_value = [
            Rank("Florida", 2),
            Rank("Texas", 1),
        ]

        response = self.app.get("get-most-banned-states-with-isbn?1534430652")

        expected = b'[{"name": "Florida", "bans": 2}, {"name": "Texas", "bans": 1}]'

        self.assertEqual(response.data, expected)


if __name__ == "__main__":
    unittest.main()
