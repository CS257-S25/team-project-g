'''
This file contains the unit tests for the Flask application.
'''
import unittest
from app import app

class TestApp(unittest.TestCase):
    '''
    This class tests the Flask application.
    '''
    def setUp(self):
        '''
        Arguments: None
        Return value: None
        This function sets up the test client for the Flask application.
        '''
        self.app = app.test_client()

    def test_homepage(self):
        '''
        Arguments: None
        Return value: None
        This function tests the homepage of the Flask application.
        '''

    def test_valid_states_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned states.
        '''
        response = self.app.get('/most-banned/states/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Florida: 6533Iowa: 3685Texas: 1964'
                      b'Pennsylvania: 664Wisconsin: 480',
                      response.data)

    def test_valid_titles_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned titles.
        '''
        response = self.app.get('/most-banned/titles/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Looking for Alaska: 135Nineteen Minutes: 126'
                      b'The Perks of Being a Wallflower: 118'
                      b'Sold: 116Thirteen Reasons Why: 112',
                      response.data)

    def test_valid_districts_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned districts.
        '''
        response = self.app.get('/most-banned/districts/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Escambia County Public Schools: 1787'
                      b'Clay County School District: 864'
                      b'Orange County Public Schools: 734'
                      b'North East Independent School District: 606'
                      b'Central York School District: 443',
                      response.data)

    def test_valid_authors_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned authors.
        '''
        response = self.app.get('/most-banned/authors/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ellen Hopkins: 791Sarah J. Maas: 657'
                      b'Jodi Picoult: 213John Green: 203Toni Morrison: 197',
                      response.data)

    def test_invalid_limit(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test is for invalid limit.
        '''
        response = self.app.get('/most-banned/states/five')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'400: Bad Request', response.data)

    def test_invalid_category(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test is for invalid category.
        '''
        response = self.app.get('/most-banned/notareal/5')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'400: Bad Request', response.data)

if __name__ == '__main__':
    unittest.main()
