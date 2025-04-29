from datetime import datetime
from statistics import fmean


class Book:
    def __init__(
        self,
        title: str,
        authors: list[str],
        summary: str,
        cover_url: str,
        genres: list[str],
        isbn: str,
        publish_date: int,
        rating_histogram: list[int],
    ):
        self.title: str = title
        self.authors: list[str] = authors
        self.summary: str = summary
        self.cover_url: str = cover_url
        self.genres: list[str] = genres
        self.isbn: int = int(isbn)
        self.publish_year: int = datetime.fromtimestamp(publish_date / 1000).year
        self.rating: float = round(fmean([1, 2, 3, 4, 5], weights=rating_histogram), 1)

    def __str__(self) -> str:
        return f"{self.title} by {self.authors_to_string()} (ISBN: {self.isbn})"

    def authors_to_string(self) -> str:
        return ", ".join(self.authors)


def main() -> None:
    """Main function for informal testing."""
    book: Book = Book(
        "to kill a mockingbird",
        ["author a", "author b"],
        "fjaskdhflahsf",
        "url",
        [
            "fiction",
            "historical fiction",
        ],
        "12481841",
        84189471,
        [10, 0, 1, 10, 50],
    )
    print(book)


if __name__ == "__main__":
    main()
