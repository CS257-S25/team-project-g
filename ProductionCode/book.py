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
    ):
        self.title = title
        self.authors = authors
        self.summary = summary
        self.cover_url = cover_url
        self.genres = genres
        self.isbn = isbn
        self.publish_date = publish_date
        self.rating_histogram = rating_histogram
