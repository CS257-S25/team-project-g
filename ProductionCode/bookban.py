from book import Book


class Bookban:
    def __init__(
        self,
        book: Book,
        state: str,
        district: str,
        ban_year: int,
        ban_month: int,
        ban_status: str,
        ban_origin: str,
    ) -> None:
        self.book: Book = book
        self.state: str = state
        self.district: str = district
        self.ban_year: int = ban_year
        self.ban_month: int = ban_month
        self.ban_status: str = ban_status
        self.ban_origin: str = ban_origin

    def __str__(self) -> str:
        return f"{self.book} banned in {self.district}, {self.state} as of {self.date_to_str}"

    def date_to_str(self) -> str:
        match self.ban_month:
            case 1:
                month = "January"
            case 2:
                month = "February"
            case 3:
                month = "March"
            case 4:
                month = "April"
            case 5:
                month = "May"
            case 6:
                month = "June"
            case 7:
                month = "July"
            case 8:
                month = "August"
            case 9:
                month = "September"
            case 10:
                month = "October"
            case 11:
                month = "November"
            case 12:
                month = "December"
            case _:
                month = "Unknown"
        return f"{month}, {self.ban_year}"

