"""Module for connecting to and interacting with psql database"""

import sys
import psycopg2

import ProductionCode.psql_config as config

from ProductionCode.book import Book
from ProductionCode.bookban import Bookban
from ProductionCode.rank import Rank
from ProductionCode.search_section import SearchSectionBook


class DataSource:
    """Class for connecting to and interacting with psql database"""

    instance = None

    def __new__(cls):
        """method insures there is only one DataSource instance"""
        if DataSource.instance is None:
            DataSource.instance = object.__new__(cls)
        return DataSource.instance

    def __init__(self):
        """Constructor that initiates connection to database"""
        self.connection = self.connect()

    def connect(self):
        """Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object."""

        try:
            connection = psycopg2.connect(
                database=config.DATABASE,
                user=config.USER,
                password=config.PASSWORD,
                host="localhost",
            )
        except psycopg2.Error as e:
            print("Connection error: ", e)
            sys.exit()
        return connection

    def _database_row_list_to_book_list(self, row_list) -> list[Book]:
        """Helper method for converting database results to a list of Book objects
        Args:
            row_list (list[Tuple]): a list of rows from an sql query
        Returns:
            (list[Book]): a list of Book objects
        """
        books = list(map(self._database_row_to_book, row_list))
        return books

    def _database_row_to_book(self, row) -> Book:
        """Helper method for converting a database row to a Book object
        Args:
            row (Tuple): a row from the sql query
        Returns:
            (Book): a Book object
        """
        details = {
            "summary": row[3],
            "cover": row[4],
            "genres": row[5],
            "publish_date": row[6],
            "rating": row[7],
        }
        book = Book(isbn=row[0], title=row[1], authors=row[2], details=details)
        return book

    def _database_row_list_to_bookban_list(self, row_list) -> list[Bookban]:
        """Helper method for converting database results to a list of Bookban objects
        Args:
            row_list (list[Tuple]): a list of rows from an sql query
        Returns:
            (list[Bookban]): a list of Bookban objects
        """
        return list(map(self._database_row_to_bookban, row_list))

    def _database_row_to_bookban(self, row) -> Bookban:
        """Helper method for converting a database row to a Bookban object
        Args:
            row (Tuple): a row from the sql query
        Returns:
            (Bookban): a Bookban object
        """
        isbn = row[0]
        book = self.book_from_isbn(isbn)
        bookban = Bookban(
            book=book,
            location={
                "state": row[1],
                "district": row[2],
            },
            details={
                "ban_year": row[3],
                "ban_month": row[4],
                "ban_status": row[5],
                "ban_origin": row[6],
            },
        )
        return bookban

    def _database_row_list_to_rank_list(self, row_list) -> list[Rank]:
        """Helper method for converting a list of rank tuple to a list of Ranks
        Args:
            row (str,int): a name and the number of associated bans
        Returns:
            (Rank): a Rank object
        """
        return list(map(self._database_row_to_rank, row_list))

    def _database_row_to_rank(self, row) -> Rank:
        """Helper method for converting a rank tuple to a Rank object
        Args:
            row (str,int): a name and the number of associated bans
        Returns:
            (Rank): a Rank object
        """
        rank = Rank(name=row[0], bans=row[1])
        return rank

    def _books_to_sections(self, books) -> list[SearchSectionBook]:
        """Helper method to convert a list of books into a list of sections for each letter
        Args:
            books (list[Book]): a list of books
        Returns:
            (list[SearchSectionBook]): a list of SearchSectionBooks

        """
        sections = {}
        for book in books:
            letter = book.title[0]
            section = sections.setdefault(letter, SearchSectionBook(letter, letter, []))
            section.results.append(book)

        sections_list = list(sections.values())
        return sections_list

    def book_from_isbn(self, isbn):
        """Queries book database based on ISBN
        Args:
            isbn (str): a book's isbn number
        Returns:
            (Book): a Book object with the isbn number
        """
        query = "SELECT * FROM books WHERE isbn=%s"
        args = (isbn,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchone()

        except psycopg2.Error as e:
            print("Couldn't find a book with that ISBN: ", e)
            sys.exit()
        if results:
            book = self._database_row_to_book(results)
            return book
        return None

    def bans_from_isbn(self, isbn) -> list[Bookban]:
        """Queries book database based on ISBN
        Args:
            isbn (str): a book's isbn number
        Returns:
            (list[Bookban]): a list of Bookban objects with the isbn number
        """
        query = "SELECT * FROM bookbans WHERE isbn=%s"
        args = (isbn,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find banned book from that ISBN ", e)
            sys.exit()

        bans = self._database_row_list_to_bookban_list(results)
        return bans

    def books_search_title(self, search_term) -> list[Book]:
        """Searches books database for titles containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            (list[Book]): a list of Book objects where titles contain search_term
        """
        query = "SELECT * FROM books WHERE title ILIKE %s ORDER BY title ASC"
        args = ("%" + search_term + "%",)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find a book with that title: ", e)
            sys.exit()

        books = self._database_row_list_to_book_list(results)
        return books

    def books_search_author(self, search_term) -> list[Book]:
        """Searches books database for authors that match search term
        Args:
            search_term (str): the author being searched for
        Returns:
            (list[Book]): a list of Book objects where search_term is in authors
        """
        query = (
            "SELECT * FROM books "
            "WHERE EXISTS ("
            "SELECT 1 "
            "FROM unnest(authors) AS author "
            "WHERE author ILIKE %s"
            ");"
        )
        args = ("%" + search_term + "%",)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find book with that author: ", e)
            sys.exit()

        books = self._database_row_list_to_book_list(results)
        return books

    def search_author(self, search_term) -> list[str]:
        """Searches books database for authors that match search term
        Args:
            search_term (str): the author being searched for
        Returns:
            list (str): a list of authors that match the search term
        """
        query = (
            "SELECT DISTINCT author FROM books, unnest(authors) AS author "
            "WHERE author ILIKE %s;"
        )
        args = ("%" + search_term + "%",)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find book with that author: ", e)
            sys.exit()

        authors = list(map(lambda result: result[0], results))
        return authors

    def search_genre(self, search_term) -> list[str]:
        """Searches books database for genres that match search term
        Args:
            search_term (str): the genre being searched for
        Returns:
            list (str): a list of genres that match the search term
        """
        query = "SELECT DISTINCT genre FROM books, unnest(genres) AS genre WHERE genre ILIKE %s;"
        args = ("%" + search_term + "%",)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find book with that genre: ", e)
            sys.exit()

        genres = list(map(lambda result: result[0], results))
        return genres

    def books_search_genre(self, search_term) -> list[Book]:
        """Searches books database for authors that match search term
        Args:
            search_term (str): the author being searched for
        Returns:
            (list[Book]): a list of Book objects where search_term is in authors
        """
        query = (
            "SELECT * FROM books "
            "WHERE EXISTS ("
            "SELECT 1 "
            "FROM unnest(genres) AS genre "
            "WHERE genre ILIKE %s"
            ");"
        )
        args = ("%" + search_term + "%",)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find book with that author: ", e)
            sys.exit()

        books = self._database_row_list_to_book_list(results)
        return books

    # def books_search_genre(self, search_term) -> list[Book]:
    #     """Searches books database for genres that match search term
    #     Args:
    #         search_term (str): the genre being searched for
    #     Returns:
    #         (list[Book]): a list of Book objects where search_term is in genres
    #     """
    #     query = "SELECT * FROM books WHERE genres @> ARRAY[%s];"
    #     args = (search_term,)

    #     try:
    #         cursor = self.connection.cursor()
    #         cursor.execute(query, args)
    #         results = cursor.fetchall()

    #     except psycopg2.Error as e:
    #         print("Couldn't find book with that genre: ", e)
    #         sys.exit()

    #     books = self.database_row_list_to_book_list(results)
    #     return books

    def get_most_banned_authors(self, max_results):
        """Returns the 5 authors with the most bans."""
        query = (
            "SELECT "
            "author, "
            "COUNT(*) AS ban_count "
            "FROM ( "
            "    SELECT "
            "        UNNEST(b.authors) AS author, "
            "        ban.isbn "
            "    FROM books AS b "
            "    INNER JOIN bookbans AS ban ON b.isbn = CAST(ban.isbn AS TEXT) "
            ") AS subquery "
            "GROUP BY author "
            "ORDER BY ban_count DESC "
            "LIMIT %s;"
        )

        args = (max_results,)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Error getting most banned authors: ", e)
            sys.exit()

        ranks = self._database_row_list_to_rank_list(results)

        return ranks

    def get_most_banned_districts(self, max_results):
        """Searches bookban database for districts with the most bans
        Args:
            max_results (int): the number of results to display
        Returns:
            (list[Rank]): a list of Rank objects of districts and number of bans
        """
        query = (
            "SELECT ban_district, COUNT(*) AS ban_count FROM bookbans GROUP BY ban_district"
            " ORDER BY ban_count DESC LIMIT %s;"
        )
        args = (max_results,)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Error getting most banned districts: ", e)
            sys.exit()

        ranks = self._database_row_list_to_rank_list(results)

        return ranks

    def get_most_banned_states(self, max_results):
        """Searches bookban database for states with the most bans
        Args:
            max_results (int): the number of results to display
        Returns:
            (list[Rank]): a list of Rank objects of states and number of bans
        """
        query = (
            "SELECT ban_state, COUNT(*) AS ban_count FROM bookbans GROUP BY ban_state"
            " ORDER BY ban_count DESC LIMIT %s;"
        )
        args = (max_results,)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Error getting most banned states: ", e)
            sys.exit()

        ranks = self._database_row_list_to_rank_list(results)
        return ranks

    def get_most_banned_states_with_isbn(self, max_results, isbn):
        """Searches bookban database for states with the most bans for a book with a certain isbn
        Args:
            max_results (int): the number of results to display
            isbn (str): the isbn number of the book
        Returns:
            (list[Rank]): a list of Rank objects of states and number of bans
        """
        query = (
            "SELECT ban_state, COUNT(*) AS ban_count FROM bookbans"
            " WHERE isbn = %s GROUP BY ban_state"
            " ORDER BY ban_count DESC LIMIT %s;"
        )
        args = (isbn, max_results)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Error getting most banned states: ", e)
            sys.exit()

        ranks = self._database_row_list_to_rank_list(results)
        return ranks

    def get_most_banned_titles(self, max_results):
        """Searches bookban database for titles with the most bans
        Args:
            max_results (int): the number of results to display
        Returns:
            (list[Rank]): a list of Rank objects of titles and number of bans
        """
        query = (
            "SELECT b.title, COUNT(*) AS ban_count FROM books AS b INNER JOIN bookbans"
            " AS ban ON b.isbn = CAST(ban.isbn AS TEXT) GROUP BY title ORDER BY ban_count"
            " DESC LIMIT %s;"
        )
        args = (max_results,)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Error getting most banned titles: ", e)
            sys.exit()

        ranks = self._database_row_list_to_rank_list(results)

        return ranks

    def get_most_banned_genres(self, max_results):
        """Searches bookban database for genres with the most bans
        Args:
            max_results (int): the number of results to display
        Returns:
            (list[Rank]): a list of Rank objects of genres and number of bans
        """
        query = (
            "SELECT "
            "genre, "
            "COUNT(*) AS ban_count "
            "FROM ( "
            "    SELECT "
            "        UNNEST(b.genres) AS genre, "
            "        ban.isbn "
            "    FROM books AS b "
            "    INNER JOIN bookbans AS ban ON b.isbn = CAST(ban.isbn AS TEXT) "
            ") AS subquery "
            "GROUP BY genre "
            "ORDER BY ban_count DESC "
            "LIMIT %s;"
        )

        args = (max_results,)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Error getting most banned genres: ", e)
            sys.exit()

        ranks = self._database_row_list_to_rank_list(results)

        return ranks

    def get_most_banned_books(self, max_results):
        """Searches bookban database for books with the most bans
        Args:
            max_results (int): the number of results to display
        Returns:
            (list[Book]): a list of Book objects with the most bans
        """

        query = (
            "SELECT b.isbn, COUNT(*) AS ban_count FROM books AS b "
            "INNER JOIN bookbans AS ban ON b.isbn = CAST(ban.isbn AS TEXT) "
            "GROUP BY b.isbn ORDER BY ban_count DESC LIMIT %s;"
        )
        args = (max_results,)
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Error getting most banned books: ", e)
            sys.exit()

        books = list(
            map(lambda result: (result[1], self.book_from_isbn(result[0])), results)
        )

        return books

    def books_search_title_to_sections(self, search_term) -> list[SearchSectionBook]:
        """Searches books database for titles beginning with search term
        Args:
            search_term (str): the string being searched for
        Returns:
            (list[SearchSectionBook]): a list of SearchSectionBook objects where each section
            begins with the letter in the alphabet
        """
        query = "SELECT * FROM books WHERE title ILIKE %s ORDER BY title ASC"
        args = (search_term + "%",)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find a book with that title: ", e)
            sys.exit()

        books = self._database_row_list_to_book_list(results)
        sections = self._books_to_sections(books)
        return sections

    def books_search_genre_to_sections(self, search_term) -> list[SearchSectionBook]:
        """Searches books database for genres matching search term
        Args:
            search_term (str): the string being searched for
        Returns:
            (list[SearchSectionBook]): a list of SearchSectionBook objects where each section
            begins with the letter in the alphabet
        """
        # query = "SELECT * FROM books WHERE title ILIKE %s ORDER BY title ASC"

        query = (
            "SELECT * FROM books "
            "WHERE EXISTS ("
            "SELECT 1 "
            "FROM unnest(genres) AS genre "
            "WHERE genre ILIKE %s"
            ") "
            "ORDER BY title ASC;"
        )
        args = (search_term,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find a book with that title: ", e)
            sys.exit()

        books = self._database_row_list_to_book_list(results)
        sections = self._books_to_sections(books)
        print(sections)
        return sections

    def books_search_author_to_sections(self, search_term) -> list[SearchSectionBook]:
        """Searches books database for authors matching search term
        Args:
            search_term (str): the string being searched for
        Returns:
            (list[SearchSectionBook]): a list of SearchSectionBook objects where each section
            begins with the letter in the alphabet
        """
        # query = "SELECT * FROM books WHERE title ILIKE %s ORDER BY title ASC"

        query = (
            "SELECT * FROM books "
            "WHERE EXISTS ("
            "SELECT 1 "
            "FROM unnest(authors) AS author "
            "WHERE author ILIKE %s"
            ") "
            "ORDER BY title ASC;"
        )
        args = (search_term,)

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, args)
            results = cursor.fetchall()

        except psycopg2.Error as e:
            print("Couldn't find a book with that title: ", e)
            sys.exit()

        books = self._database_row_list_to_book_list(results)
        sections = self._books_to_sections(books)
        print(sections)
        return sections
