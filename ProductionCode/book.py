"""Module containing a book class for representing data on a book"""


class Book:
    """Book class to represent book data"""

    def __init__(
        self,
        isbn: str,
        title: str,
        authors: list[str],
        details: dict,
    ):
        self.isbn: str = isbn
        self.title: str = title
        self.authors: list[str] = authors
        self.details = details

    def __str__(self) -> str:
        """Method for displaying basic book information
        Args: None
        Returns:
            string with information on title, authors, and isbn number
        """
        return f"{self.title} by {self.authors_to_string()} (ISBN: {self.isbn})"

    def authors_to_string(self) -> str:
        """Helper method for displaying author information"""
        return ", ".join(self.authors)

    def genres_to_string(self) -> str:
        """Helper method for displaying author information"""
        if self.details["genres"]:
            return ", ".join(self.details["genres"])
        return ""
