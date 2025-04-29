from book import Book


class Bookban:
    def __init__(
        self,
        book: Book,
        state: str,
        district: str,
        ban_date: str,  # should eventually change to unix time
        ban_status: str,
        origin: str,
    ):
        self.book: Book = book
        self.state: str = state
        self.district: str = district
        self.ban_date: str = ban_date
        self.ban_status: str = ban_status
        self.origin: str = origin
