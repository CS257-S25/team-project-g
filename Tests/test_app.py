"""
This file contains the unit tests for the Flask application.
"""

import unittest
from app import app


class TestApp(unittest.TestCase):
    """
    This class tests the Flask application.
    """

    def setUp(self):
        """
        Arguments: None
        Return value: None
        This function sets up the test client for the Flask application.
        """
        self.app = app.test_client()

    def test_homepage(self):
        """
        Arguments: None
        Return value: None
        This function tests the homepage of the Flask application.
        """
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)

        expected_strings = [
            b"The following addresses can be used to see information about banned books:",
            b'To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;".',
            b"&lt;field&gt; can be title, author, or genre",
            b"&lt;query&gt; is the search term",
            b"To see a list of categories with the most banned books, go to "
            b'"/most-banned/&lt;field&gt;/&lt;max_results&gt;".',
            b"&lt;field&gt; can be states, districts, authors, or titles",
            b"&lt;max_results&gt; is the number of results you want to display",
        ]

        for expected in expected_strings:
            self.assertIn(expected, response.data)

    def test_valid_states_route(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned states.
        """
        response = self.app.get("/most-banned/states/5")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Florida: 6533</br>Iowa: 3685</br>Texas: 1964</br>"
            b"Pennsylvania: 664</br>Wisconsin: 480",
            response.data,
        )

    def test_valid_titles_route(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned titles.
        """
        response = self.app.get("/most-banned/titles/5")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Looking for Alaska: 135</br>Nineteen Minutes: 126</br>"
            b"The Perks of Being a Wallflower: 118</br>"
            b"Sold: 116</br>Thirteen Reasons Why: 112",
            response.data,
        )

    def test_valid_districts_route(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned districts.
        """
        response = self.app.get("/most-banned/districts/5")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Escambia County Public Schools: 1787</br>"
            b"Clay County School District: 864</br>"
            b"Orange County Public Schools: 734</br>"
            b"North East Independent School District: 606</br>"
            b"Central York School District: 443",
            response.data,
        )

    def test_valid_authors_route(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned authors.
        """
        response = self.app.get("/most-banned/authors/5")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Ellen Hopkins: 791</br>Sarah J. Maas: 657</br>"
            b"Jodi Picoult: 213</br>John Green: 203</br>Toni Morrison: 197",
            response.data,
        )

    def test_invalid_max_results(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test is for invalid max_results.
        """
        response = self.app.get("/most-banned/states/five")
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"500: Bad Request", response.data)

    def test_invalid_category(self):
        """
        Arguments: None
        Return value: Return true if the test passes.
        This test is for invalid category.
        """
        response = self.app.get("/most-banned/notareal/5")
        self.assertEqual(response.status_code, 500)
        self.assertIn(b"500: Bad Request", response.data)


class TestAppSearch(unittest.TestCase):
    """
    Tests for search methods for Flask app
    """

    def setUp(self):
        """This function sets up the test client for the Flask application.
        Args:
            None
        Returns:
            None
        """
        self.app = app.test_client()

    def test_search_author(self):
        """Test for a valid author search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/author/Kristin Cast")
        self.assertEqual(
            b"Kalona's Fall by Kristin Cast, P.C. Cast (ISBN not found)</br>"
            b"Kisses from Hell by Francesca Lia Block, Kristin Cast, Alyson Noel"
            b", Richelle Mead, Kelley Armstrong (ISBN: 0061956961)",
            response.data,
        )

    def test_search_title(self):
        """Test for valid title search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/title/kaleidoscope")
        self.assertEqual(
            b"Kaleidoscope by Danielle Steel (ISBN: 0440236924)</br>"
            b"Kaleidoscope Song by Fox Benwell (ISBN: 1481477676)",
            response.data,
        )

    def test_search_genre(self):
        """Test for valid genre search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/genre/lgbt")
        self.assertEqual(
            b"Kapaemahu by Joe Wilson, Daniel Sousa, Hinaleimoana Wong-Kalu, Dean Hamer "
            b"(ISBN: 0593530063)</br>"
            b"Kaleidoscope Song by Fox Benwell (ISBN: 1481477676)</br>"
            b"Kate in Waiting by Becky Albertalli (ISBN: 0062643835)</br>"
            b"Keeping You a Secret by Julie Anne Peters (ISBN: 0316009857)</br>"
            b"King and the Dragonflies by Kacen Callender (ISBN: 1338129333)</br>"
            b"King of the Screwups by K.L. Going (ISBN: 0152062580)</br>"
            b"King of Scars by Leigh Bardugo (ISBN: 125014227X)</br>"
            b"Kingsbane by Claire Legrand (ISBN: 1492656666)</br>"
            b"Kings of B'more by R. Eric Thomas (ISBN: 0593326180)</br>"
            b"Kings, Queens, and In-Betweens by Tanya Boteju (ISBN: 1534430652)</br>"
            b"Kiss & Tell by Adib Khorram (ISBN: 0593325265)</br>"
            b"Kings Rising by C.S. Pacat (ISBN: 174348495X)</br>"
            b"Kiss Number 8 by Ellen T. Crenshaw, Colleen A.F. Venable (ISBN: 1250196930)</br>"
            b"Kissing Kate by Lauren Myracle (ISBN: 0142408697)",
            response.data,
        )

    def test_search_invalid_field(self):
        """Test for invalid field search
        Args:
            None
        Return:
            None
        """
        response = self.app.get("/search/bad-field/search")
        self.assertEqual(400, response.status_code)

class TestAppDetails(unittest.TestCase):
    """
    Tests for details methods for Flask app
    """
    def setUp(self):
        """This function sets up the test client for the Flask application.
        Args:
            None
        Returns:
            None
        """
        self.app = app.test_client()
        
    def test_valid_details_route(self):
        """Details for ISBN 1250142202 should include all the expected fields."""
        response = self.app.get("/details/1250142202")
        self.assertEqual(response.status_code, 200)

        data = response.data

        header = (
            b"Details for Killing Jesus: A History by "
            b"Martin Dugard, Bill O'Reilly (2017, ISBN: 1250142202)"
        )
        self.assertIn(header, data)

        summary = (
            b"Book details from Goodreads: Millions of readers have thrilled "
            b"to bestselling authors Bill O'Reilly and historian Martin Dugard's "
            b"Killing Kennedy and Killing Lincoln"
        )
        self.assertIn(summary, data)

        genres = (
            b"Genres: Historical, Christianity, Faith, Biography, Book Club, "
            b"Nonfiction, History, Religion, Christian, Audiobook"
        )
        self.assertIn(genres, data)

        self.assertIn(b"Average review: 4.0 stars", data)

        self.assertIn(
            b"Banned in Escambia County Public Schools, Florida in August 2023",
            data
        )

        self.assertIn(b"<br /><br />", data)
    
    def test_invalid_details_route(self):
        """An unknown ISBN should return a 400 with the correct error message."""
        response = self.app.get("/details/0000000000")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"No book with that ISBN found!", response.data)

if __name__ == "__main__":
    unittest.main()
