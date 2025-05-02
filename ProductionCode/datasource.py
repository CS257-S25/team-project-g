"""Module for connecting to and interacting with psql database"""

import psycopg2

import psql_config as config


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

    def search_author(self, search_term):
        """Searches booksbans database for authors exactly matching search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where author is the search term
            test = DataSource()

        """
        query = "SELECT * FROM bookbans WHERE author=%s"

        cursor = self.connection.cursor()
        cursor.execute(query, (search_term,))

        results = cursor.fetchall()
        return results

    def search_title_like(self, search_term):
        """Searches booksbans database for titles containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where title contains the search term
        """
        query = "SELECT * FROM bookbans WHERE title LIKE %s"
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
        query = "SELECT * FROM bookbans WHERE genre LIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, ("%" + search_term + "%",))

        results = cursor.fetchall()
        return results
    
    def search_author_like(self, search_term):
        """Searches booksbans database for authors containing search term
        Args:
            search_term (str): the string being searched for
        Returns:
            list of bans where author contains the search term
        """
        query = "SELECT * FROM bookbans WHERE author LIKE %s"
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



# if __name__ == "__main__":
#     my_ds = DataSource()
#     print(my_ds.search_title_like("Angel"))
