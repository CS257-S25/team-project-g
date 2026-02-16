"""Module containing a bookban class for representing data on a bookban"""

from ProductionCode.book import Book


class Bookban:
    """Bookban class to represent bookban data"""

    def __init__(self, book: Book, location, details) -> None:
        self.book: Book = book
        self.location = location
        self.details = details

    def __str__(self) -> str:
        """Method for displaying basic bookban information
        Args: None
        Returns:
            string with information on book, location, and date
        """
        return (
            f"{self.book} banned in {self.location['district']}, {self.location['state']}"
            f" as of {self.date_to_str()}"
        )

    def date_to_str(self) -> str:
        """Helper method for printing date"""
        return f"{self.details['ban_month']}, {self.details['ban_year']}"
