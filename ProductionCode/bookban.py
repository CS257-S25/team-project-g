from book import Book


class Bookban:
    def __init__(
        self,
        book: Book,
        state: str,
        district: str,
        ban_date: str,  # should eventually change to unix time
        ban_status: str,
        ban_origin: str,
    ) -> None:
        self.book: Book = book
        self.state: str = state
        self.district: str = district
        self.ban_date: str = ban_date
        self.ban_status: str = ban_status
        self.ban_origin: str = ban_origin

    def __str__(self) -> str: 
        return f"{self.book} banned in {self.district}, {self.state} as of {self.ban_date}"