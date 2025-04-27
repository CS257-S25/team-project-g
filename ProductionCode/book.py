class Book:
    def __init__(
        self,
        title: str,
        authors: list[str],
        summary: str,
        cover_url: str,
        genres: list[str],
        isbn: int,
        publish_date: int,
        rating_histogram: float,
    ) -> None:
        self.title = title
        self.authors = authors
        self.summary = summary
        self.cover_url = cover_url
        self.genres = genres
        self.isbn = isbn
        self.publish_date = publish_date
        self.rating_histogram = rating_histogram

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
        12481841,
        84189471,
        3.5,
    )
    print(book)


if __name__ == "__main__":
    main()
