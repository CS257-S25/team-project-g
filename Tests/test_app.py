import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        pass

    def test_valid_states_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned states.
        '''
        response = self.app.get('/most-banned/states/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Florida: 6533Iowa: 3685Texas: 1964Pennsylvania: 664Wisconsin: 480', response.data)

    def test_valid_titles_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned titles.
        '''
        response = self.app.get('/most-banned/titles/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Looking for Alaska: 135Nineteen Minutes: 126The Perks of Being a Wallflower: 118Sold: 116Thirteen Reasons Why: 112', response.data)

    def test_valid_districts_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned districts.
        '''
        response = self.app.get('/most-banned/districts/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Escambia County Public Schools: 1787Clay County School District: 864Orange County Public Schools: 734North East Independent School District: 606Central York School District: 443', response.data)

    def test_valid_authors_route(self):
        '''
        Arguments: None
        Return value: Return true if the test passes.
        This test grabs the most banned authors.
        ''' 
        response = self.app.get('/most-banned/authors/5')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Ellen Hopkins: 791Sarah J. Maas: 657Jodi Picoult: 213John Green: 203Toni Morrison: 197', response.data)

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
