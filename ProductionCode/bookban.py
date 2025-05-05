from ProductionCode.book import Book


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
        return f"{self.book} banned in {self.district}, {self.state} as of {self.date_to_str()}"

    def date_to_str(self) -> str:
        # match self.ban_month:
        #     case 1:
        #         month = "January"
        #     case 2:
        #         month = "February"
        #     case 3:
        #         month = "March"
        #     case 4:
        #         month = "April"
        #     case 5:
        #         month = "May"
        #     case 6:
        #         month = "June"
        #     case 7:
        #         month = "July"
        #     case 8:
        #         month = "August"
        #     case 9:
        #         month = "September"
        #     case 10:
        #         month = "October"
        #     case 11:
        #         month = "November"
        #     case 12:
        #         month = "December"
        #     case _:
        #         month = "Unknown"
        return f"{self.ban_month}, {self.ban_year}"


def main():
    book = Book(
        isbn="440236924",
        title="Kaleidoscope",
        authors=["Danielle Steel"],
        summary="When a beautiful young Frenchwoman and a brilliant American actor meet in wartime Paris, their love begins like a fairy tale but ends in tragedy. Suddenly orphaned, their three children are cruelly separated. Megan, the baby, adopted by a family of comfortable means, becomes doctor in the rural Appalachia. Alexandra, raised in lavish wealth, marries a powerful man whose pride is his pedigree and who assumes that Alexandra is her parents' natural offspring. Neither of them has the remotest suspicion that she is adopted, or what turbulent tragedy lurks in her past. And Hilary, oldest of the Walker children, remembers them all, and the grief that tore them apart and cast them into separate lives. Feeling the loss throughout her life, and unable to find her sisters, she builds an extraordinary career and has no personal life. When John Chapman, lawyer and prestigious private investigator, is asked to find these three women, he wonders why. Their parents' only friend, he did nothing to keep them together  as children and has been haunted by remorse all his life. The investigator follows a trail that leads from chic New York to Boston slums, from elegant Parisian salons to the Appalachian hills, to the place where the three sisters face each other and one more final, devastating truth before they can move on.",
        cover="https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1173371736i/278102.jpg",
        genres=[
            "Adult Fiction",
            "Contemporary Romance",
            "Romance,Novels",
            "Contemporary",
            "Drama",
            "Adult",
            "Chick Lit",
            "Historical Fiction",
            "Fiction",
        ],
        publish_date="2000-10-28",
        rating=4.0,
    )
    bookban = Bookban(
        book=book,
        state="Florida",
        district="Martin County Schools",
        ban_year=2023,
        ban_month=3,
        ban_status="Banned from Libraries and Classrooms",
        ban_origin="Formal Challenge",
    )
    print("test")
    print(bookban)


if __name__ == "__main__":
    main()
