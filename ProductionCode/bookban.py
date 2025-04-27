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
        self.book = book
        self.state = state
        self.district = district
        self.ban_date = ban_date
        self.ban_status = ban_status
        self.origin = origin
