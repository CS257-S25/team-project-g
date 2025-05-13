"""Module containing a book class for representing data on a book"""

# from datetime import datetime
# from statistics import fmean
# from psycopg2 import DATETIME


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

    # def average_rating_histogram(self, rating_histogram):
    #     return round(fmean([1, 2, 3, 4, 5], weights=rating_histogram), 1)


# class BookDetails:
#     def __init__(
#         self,
#         summary: str,
#         cover: str,
#         genres: list[str],
#         publish_date,
#         rating: float,
#     ):
#         self.summary: str = summary
#         self.cover: str = cover
#         self.genres: list[str] = genres
#         self.publish_date = publish_date
#         self.rating: float = rating


# def main() -> None:
#     """Main function for informal testing."""
#     book: Book = Book(
#         "to kill a mockingbird",
#         ["author a", "author b"],
#         "fjaskdhflahsf",
#         "url",
#         [
#             "fiction",
#             "historical fiction",
#         ],
#         "12481841",
#         84189471,
#         [10, 0, 1, 10, 50],
#     )
#     print(book)
#
#
# if __name__ == "__main__":
#     main()
