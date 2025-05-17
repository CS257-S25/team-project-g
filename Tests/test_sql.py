"""This file contains the unit tests for the SQL queries."""

import psycopg2
import unittest
from unittest.mock import MagicMock, patch
from ProductionCode import datasource
from ProductionCode.datasource import DataSource

# books_search_title,
# book_from_isbn,
# books_search_author,
# books_search_genre,
# get_most_banned_authors,
# get_most_banned_districts,
# get_most_banned_states,
# get_most_banned_titles
# )
from ProductionCode.book import Book
from ProductionCode.bookban import Bookban
from ProductionCode.rank import Rank


# class TestSQLQueries(unittest.TestCase):
#     """This class tests the SQL queries."""
#
#     def setUp(self):
#         """Create a mock postgres connection."""
#         self.mock_conn = MagicMock()
#         self.mock_cursor = self.mock_conn.cursor.return_value
#         # self.ds = DataSource()
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_book_search_title_killing(self, mock_connect):
#         """Test search_title in a normal case."""
#         response = [
#             (
#                 1250142202,
#                 "Killing Jesus: A History",
#                 {"Martin Dugard", "Bill O'Reilly"},
#                 "Millions of readers have thrilled to bestselling authors"
#                 "Bill O'Reilly and historian Martin Dugard's Killing Kennedy "
#                 "and Killing Lincoln , page-turning works of nonfiction that have changed"
#                 "the way we read history.The basis for the 2015 television film available "
#                 "on streaming.Now the iconic anchor of The O'Reilly Factor details the "
#                 "events leading up to the murder of the most influential man in Jesus "
#                 "of Nazareth. Nearly two thousand years after this beloved and "
#                 "controversial young revolutionary was brutally killed by Roman "
#                 "soldiers, more than 2.2 billion human beings attempt to follow his "
#                 "teachings and believe he is God. Killing Jesus will take readers "
#                 "inside Jesus's life, recounting the seismic political and historical "
#                 "events that made his death inevitable - and changed the world forever.",
#                 "https://images-na.ssl-images-amazon.com/images/S/compressed."
#                 "photo.goodreads.com/books/1479249078i/31949128.jpg",
#                 {
#                     "Historical",
#                     "Christianity",
#                     "Faith",
#                     "Biography",
#                     "Book Club",
#                     "Nonfiction",
#                     "History",
#                     "Religion",
#                     "Christian",
#                     "Audiobook",
#                 },
#                 "2017-3-14",
#                 4,
#             )
#         ]
#
#         expected_result = [
#             "Killing Jesus: A History by Martin Dugard, Bill O'Reilly (ISBN: 1250142202)"
#         ]
#         # link the mock connection
#         mock_connect.return_value = self.mock_conn
#         # set what it should return
#         self.mock_cursor.fetchall.return_value = response
#         search_result = DataSource().books_search_title("Killing Jesus: ")
#         search_result = list(map(str, search_result))
#         self.assertEqual(search_result, expected_result)
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_search_isbn(self, mock_connect):
#         """Test search_isbn in a normal case."""
#         response = (
#             440236924,
#             "Kaleidoscope",
#             "When a beautiful young Frenchwoman and a brilliant "
#             "American actor meet in wartime Paris, their love "
#             "begins like a fairy tale but ends in tragedy. "
#             "Suddenly orphaned, their three children are cruelly "
#             "separated. Megan, the baby, adopted by a family of "
#             "comfortable means, becomes doctor in the rural Appalachia. "
#             "Alexandra, raised in lavish wealth, marries a powerful "
#             "man whose pride is his pedigree and who assumes that "
#             "Alexandra is her parents' natural offspring. Neither of "
#             "them has the remotest suspicion that she is adopted, or "
#             "what turbulent tragedy lurks in her past. And Hilary, oldest "
#             "of the Walker children, remembers them all, and the grief "
#             "that tore them apart and cast them into separate lives. "
#             "Feeling the loss throughout her life, and unable to find "
#             "her sisters, she builds an extraordinary career and has "
#             "no personal life. When John Chapman, lawyer and prestigious "
#             "private investigator, is asked to find these three women, "
#             "he wonders why. Their parents' only friend, he did nothing "
#             "to keep them together as children and has been haunted by "
#             "remorse all his life. The investigator follows a trail that "
#             "leads from chic New York to Boston slums, from elegant Parisian "
#             "salons to the Appalachian hills, to the place where the three "
#             "sisters face each other and one more final, devastating "
#             "truth before they can move on.",
#             "https://images-na.ssl-images-amazon.com/images/S"
#             "/compressed.photo.goodreads.com/books/1173371736i/278102.jpg",
#             {
#                 "Adult Fiction",
#                 "Contemporary Romance",
#                 "Romance",
#                 "Novels",
#                 "Contemporary",
#                 "Drama",
#                 "Adult",
#                 "Chick Lit",
#                 "Historical Fiction",
#                 "Fiction",
#             },
#             "2000-10-28",
#             4,
#         )
#         mock_connect.return_value = self.mock_conn
#         self.mock_cursor.fetchone.return_value = response
#         self.assertEqual(self.ds.book_from_isbn(440236924), str(response))
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_search_author(self, mock_connect):
#         """Test a normal case for search_author."""
#         response = (
#             1952457106,
#             "A Kingdom of Flesh and Fire",
#             {"Jennifer L. Armentrout"},
#             "A Betrayal…Everything Poppy has ever believed in is a lie, "
#             "i ncluding the man she was falling in love with. Thrust "
#             "among those who see her as a symbol of a monstrous kingdom, "
#             "she barely knows wh o she is without the veil of the Maiden. "
#             "But what she does know is that nothing is as dangerous "
#             "to her as him. The Dark One. The Prin ce of Atlantia. "
#             "He wants her to fight him, and that's one order she's "
#             "more than happy to obey. He may have taken her, but he "
#             "will never have her.A Choice...Casteel Da'Neer is known by "
#             "many names and many faces. His lies are as seductive as his "
#             "touch. His truths as s ensual as his bite. Poppy knows "
#             "better than to trust him. He needs her alive, healthy, "
#             "and whole to achieve his goals. But he's the o nly way "
#             "for her to get what she wants—to find her brother Ian "
#             "and see for herself if he has become a soulless Ascended. "
#             "Working with Casteel instead of against him presents its "
#             "own risks. He still tempts her with every breath, offering "
#             "up all she's ever wanted. Cast eel has plans for her. Ones "
#             "that could expose her to unimaginable pleasure and "
#             "unfathomable pain. Plans that will force her to look "
#             "beyond everything she thought she knew about herself—"
#             "about him. Plans that could bind their lives together "
#             "in unexpected ways that nei ther kingdom is prepared "
#             "for. And she's far too reckless, too hungry, to "
#             "resist the temptation.A Secret…But unrest has "
#             "grown in Atlan tia as they await the return of "
#             "their Prince. Whispers of war have become stronger, "
#             "and Poppy is at the very heart of it all. The King "
#             "wants to use her to send a message. The Descenters "
#             "want her dead. The wolven are growing more unpredictable. "
#             "And as her abilities t o feel pain and emotion begin to "
#             "grow and strengthen, the Atlantians start to fear her. "
#             "Dark secrets are at play, ones steeped in the blood-drenched "
#             "sins of two kingdoms that would do anything to keep the truth "
#             "hidden. But when the earth begins to shake, and the skies "
#             "start to bleed, it may already be too late.",
#             "https://images-na.ssl-images-amazon.com/images"
#             "/S/compressed.photo.goodreads.com/books"
#             "/1734440592i/54319549.jpg",
#             {
#                 "Paranormal",
#                 "New Adult",
#                 "Fiction",
#                 "Romantasy",
#                 "Enemies To Lovers",
#                 "Fantasy",
#                 "Fantasy Romance",
#                 "Magic",
#                 "Audiobook",
#                 "Vampires",
#             },
#             "2020-9-1",
#             4.3,
#         )
#         mock_connect.return_value = self.mock_conn
#         self.mock_cursor.fetchone.return_value = response
#         self.assertEqual(
#             self.ds.books_search_author("Jennifer L. Armentrout"), str(response)
#         )
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_search_genre(self, mock_connect):
#         """Test a normal case for search_genre."""
#         response = (
#             "1682632075",
#             "King & Kayla and the Case of the Gold Ring",
#             {"Dori Hillestad Butler", "Nancy Meyers"},
#             "King &amp; Kayla are back on the case in this laugh-out-loud "
#             "mystery from the Theodor Seuss Geisel Honor Award-winning series.King"
#             ", Kayla, Mason, and Asia are playing in the snow. Later, Asia discovers "
#             "her gold ring is missing. What happened to it?Analytical Kayla has a plan. "
#             "Together the friends retrace their steps and thoroughly search the area. "
#             "Sensitive King remembers the crow he saw outside. Crows like shiny things. "
#             "Can King and Kayla put the pieces together and find the lost ring?With simple"
#             ", straightforward language and great verbal and visual humor, the King &amp; "
#             "Kayla series is perfect for newly independent readers. King and Kayla model "
#             "excellent problem-solving skills, including working as a team, gathering "
#             "facts, making lists, and evaluating evidence.",
#             "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads."
#             "com/books/1599572199i/54793419.jpg",
#             {
#                 "Chapter Books",
#                 "Humor",
#                 "Fiction",
#                 "Friendship",
#                 "Dogs",
#                 "Animal Fiction",
#                 "Mystery",
#                 "Animals",
#                 "Childrens",
#             },
#             "2021-2-2",
#             3.9,
#         )
#         mock_connect.return_value = self.mock_conn
#         self.mock_cursor.fetchone.return_value = response
#         self.assertEqual(self.ds.books_search_genre("Animal Fiction"), str(response))
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_get_most_banned_authors(self, mock_connect):
#         """Test get_most_banned_authors with a limit of 1."""
#         response = ({"Sarah J. Maas"}, 52)
#         mock_connect.return_value = self.mock_conn
#         self.mock_cursor.fetchone.return_value = response
#         self.assertEqual(self.ds.get_most_banned_authors(1), str(response))
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_get_most_banned_districts(self, mock_connect):
#         """Test get_most_banned_districts with a limit of 1."""
#         response = ("Escambia County Public Schools", 23)
#         mock_connect.return_value = self.mock_conn
#         self.mock_cursor.fetchone.return_value = response
#         self.assertEqual(self.ds.get_most_banned_districts(1), str(response))
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_get_most_banned_states(self, mock_connect):
#         """Test get_most_banned_states with a limit of 1."""
#         response = ("Florida", 87)
#         mock_connect.return_value = self.mock_conn
#         self.mock_cursor.fetchone.return_value = response
#         self.assertEqual(self.ds.get_most_banned_states(1), str(response))
#
#     @patch("ProductionCode.datasource.psycopg2.connect")
#     def test_get_most_banned_titles(self, mock_connect):
#         """Test get_most_banned_titles with a limit of 1."""
#         response = ("Kingdom of Ash", 52)
#         mock_connect.return_value = self.mock_conn
#         self.mock_cursor.fetchone.return_value = response
#         self.assertEqual(self.ds.get_most_banned_titles(1), str(response))
#
#     # @patch("ProductionCode.datasource.psycopg2.connect")
#     # def test_search_isbn(self, mock_connect):
#     #     """Test search_isbn in a normal case."""
#     #     response = (
#     #         440236924,
#     #         "Kaleidoscope",
#     #         "When a beautiful young Frenchwoman and a brilliant "
#     #         "American actor meet in wartime Paris, their love "
#     #         "begins like a fairy tale but ends in tragedy. "
#     #         "Suddenly orphaned, their three children are cruelly "
#     #         "separated. Megan, the baby, adopted by a family of "
#     #         "comfortable means, becomes doctor in the rural Appalachia. "
#     #         "Alexandra, raised in lavish wealth, marries a powerful "
#     #         "man whose pride is his pedigree and who assumes that "
#     #         "Alexandra is her parents' natural offspring. Neither of "
#     #         "them has the remotest suspicion that she is adopted, or "
#     #         "what turbulent tragedy lurks in her past. And Hilary, oldest "
#     #         "of the Walker children, remembers them all, and the grief "
#     #         "that tore them apart and cast them into separate lives. "
#     #         "Feeling the loss throughout her life, and unable to find "
#     #         "her sisters, she builds an extraordinary career and has "
#     #         "no personal life. When John Chapman, lawyer and prestigious "
#     #         "private investigator, is asked to find these three women, "
#     #         "he wonders why. Their parents' only friend, he did nothing "
#     #         "to keep them together as children and has been haunted by "
#     #         "remorse all his life. The investigator follows a trail that "
#     #         "leads from chic New York to Boston slums, from elegant Parisian "
#     #         "salons to the Appalachian hills, to the place where the three "
#     #         "sisters face each other and one more final, devastating "
#     #         "truth before they can move on.",
#     #         "https://images-na.ssl-images-amazon.com/images/S"
#     #         "/compressed.photo.goodreads.com/books/1173371736i/278102.jpg",
#     #         {
#     #             "Adult Fiction",
#     #             "Contemporary Romance",
#     #             "Romance",
#     #             "Novels",
#     #             "Contemporary",
#     #             "Drama",
#     #             "Adult",
#     #             "Chick Lit",
#     #             "Historical Fiction",
#     #             "Fiction",
#     #         },
#     #         "2000-10-28",
#     #         4,
#     #     )
#     #     mock_connect.return_value = self.mock_conn
#     #     self.mock_cursor.fetchall.return_value = response
#     #     self.assertEqual(self.ds.book_from_isbn(440236924), str(response))
#     #
#     # @patch("ProductionCode.datasource.psycopg2.connect")
#     # def test_search_author(self, mock_connect):
#     #     """Test a normal case for search_author."""
#     #     response = (
#     #         1952457106,
#     #         "A Kingdom of Flesh and Fire",
#     #         {"Jennifer L. Armentrout"},
#     #         "A Betrayal…Everything Poppy has ever believed in is a lie, "
#     #         "i ncluding the man she was falling in love with. Thrust "
#     #         "among those who see her as a symbol of a monstrous kingdom, "
#     #         "she barely knows wh o she is without the veil of the Maiden. "
#     #         "But what she does know is that nothing is as dangerous "
#     #         "to her as him. The Dark One. The Prin ce of Atlantia. "
#     #         "He wants her to fight him, and that's one order she's "
#     #         "more than happy to obey. He may have taken her, but he "
#     #         "will never have her.A Choice...Casteel Da'Neer is known by "
#     #         "many names and many faces. His lies are as seductive as his "
#     #         "touch. His truths as s ensual as his bite. Poppy knows "
#     #         "better than to trust him. He needs her alive, healthy, "
#     #         "and whole to achieve his goals. But he's the o nly way "
#     #         "for her to get what she wants—to find her brother Ian "
#     #         "and see for herself if he has become a soulless Ascended. "
#     #         "Working with Casteel instead of against him presents its "
#     #         "own risks. He still tempts her with every breath, offering "
#     #         "up all she's ever wanted. Cast eel has plans for her. Ones "
#     #         "that could expose her to unimaginable pleasure and "
#     #         "unfathomable pain. Plans that will force her to look "
#     #         "beyond everything she thought she knew about herself—"
#     #         "about him. Plans that could bind their lives together "
#     #         "in unexpected ways that nei ther kingdom is prepared "
#     #         "for. And she's far too reckless, too hungry, to "
#     #         "resist the temptation.A Secret…But unrest has "
#     #         "grown in Atlan tia as they await the return of "
#     #         "their Prince. Whispers of war have become stronger, "
#     #         "and Poppy is at the very heart of it all. The King "
#     #         "wants to use her to send a message. The Descenters "
#     #         "want her dead. The wolven are growing more unpredictable. "
#     #         "And as her abilities t o feel pain and emotion begin to "
#     #         "grow and strengthen, the Atlantians start to fear her. "
#     #         "Dark secrets are at play, ones steeped in the blood-drenched "
#     #         "sins of two kingdoms that would do anything to keep the truth "
#     #         "hidden. But when the earth begins to shake, and the skies "
#     #         "start to bleed, it may already be too late.",
#     #         "https://images-na.ssl-images-amazon.com/images"
#     #         "/S/compressed.photo.goodreads.com/books"
#     #         "/1734440592i/54319549.jpg",
#     #         {
#     #             "Paranormal",
#     #             "New Adult",
#     #             "Fiction",
#     #             "Romantasy",
#     #             "Enemies To Lovers",
#     #             "Fantasy",
#     #             "Fantasy Romance",
#     #             "Magic",
#     #             "Audiobook",
#     #             "Vampires",
#     #         },
#     #         "2020-9-1",
#     #         4.3,
#     #     )
#     #     mock_connect.return_value = self.mock_conn
#     #     self.mock_cursor.fetchone.return_value = response
#     #     self.assertEqual(
#     #         self.ds.books_search_author("Jennifer L. Armentrout"), str(response)
#     #     )
#     #
#     # @patch("ProductionCode.datasource.psycopg2.connect")
#     # def test_search_genre(self, mock_connect):
#     #     """Test a normal case for search_genre."""
#     #     response = (
#     #         "1682632075",
#     #         "King & Kayla and the Case of the Gold Ring",
#     #         {"Dori Hillestad Butler", "Nancy Meyers"},
#     #         "King &amp; Kayla are back on the case in this laugh-out-loud "
#     #         "mystery from the Theodor Seuss Geisel Honor Award-winning series.King"
#     #         ", Kayla, Mason, and Asia are playing in the snow. Later, Asia discovers "
#     #         "her gold ring is missing. What happened to it?Analytical Kayla has a plan. "
#     #         "Together the friends retrace their steps and thoroughly search the area. "
#     #         "Sensitive King remembers the crow he saw outside. Crows like shiny things. "
#     #         "Can King and Kayla put the pieces together and find the lost ring?With simple"
#     #         ", straightforward language and great verbal and visual humor, the King &amp; "
#     #         "Kayla series is perfect for newly independent readers. King and Kayla model "
#     #         "excellent problem-solving skills, including working as a team, gathering "
#     #         "facts, making lists, and evaluating evidence.",
#     #         "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads."
#     #         "com/books/1599572199i/54793419.jpg",
#     #         {
#     #             "Chapter Books",
#     #             "Humor",
#     #             "Fiction",
#     #             "Friendship",
#     #             "Dogs",
#     #             "Animal Fiction",
#     #             "Mystery",
#     #             "Animals",
#     #             "Childrens",
#     #         },
#     #         "2021-2-2",
#     #         3.9,
#     #     )
#     #     mock_connect.return_value = self.mock_conn
#     #     self.mock_cursor.fetchone.return_value = response
#     #     self.assertEqual(self.ds.books_search_genre("Animal Fiction"), str(response))
#     #
#     # @patch("ProductionCode.datasource.psycopg2.connect")
#     # def test_get_most_banned_authors(self, mock_connect):
#     #     """Test get_most_banned_authors with a limit of 1."""
#     #     response = ({"Sarah J. Maas"}, 52)
#     #     mock_connect.return_value = self.mock_conn
#     #     self.mock_cursor.fetchone.return_value = response
#     #     self.assertEqual(self.ds.get_most_banned_authors(1), str(response))
#     #
#     # @patch("ProductionCode.datasource.psycopg2.connect")
#     # def test_get_most_banned_districts(self, mock_connect):
#     #     """Test get_most_banned_districts with a limit of 1."""
#     #     response = ("Escambia County Public Schools", 23)
#     #     mock_connect.return_value = self.mock_conn
#     #     self.mock_cursor.fetchone.return_value = response
#     #     self.assertEqual(self.ds.get_most_banned_districts(1), str(response))
#     #
#     # @patch("ProductionCode.datasource.psycopg2.connect")
#     # def test_get_most_banned_states(self, mock_connect):
#     #     """Test get_most_banned_states with a limit of 1."""
#     #     response = ("Florida", 87)
#     #     mock_connect.return_value = self.mock_conn
#     #     self.mock_cursor.fetchone.return_value = response
#     #     self.assertEqual(self.ds.get_most_banned_states(1), str(response))
#     #
#     # @patch("ProductionCode.datasource.psycopg2.connect")
#     # def test_get_most_banned_titles(self, mock_connect):
#     #     """Test get_most_banned_titles with a limit of 1."""
#     #     response = ("Kingdom of Ash", 52)
#     #     mock_connect.return_value = self.mock_conn
#     #     self.mock_cursor.fetchone.return_value = response
#     #     self.assertEqual(self.ds.get_most_banned_titles(1), str(response))
class TestSQLSearchMethods(unittest.TestCase):
    """This class tests search methods for SQL queries"""

    def setUp(self):
        """Create a mock prostgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_title(self, mock_connect):
        """Tests search title method for the books database"""
        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = [
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        ]

        expected = [
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
        ]

        self.mock_cursor.fetchall.return_value = response

        results = ds.books_search_title("Kaleidoscope")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_author(self, mock_connect):
        """Tests search author method for books database"""
        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = [
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        ]

        expected = [
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
        ]

        self.mock_cursor.fetchall.return_value = response

        results = ds.books_search_author("Danielle Steel")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_genre(self, mock_connect):
        """Tests search genre method for books database"""

        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = [
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        ]

        expected = [
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
        ]

        self.mock_cursor.fetchall.return_value = response

        results = ds.books_search_genre("Mystery")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))


class TestSQLFromISBNMethods(unittest.TestCase):
    """This class tests methods from isbn for SQL queries"""

    def setUp(self):
        """Create a mock postgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_book_from_isbn(self, mock_connect):
        """Tests search book by isbn method for book database"""
        mock_connect.return_value = self.mock_conn

        ds = DataSource()

        response = (
            "440236924",
            "Kaleidoscope",
            ["Danielle Steel"],
            "summary",
            "url.jpg",
            ["Mystery", "Fantasy"],
            "2020-10-27",
            3.9,
        )

        expected = Book(
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
        )

        self.mock_cursor.fetchone.return_value = response

        results = ds.book_from_isbn("440236924")

        self.assertEqual(str(results), str(expected))

    @patch("ProductionCode.datasource.DataSource.database_row_list_to_bookban_list")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_bans_from_isbn(self, mock_connect, mock_database_row_list_to_bookban_list):
        """Tests search book bans by isbn method for bookbans database"""
        mock_connect.return_value = self.mock_conn

        mock_database_row_list_to_bookban_list.return_value = [
            Bookban(
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
                state="Florida",
                district="Martin County Schools",
                ban_year=2023,
                ban_month=3,
                ban_status="Banned from Libraries and Classrooms",
                ban_origin="Formal Challenge",
            )
        ]

        ds = DataSource()

        response = [
            (
                "440236924",
                "Florida",
                "Martin County Schools",
                2023,
                3,
                "Banned from Libraries and Classrooms",
                "Formal Challenge",
            )
        ]

        expected = [
            Bookban(
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
                state="Florida",
                district="Martin County Schools",
                ban_year=2023,
                ban_month=3,
                ban_status="Banned from Libraries and Classrooms",
                ban_origin="Formal Challenge",
            )
        ]
        self.mock_cursor.fetchall.return_value = response

        results = ds.bans_from_isbn("440236924")

        self.assertEqual(list(map(str, results)), list(map(str, expected)))


class TestSQLHelperMethods(unittest.TestCase):
    """This class tests the helper methods for SQL queries"""

    def setUp(self):
        """Create a mock postgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_to_book(self, _mock_connect):
        """Converting database row to book object test"""

        ds = DataSource()

        expected = Book(
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
        )

        results = ds.database_row_to_book(
            (
                "440236924",
                "Kaleidoscope",
                ["Danielle Steel"],
                "summary",
                "url.jpg",
                ["Mystery", "Fantasy"],
                "2020-10-27",
                3.9,
            )
        )

        self.assertEqual(str(results), str(expected))

    @patch("ProductionCode.datasource.DataSource.database_row_to_book")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_list_to_book_list(
        self, mock_connect, mock_database_row_to_book
    ):
        """Converting database row to book object list test"""
        mock_connect.return_value = self.mock_conn

        mock_database_row_to_book.return_value = Book(
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
        )

        ds = DataSource()

        expected = [
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
        ]

        results = ds.database_row_list_to_book_list(
            [
                (
                    "440236924",
                    "Kaleidoscope",
                    ["Danielle Steel"],
                    "summary",
                    "url.jpg",
                    ["Mystery", "Fantasy"],
                    "2020-10-27",
                    3.9,
                ),
                (
                    "440236924",
                    "Kaleidoscope",
                    ["Danielle Steel"],
                    "summary",
                    "url.jpg",
                    ["Mystery", "Fantasy"],
                    "2020-10-27",
                    3.9,
                ),
            ]
        )

        self.assertEqual(list(map(str, results)), list(map(str, expected)))

    @patch("ProductionCode.datasource.DataSource.book_from_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_to_bookban(self, mock_connect, mock_book_from_isbn):
        """Test for helper method converting database row to bookban"""
        mock_connect.return_value = self.mock_conn

        mock_book_from_isbn.return_value = Book(
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
        )

        ds = DataSource()

        expected = (
            "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
            " banned in Martin County Schools, Florida as of 3, 2023"
        )

        result = ds.database_row_to_bookban(
            (
                "440236924",
                "Florida",
                "Martin County Schools",
                2023,
                3,
                "Banned from Libraries and Classrooms",
                "Formal Challenge",
            )
        )

        self.assertEqual(str(result), expected)

    @patch("ProductionCode.datasource.DataSource.database_row_to_bookban")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_list_to_bookban_list(
        self, mock_connect, mock_database_row_to_bookban
    ):
        """Test for helper method converting database row to bookban"""
        mock_connect.return_value = self.mock_conn

        mock_database_row_to_bookban.return_value = Bookban(
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
            state="Florida",
            district="Martin County Schools",
            ban_year=2023,
            ban_month=3,
            ban_status="Banned from Libraries and Classrooms",
            ban_origin="Formal Challenge",
        )

        ds = DataSource()

        expected = [
            "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
            " banned in Martin County Schools, Florida as of 3, 2023",
            "Kaleidoscope by Danielle Steel (ISBN: 440236924)"
            " banned in Martin County Schools, Florida as of 3, 2023",
        ]

        result = ds.database_row_list_to_bookban_list(
            [
                (
                    "440236924",
                    "Florida",
                    "Martin County Schools",
                    2023,
                    3,
                    "Banned from Libraries and Classrooms",
                    "Formal Challenge",
                ),
                (
                    "440236924",
                    "Florida",
                    "Martin County Schools",
                    2023,
                    3,
                    "Banned from Libraries and Classrooms",
                    "Formal Challenge",
                ),
            ]
        )

        self.assertEqual(list(map(str, result)), expected)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_to_rank(self, _mock_connect):
        """Converting database row to rank object test"""
        ds = DataSource()

        expected = Rank("Florida", 50)

        result = ds.database_row_to_rank(("Florida", 50))

        self.assertEqual(str(expected), str(result))

    @patch("ProductionCode.datasource.DataSource.database_row_to_rank")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_database_row_list_to_rank_list(
        self, mock_connect, mock_database_row_to_rank
    ):
        """Converting database row list to rank object list test"""
        mock_connect.return_value = self.mock_conn
        mock_database_row_to_rank.return_value = Rank("Florida", 50)

        ds = DataSource()

        expected = [Rank("Florida", 50), Rank("Florida", 50)]

        result = ds.database_row_list_to_rank_list([("Florida", 50), ("Florida", 50)])

        self.assertEqual(list(map(str, result)), list(map(str, expected)))


class TestSQLMostBannedMethods(unittest.TestCase):
    def setUp(self):
        """Create a mock prostgres connection"""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_authors(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [(
            ["Sarah J. Maas"],
            52
        )]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_authors(1)
        self.assertEqual(list(map(str, results)), list(map(str, response)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_districts(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [(
            "Escambia County Public Schools",
            23
        )]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_districts(1)
        self.assertEqual(list(map(str, results)), list(map(str, response)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [(
            "Florida",
            87
        )]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_states(1)
        self.assertEqual(list(map(str, results)), list(map(str, response)))

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_titles(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [(
            "Kingdom of Ash",
            52
        )]
        self.mock_cursor.fetchall.return_value = response
        results = ds.get_most_banned_titles(1)
        self.assertEqual(list(map(str, results)), list(map(str, response)))

    @patch("ProductionCode.datasource.DataSource.book_from_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_books(self, mock_connect, mock_book_from_isbn):
        """Test get_most_banned_books with a limit of 1."""
        mock_connect.return_value = self.mock_conn
        ds = DataSource()
        response = [("1639731067", 52)]
        self.mock_cursor.fetchall.return_value = response
        expected_str = "Kingdom of Ash by Sarah J. Maas (ISBN: 1639731067)"
        mock_book_from_isbn.return_value = expected_str
        results = ds.get_most_banned_books(1)
        self.assertEqual(list(map(str, results)), [expected_str])

class TestSQLExceptionBranches(unittest.TestCase):
    def setUp(self):
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_book_from_isbn_error(self, mock_connect):
        """If the SELECT fails, we sys.exit() in book_from_isbn."""
        mock_connect.return_value = self.mock_conn
        # make cursor.execute raise
        self.mock_cursor.execute.side_effect = psycopg2.Error("boom")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.book_from_isbn("12345")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_title_error(self, mock_connect):
        """Trigger the except-clause in books_search_title."""
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("oh no")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.books_search_title("anything")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_author_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("fail")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.books_search_author("someone")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_books_search_genre_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("oops")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.books_search_genre("fantasy")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_bans_from_isbn_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("nope")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.bans_from_isbn("440236924")

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_author_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_authors(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_districts_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_districts(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_states_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_states(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_titles_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_titles(1)

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_get_most_banned_books_error(self, mock_connect):
        mock_connect.return_value = self.mock_conn
        self.mock_cursor.execute.side_effect = psycopg2.Error("err")
        ds = DataSource()
        with self.assertRaises(SystemExit):
            ds.get_most_banned_books(1)