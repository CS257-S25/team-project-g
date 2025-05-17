"""Module containing a bookban class for representing data on a bookban"""

# from datetime import datetime

from ProductionCode.book import Book


class Bookban:
    """Bookban class to represent bookban data"""

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
        """Method for displaying basic bookban information
        Args: None
        Returns:
            string with information on book, location, and date
        """
        return f"{self.book} banned in {self.district}, {self.state} as of {self.date_to_str()}"

    def date_to_str(self) -> str:
        """Helper method for printing date"""
        return f"{self.ban_month}, {self.ban_year}"


# def main():
#     book = Book(
#         isbn="440236924",
#         title="Kaleidoscope",
#         authors=["Danielle Steel"],
#         summary="summary",
#         cover="cover.jpg",
#         genres=[
#             "Adult Fiction",
#             "Contemporary Romance",
#             "Romance,Novels",
#             "Contemporary",
#             "Drama",
#             "Adult",
#             "Chick Lit",
#             "Historical Fiction",
#             "Fiction",
#         ],
#         publish_date="2000-10-28",
#         rating=4.0,
#     )
#     bookban = Bookban(
#         book=book,
#         state="Florida",
#         district="Martin County Schools",
#         ban_year=2023,
#         ban_month=3,
#         ban_status="Banned from Libraries and Classrooms",
#         ban_origin="Formal Challenge",
#     )
#     print("test")
#     print(bookban)
#
#
# if __name__ == "__main__":
#     main()
