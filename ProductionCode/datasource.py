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
        cursor.execute(query, ("%" + search_term + "%",))

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


# if __name__ == "__main__":
#     my_ds = DataSource()
#     print(my_ds.search_title_like("Angel"))
