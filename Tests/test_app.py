from ..app import *
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_homepage(self):
        pass

if __name__ == '__main__':
    unittest.main()
