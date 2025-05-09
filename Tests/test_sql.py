"""This file contains the unit tests for the SQL queries."""

import unittest
from unittest.mock import MagicMock, patch
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


class TestSQLQueries(unittest.TestCase):
    """This class tests the SQL queries."""

    def setUp(self):
        """Create a mock postgres connection."""
        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value
        # self.ds = DataSource()

    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_book_search_title_killing(self, mock_connect):
        """Test search_title in a normal case."""
        expected = [
            (
                1250142202,
                "Killing Jesus: A History",
                {"Martin Dugard", "Bill O'Reilly"},
                "Millions of readers have thrilled to bestselling authors"
                "Bill O'Reilly and historian Martin Dugard's Killing Kennedy "
                "and Killing Lincoln , page-turning works of nonfiction that have changed"
                "the way we read history.The basis for the 2015 television film available "
                "on streaming.Now the iconic anchor of The O'Reilly Factor details the "
                "events leading up to the murder of the most influential man in Jesus "
                "of Nazareth. Nearly two thousand years after this beloved and "
                "controversial young revolutionary was brutally killed by Roman "
                "soldiers, more than 2.2 billion human beings attempt to follow his "
                "teachings and believe he is God. Killing Jesus will take readers "
                "inside Jesus's life, recounting the seismic political and historical "
                "events that made his death inevitable - and changed the world forever.",
                "https://images-na.ssl-images-amazon.com/images/S/compressed."
                "photo.goodreads.com/books/1479249078i/31949128.jpg",
                {
                    "Historical",
                    "Christianity",
                    "Faith",
                    "Biography",
                    "Book Club",
                    "Nonfiction",
                    "History",
                    "Religion",
                    "Christian",
                    "Audiobook",
                },
                "2017-3-14",
                4,
            )
        ]
        # link the mock connection
        mock_connect.return_value = self.mock_conn
        # # set what it should return
        self.mock_cursor.fetchall.return_value = expected
        # mock_con = mock_connect.return_value mock_cur = mock_con.cursor.return_value
        # mock_cur.fetch_all.return_value = expected

        result = DataSource().books_search_title("Killing Jesus")
        result = list(map(str, result))
        self.assertEqual(result, expected)
        # self.assertEqual(
        #     DataSource().books_search_title("Killing Jesus: "), str(response)
        # )

    # @patch("ProductionCode.datasource.psycopg2.connect")
    # def test_search_isbn(self, mock_connect):
    #     """Test search_isbn in a normal case."""
    #     response = (
    #         440236924,
    #         "Kaleidoscope",
    #         "When a beautiful young Frenchwoman and a brilliant "
    #         "American actor meet in wartime Paris, their love "
    #         "begins like a fairy tale but ends in tragedy. "
    #         "Suddenly orphaned, their three children are cruelly "
    #         "separated. Megan, the baby, adopted by a family of "
    #         "comfortable means, becomes doctor in the rural Appalachia. "
    #         "Alexandra, raised in lavish wealth, marries a powerful "
    #         "man whose pride is his pedigree and who assumes that "
    #         "Alexandra is her parents' natural offspring. Neither of "
    #         "them has the remotest suspicion that she is adopted, or "
    #         "what turbulent tragedy lurks in her past. And Hilary, oldest "
    #         "of the Walker children, remembers them all, and the grief "
    #         "that tore them apart and cast them into separate lives. "
    #         "Feeling the loss throughout her life, and unable to find "
    #         "her sisters, she builds an extraordinary career and has "
    #         "no personal life. When John Chapman, lawyer and prestigious "
    #         "private investigator, is asked to find these three women, "
    #         "he wonders why. Their parents' only friend, he did nothing "
    #         "to keep them together as children and has been haunted by "
    #         "remorse all his life. The investigator follows a trail that "
    #         "leads from chic New York to Boston slums, from elegant Parisian "
    #         "salons to the Appalachian hills, to the place where the three "
    #         "sisters face each other and one more final, devastating "
    #         "truth before they can move on.",
    #         "https://images-na.ssl-images-amazon.com/images/S"
    #         "/compressed.photo.goodreads.com/books/1173371736i/278102.jpg",
    #         {
    #             "Adult Fiction",
    #             "Contemporary Romance",
    #             "Romance",
    #             "Novels",
    #             "Contemporary",
    #             "Drama",
    #             "Adult",
    #             "Chick Lit",
    #             "Historical Fiction",
    #             "Fiction",
    #         },
    #         "2000-10-28",
    #         4,
    #     )
    #     mock_connect.return_value = self.mock_conn
    #     self.mock_cursor.fetchall.return_value = response
    #     self.assertEqual(self.ds.book_from_isbn(440236924), str(response))
    #
    # @patch("ProductionCode.datasource.psycopg2.connect")
    # def test_search_author(self, mock_connect):
    #     """Test a normal case for search_author."""
    #     response = (
    #         1952457106,
    #         "A Kingdom of Flesh and Fire",
    #         {"Jennifer L. Armentrout"},
    #         "A Betrayal…Everything Poppy has ever believed in is a lie, "
    #         "i ncluding the man she was falling in love with. Thrust "
    #         "among those who see her as a symbol of a monstrous kingdom, "
    #         "she barely knows wh o she is without the veil of the Maiden. "
    #         "But what she does know is that nothing is as dangerous "
    #         "to her as him. The Dark One. The Prin ce of Atlantia. "
    #         "He wants her to fight him, and that's one order she's "
    #         "more than happy to obey. He may have taken her, but he "
    #         "will never have her.A Choice...Casteel Da'Neer is known by "
    #         "many names and many faces. His lies are as seductive as his "
    #         "touch. His truths as s ensual as his bite. Poppy knows "
    #         "better than to trust him. He needs her alive, healthy, "
    #         "and whole to achieve his goals. But he's the o nly way "
    #         "for her to get what she wants—to find her brother Ian "
    #         "and see for herself if he has become a soulless Ascended. "
    #         "Working with Casteel instead of against him presents its "
    #         "own risks. He still tempts her with every breath, offering "
    #         "up all she's ever wanted. Cast eel has plans for her. Ones "
    #         "that could expose her to unimaginable pleasure and "
    #         "unfathomable pain. Plans that will force her to look "
    #         "beyond everything she thought she knew about herself—"
    #         "about him. Plans that could bind their lives together "
    #         "in unexpected ways that nei ther kingdom is prepared "
    #         "for. And she's far too reckless, too hungry, to "
    #         "resist the temptation.A Secret…But unrest has "
    #         "grown in Atlan tia as they await the return of "
    #         "their Prince. Whispers of war have become stronger, "
    #         "and Poppy is at the very heart of it all. The King "
    #         "wants to use her to send a message. The Descenters "
    #         "want her dead. The wolven are growing more unpredictable. "
    #         "And as her abilities t o feel pain and emotion begin to "
    #         "grow and strengthen, the Atlantians start to fear her. "
    #         "Dark secrets are at play, ones steeped in the blood-drenched "
    #         "sins of two kingdoms that would do anything to keep the truth "
    #         "hidden. But when the earth begins to shake, and the skies "
    #         "start to bleed, it may already be too late.",
    #         "https://images-na.ssl-images-amazon.com/images"
    #         "/S/compressed.photo.goodreads.com/books"
    #         "/1734440592i/54319549.jpg",
    #         {
    #             "Paranormal",
    #             "New Adult",
    #             "Fiction",
    #             "Romantasy",
    #             "Enemies To Lovers",
    #             "Fantasy",
    #             "Fantasy Romance",
    #             "Magic",
    #             "Audiobook",
    #             "Vampires",
    #         },
    #         "2020-9-1",
    #         4.3,
    #     )
    #     mock_connect.return_value = self.mock_conn
    #     self.mock_cursor.fetchone.return_value = response
    #     self.assertEqual(
    #         self.ds.books_search_author("Jennifer L. Armentrout"), str(response)
    #     )
    #
    # @patch("ProductionCode.datasource.psycopg2.connect")
    # def test_search_genre(self, mock_connect):
    #     """Test a normal case for search_genre."""
    #     response = (
    #         "1682632075",
    #         "King & Kayla and the Case of the Gold Ring",
    #         {"Dori Hillestad Butler", "Nancy Meyers"},
    #         "King &amp; Kayla are back on the case in this laugh-out-loud "
    #         "mystery from the Theodor Seuss Geisel Honor Award-winning series.King"
    #         ", Kayla, Mason, and Asia are playing in the snow. Later, Asia discovers "
    #         "her gold ring is missing. What happened to it?Analytical Kayla has a plan. "
    #         "Together the friends retrace their steps and thoroughly search the area. "
    #         "Sensitive King remembers the crow he saw outside. Crows like shiny things. "
    #         "Can King and Kayla put the pieces together and find the lost ring?With simple"
    #         ", straightforward language and great verbal and visual humor, the King &amp; "
    #         "Kayla series is perfect for newly independent readers. King and Kayla model "
    #         "excellent problem-solving skills, including working as a team, gathering "
    #         "facts, making lists, and evaluating evidence.",
    #         "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads."
    #         "com/books/1599572199i/54793419.jpg",
    #         {
    #             "Chapter Books",
    #             "Humor",
    #             "Fiction",
    #             "Friendship",
    #             "Dogs",
    #             "Animal Fiction",
    #             "Mystery",
    #             "Animals",
    #             "Childrens",
    #         },
    #         "2021-2-2",
    #         3.9,
    #     )
    #     mock_connect.return_value = self.mock_conn
    #     self.mock_cursor.fetchone.return_value = response
    #     self.assertEqual(self.ds.books_search_genre("Animal Fiction"), str(response))
    #
    # @patch("ProductionCode.datasource.psycopg2.connect")
    # def test_get_most_banned_authors(self, mock_connect):
    #     """Test get_most_banned_authors with a limit of 1."""
    #     response = ({"Sarah J. Maas"}, 52)
    #     mock_connect.return_value = self.mock_conn
    #     self.mock_cursor.fetchone.return_value = response
    #     self.assertEqual(self.ds.get_most_banned_authors(1), str(response))
    #
    # @patch("ProductionCode.datasource.psycopg2.connect")
    # def test_get_most_banned_districts(self, mock_connect):
    #     """Test get_most_banned_districts with a limit of 1."""
    #     response = ("Escambia County Public Schools", 23)
    #     mock_connect.return_value = self.mock_conn
    #     self.mock_cursor.fetchone.return_value = response
    #     self.assertEqual(self.ds.get_most_banned_districts(1), str(response))
    #
    # @patch("ProductionCode.datasource.psycopg2.connect")
    # def test_get_most_banned_states(self, mock_connect):
    #     """Test get_most_banned_states with a limit of 1."""
    #     response = ("Florida", 87)
    #     mock_connect.return_value = self.mock_conn
    #     self.mock_cursor.fetchone.return_value = response
    #     self.assertEqual(self.ds.get_most_banned_states(1), str(response))
    #
    # @patch("ProductionCode.datasource.psycopg2.connect")
    # def test_get_most_banned_titles(self, mock_connect):
    #     """Test get_most_banned_titles with a limit of 1."""
    #     response = ("Kingdom of Ash", 52)
    #     mock_connect.return_value = self.mock_conn
    #     self.mock_cursor.fetchone.return_value = response
    #     self.assertEqual(self.ds.get_most_banned_titles(1), str(response))


#
# class TestSQLHelperMethods(unittest.TestCase):
#     """This class tests the helper methods for SQL queries"""
#
#     def setUp(self):
#         """Setup method to create datasource"""
#         self.ds = DataSource()
#
#     def test_database_row_to_book(self):
#         """Converting database row to book object test"""
#         expected = Book(
#             isbn="440236924",
#             title="Kaleidoscope",
#             authors=["Danielle Steel"],
#             details={
#                 "summary": "summary",
#                 "cover": "url.jpg",
#                 "genres": ["Mystery", "Fantasy"],
#                 "publish_date": "2020-10-27",
#                 "rating": 3.9,
#             },
#         )
#
#         results = self.ds.database_row_to_book(
#             (
#                 "440236924",
#                 "Kaleidoscope",
#                 ["Danielle Steel"],
#                 "summary",
#                 "url.jpg",
#                 ["Mystery", "Fantasy"],
#                 "2020-10-27",
#                 3.9,
#             )
#         )
#
#         self.assertEqual(results, expected)
#
#     def test_database_row_list_to_book_list(self):
#         """Converting database row to book object test"""
#         expected = [
#             Book(
#                 isbn="440236924",
#                 title="Kaleidoscope",
#                 authors=["Danielle Steel"],
#                 details={
#                     "summary": "summary",
#                     "cover": "url.jpg",
#                     "genres": ["Mystery", "Fantasy"],
#                     "publish_date": "2020-10-27",
#                     "rating": 3.9,
#                 },
#             ),
#             Book(
#                 isbn="440236924",
#                 title="Kaleidoscope",
#                 authors=["Danielle Steel"],
#                 details={
#                     "summary": "summary",
#                     "cover": "url.jpg",
#                     "genres": ["Mystery", "Fantasy"],
#                     "publish_date": "2020-10-27",
#                     "rating": 3.9,
#                 },
#             ),
#         ]
#
#         results = self.ds.database_row_list_to_book_list(
#             [
#                 (
#                     "440236924",
#                     "Kaleidoscope",
#                     ["Danielle Steel"],
#                     "summary",
#                     "url.jpg",
#                     ["Mystery", "Fantasy"],
#                     "2020-10-27",
#                     3.9,
#                 ),
#                 (
#                     "440236924",
#                     "Kaleidoscope",
#                     ["Danielle Steel"],
#                     "summary",
#                     "url.jpg",
#                     ["Mystery", "Fantasy"],
#                     "2020-10-27",
#                     3.9,
#                 ),
#             ]
#         )
#
#         self.assertEqual(results, expected)
