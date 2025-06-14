"""Mock book and bookban objects for testing"""

from ProductionCode.book import Book
from ProductionCode.bookban import Bookban
from ProductionCode.search_section import SearchSection

mock_book = Book(
    isbn="440236924",
    title="Kaleidoscope",
    authors=["Danielle Steel"],
    details={
        "summary": "summary",
        "cover": "cover.jpg",
        "genres": ["Mystery", "Fantasy"],
        "publish_date": "2020-10-27",
        "rating": 3.9,
    },
)


mock_ban = Bookban(
    Book(
        isbn="440236924",
        title="Kaleidoscope",
        authors=["Danielle Steel"],
        details={
            "summary": "summary",
            "cover": "url.jpg",
            "genres": ["Mystery", "Fantasy"],
            "publish_date": "2020-10-27",
            "rating": 3.9,
        },
    ),
    location={
        "state": "Florida",
        "district": "Martin County Schools",
    },
    details={
        "ban_year": 2023,
        "ban_month": 3,
        "ban_status": "Banned from Libraries and Classrooms",
        "ban_origin": "Formal Challenge",
    },
)

mock_search_section = SearchSection("Title", "title", [mock_book, mock_book])
