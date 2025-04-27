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
        self.title = title
        self.authors = authors
        self.summary = summary
        self.cover_url = cover_url
        self.genres = genres
        self.isbn = int(isbn)
        self.publish_year = datetime.fromtimestamp(publish_date/1000).year
        self.rating = round(fmean([1,2,3,4,5],weights=rating_histogram),1)
