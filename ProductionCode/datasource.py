"""Module for connecting to and interacting with psql database"""

import psycopg2

import psl_config as config

from book import Book
from bookban import Bookban


class DataSource:
    """Class for connecting to and interacting with psql database"""

    def __init__(self):
        """Constructor that initiates connection to database"""
        self.connection = self.connect()

    def connect(self):
        """Initiates connection to database using information in the psqlConfig.py file.
        Returns the connection object."""

        try:
            connection = psycopg2.connect(
                database=config.database,
                user=config.user,
                password=config.password,
                host="localhost",
            )
        except psycopg2.OperationalError as e:
            print("Connection error: ", e)
        return connection

    def execute_query(self, query, args=None):
        """Helper method for executing sql queries
        Args:
            query (str): sql query
            args (Tuple): arguments for query
        Returns:
            query response
        """
        # TODO: Should probably add error handling
        cursor = self.connection.cursor()
        if args is None:
            cursor.execute(query)
        else:
            cursor.execute(query, args)
        results = cursor.fetchall()
        return results

    def database_row_list_to_book_list(self, row_list) -> list[Book]:
        return list(map(self.database_row_to_book, row_list))

    def database_row_to_book(self, row) -> Book:
        book = Book(
            isbn=row[0],
            title=row[1],
            authors=row[2],
            summary=row[3],
            cover=row[4],
            genres=row[5],
            publish_date=row[6],
            rating=row[7],
        )
        return book

    def database_row_list_to_bookban_list(self, row_list) -> list[Bookban]:
        return list(map(self.database_row_to_bookban, row_list))

    def database_row_to_bookban(self, row) -> Bookban:
        isbn = row[0]
        # TODO: something to get the book associated with the isbn

        # for now, dummy book data
        book = Book(
            isbn="000000000",
            title="Book Title",
            authors=["Author"],
            summary="summary of book",
            genres=["First Genre", "Second Genre"],
            cover="url",
            publish_date=57891375319,
            rating=5.0,
        )
        bookban = Bookban(
            book=book,
            state=row[1],
            district=row[2],
            ban_date=row[3],
            ban_status=row[4],
            ban_origin=row[5],
        )
        return bookban

    def books_search_title(self, search_term) -> list[Book]:
        query = "SELECT * FROM books WHERE title ILIKE %s"
        args = ("%" + search_term + "%",)

        results = self.execute_query(query, args)
        books = self.database_row_list_to_book_list(results)
        return books

    def search_author(self, search_term) -> list[Bookban]:
        """Searches bookbans database for authors exactly matching search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where author is the search term
            test = DataSource()

        """
        query = "SELECT * FROM bookbans WHERE author=%s"
        args = (search_term,)

        results = self.execute_query(query, args)
        bookbans = self.database_row_list_to_bookban_list(results)

        return bookbans

    def search_title_like(self, search_term):
        """Searches booksbans database for titles containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where title contains the search term
        """
        query = "SELECT * FROM bookbans WHERE title ILIKE %s"
        # search_term = "Angel"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()
        return results

    def search_genre(self, search_term):
        """Searches booksbans database for genres containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where genre contains the search term
        """
        query = "SELECT * FROM bookbans WHERE genre ILIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()

        return results

    def get_bans_per_year(self):
        """Returns the number of bans per year from 2020 to 2025."""
        query = (
            "SELECT year_banned, COUNT(*) AS bans_in_year "
            "FROM bookbans "
            "WHERE year_banned BETWEEN 2020 AND 2025 "
            "GROUP BY year_banned "
            "ORDER BY year_banned;"
        )

    def get_most_common_words(self):
        """Returns the 5 most common words in the titles of banned books."""
        query = (
            "SELECT word, COUNT(*) AS occurrences "
            "FROM ("
            "  SELECT regexp_split_to_table(lower(title), E'\\W+') AS word "
            "  FROM bookbans"
            ") AS words "
            "WHERE word <> '' "
            "GROUP BY word "
            "ORDER BY occurrences DESC "
            "LIMIT 5;"
        )

    def get_most_banned_authors(self):
        """Returns the 5 authors with the most bans."""
        query = (
            "SELECT author, COUNT(*) AS ban_count "
            "FROM bookbans "
            "GROUP BY author "
            "ORDER BY ban_count DESC "
            "LIMIT 5;"
        )

    def get_keyword(self, keyword):
        """Returns all books that contain the given keyword in their title."""
        query = (
            "SELECT title, author, year_banned "
            "FROM bookbans "
            f"WHERE title ILIKE '%{keyword}%' "
            "ORDER BY title;"
        )

    def get_most_banned_districts(self):
        """Returns the 5 districts with the most bans."""
        query = (
            "SELECT district, COUNT(*) AS ban_count "
            "FROM bookbans "
            "GROUP BY district "
            "ORDER BY ban_count DESC "
            "LIMIT 5;"
        )

    def get_most_banned_states(self):
        """Returns the 5 states with the most bans."""
        query = (
            "SELECT state, COUNT(*) AS ban_count "
            "FROM bookbans "
            "GROUP BY state "
            "ORDER BY ban_count DESC "
            "LIMIT 5;"
        )

    def get_most_banned_titles(self):
        """Returns the 5 titles with the most bans."""
        query = (
            "SELECT title, COUNT(*) AS ban_count "
            "FROM bookbans "
            "GROUP BY title "
            "ORDER BY ban_count DESC "
            "LIMIT 5;"
        )


if __name__ == "__main__":
    my_ds = DataSource()
    # results = my_ds.search_author("Haruki Murakami")
    results = my_ds.books_search_title("a")
    for result in results:
        print(result)
