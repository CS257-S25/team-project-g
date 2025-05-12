import unittest

from ProductionCode.book import Book, BookDetails
from ProductionCode.bookban import Bookban


class TestBookban(unittest.TestCase):
    """Tests for Book class"""

    def setUp(self):
        book = Book(
            isbn="440236924",
            title="Kaleidoscope",
            authors=["Danielle Steel"],
            details={
                "summary": "When a beautiful young Frenchwoman and a brilliant American actor meet in wartime Paris, their love begins like a fairy tale but ends in tragedy. Suddenly orphaned, their three children are cruelly separated. Megan, the baby, adopted by a family of comfortable means, becomes doctor in the rural Appalachia. Alexandra, raised in lavish wealth, marries a powerful man whose pride is his pedigree and who assumes that Alexandra is her parents' natural offspring. Neither of them has the remotest suspicion that she is adopted, or what turbulent tragedy lurks in her past. And Hilary, oldest of the Walker children, remembers them all, and the grief that tore them apart and cast them into separate lives. Feeling the loss throughout her life, and unable to find her sisters, she builds an extraordinary career and has no personal life. When John Chapman, lawyer and prestigious private investigator, is asked to find these three women, he wonders why. Their parents' only friend, he did nothing to keep them together  as children and has been haunted by remorse all his life. The investigator follows a trail that leads from chic New York to Boston slums, from elegant Parisian salons to the Appalachian hills, to the place where the three sisters face each other and one more final, devastating truth before they can move on.",
                "cover": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1173371736i/278102.jpg",
                "genres": [
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
                "publish_date": "2000-10-28",
                "rating": 4.0,
            },
        )

        self.bookban = Bookban(
            book=book,
            state="Florida",
            district="Martin County Schools",
            ban_year=2023,
            ban_month=3,
            ban_status="Banned from Libraries and Classrooms",
            ban_origin="Formal Challenge",
        )

    def test_string(self):
        """Tests __str__ method"""
        self.assertEqual(
            str(self.bookban),
            "Kaleidoscope by Danielle Steel (ISBN: 440236924) "
            "banned in Martin County Schools, Florida as of 3, 2023",
        )

    def test_date_to_str(self):
        self.assertEqual(self.bookban.date_to_str(), "3, 2023")
