"""Module for connecting to and interacting with psql database"""

import psycopg2

import psql_config as config

from ProductionCode.book import Book
from ProductionCode.bookban import Bookban


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
        """Helper method for converting database results to a list of Book objects
        Args:
            row_list (list[Tuple]): a list of rows from an sql query
        Returns:
            (list[Book]): a list of Book objects
        """
        return list(map(self.database_row_to_book, row_list))

    def database_row_to_book(self, row) -> Book:
        """Helper method for converting a database row to a Book object
        Args:
            row (Tuple): a row from the sql query
        Returns:
            (Book): a Book object
        """
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
        """Helper method for converting database results to a list of Bookban objects
        Args:
            row_list (list[Tuple]): a list of rows from an sql query
        Returns:
            (list[Bookban]): a list of Bookban objects
        """
        return list(map(self.database_row_to_bookban, row_list))

    def database_row_to_bookban(self, row) -> Bookban:
        """Helper method for converting a database row to a Bookban object
        Args:
            row (Tuple): a row from the sql query
        Returns:
            (Bookban): a Bookban object
        """
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
            ban_year=row[3],
            ban_month=row[4],
            ban_status=row[5],
            ban_origin=row[6],
        )
        return bookban

    def books_search_title(self, search_term) -> list[Book]:
        """Searches books database for titles containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            (list[Book]): a list of Book objects where titles contain search_term
        """
        query = "SELECT * FROM books WHERE title ILIKE %s"
        args = ("%" + search_term + "%",)

        results = self.execute_query(query, args)
        books = self.database_row_list_to_book_list(results)
        return books

    def books_search_author(self, search_term) -> list[Book]:
        """Searches books database for authors that match search term
        Args:
            search_term (str): the author being searched for
        Returns:
            (list[Book]): a list of Book objects where search_term is in authors
        """
        query = "SELECT * FROM books WHERE authors @> ARRAY[%s];"
        args = (search_term,)

        results = self.execute_query(query, args)
        books = self.database_row_list_to_book_list(results)
        return books

    def books_search_genre(self, search_term) -> list[Book]:
        """Searches books database for genres that match search term
        Args:
            search_term (str): the genre being searched for
        Returns:
            (list[Book]): a list of Book objects where search_term is in genres
        """
        query = "SELECT * FROM books WHERE genres @> ARRAY[%s];"
        args = (search_term,)

        results = self.execute_query(query, args)
        books = self.database_row_list_to_book_list(results)
        return books

    # def get_bans_per_year(self):
    #     """Returns the number of bans per year from 2020 to 2025."""
    #     query = (
    #         "SELECT year_banned, COUNT(*) AS bans_in_year "
    #         "FROM bookbans "
    #         "WHERE year_banned BETWEEN 2020 AND 2025 "
    #         "GROUP BY year_banned "
    #         "ORDER BY year_banned;"
    #     )

    def search_secondary_author(self, search_term):
        """Searches booksbans database for secondary authors containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where secondary author contains the search term
        """
        query = "SELECT * FROM bookbans WHERE secondary_author ILIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()
        return results
    
    def search_illustrator(self, search_term):
        """Searches booksbans database for illustrators containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where illustrator contains the search term
        """
        query = "SELECT * FROM bookbans WHERE illustrator ILIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()
        return results
    
    def search_translator(self, search_term):
        """Searches booksbans database for translators containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where translator contains the search term
        """
        query = "SELECT * FROM bookbans WHERE translator ILIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()
        return results
    
    def search_state(self, search_term):
        """Searches booksbans database for states containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where state contains the search term
        """
        query = "SELECT * FROM bookbans WHERE state ILIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()
        return results
    
    def search_district(self, search_term):
        """Searches booksbans database for districts containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where district contains the search term
        """
        query = "SELECT * FROM bookbans WHERE district ILIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()
        return results
    
    def get_date_of_challenge(self):
        """Returns the date of challenge for all bans."""
        query = "SELECT date_of_challenge FROM bookbans ORDER BY date_of_challenge;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results

    def get_ban_status(self):
        """Returns the status of all bans."""
        query = "SELECT ban_status FROM bookbans ORDER BY ban_status;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results

    def get_origin_of_challenge(self):
        """Returns the origin of challenge for all bans."""
        query = "SELECT origin_of_challenge FROM bookbans ORDER BY origin_of_challenge;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results

    def get_bans_per_year(self):
        """Returns the number of bans per year from 2020 to 2025."""
        query = "SELECT year_banned, COUNT(*) AS bans_in_year FROM bookbans WHERE year_banned BETWEEN 2020 AND 2025 GROUP BY year_banned ORDER BY year_banned;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results

    def get_most_common_words(self):
        """Returns the 5 most common words in the titles of banned books."""
        query = "SELECT word, COUNT(*) AS occurrences FROM (SELECT regexp_split_to_table(lower(title), E'\\W+') AS word FROM bookbans) AS words WHERE word <> '' GROUP BY word ORDER BY occurrences DESC LIMIT 5;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results
    
    def get_most_banned_authors(self):
        """Returns the 5 authors with the most bans."""
        query = "SELECT author, COUNT(*) AS ban_count FROM bookbans GROUP BY author ORDER BY ban_count DESC LIMIT 5;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results

    def get_most_banned_districts(self):
        query = "SELECT district, COUNT(*) AS ban_count FROM bookbans GROUP BY district ORDER BY ban_count DESC LIMIT 5;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results

    def get_most_banned_states(self):
        """Returns the 5 states with the most bans."""
        query = "SELECT state, COUNT(*) AS ban_count FROM bookbans GROUP BY state ORDER BY ban_count DESC LIMIT 5;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results

    def get_most_banned_titles(self):
        """Returns the 5 titles with the most bans."""
        query = "SELECT title, COUNT(*) AS ban_count FROM bookbans GROUP BY title ORDER BY ban_count DESC LIMIT 5;"
        cursor = self.connection.cursor()
        cursor.execute(query)

        results = cursor.fetchall()
        return results


if __name__ == "__main__":
    my_ds = DataSource()
    # results = my_ds.search_author("Haruki Murakami")
    output = my_ds.books_search_title("killing")
    for result in output:
        print(result)


