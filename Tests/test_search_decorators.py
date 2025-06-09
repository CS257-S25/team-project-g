"""Module for testing search decorators"""

import unittest
from unittest.mock import MagicMock, patch
from ProductionCode.search_decorators import (
    SearchComponent,
    SearchConcreteComponent,
    SearchConcreteDecoratorAuthor,
    SearchConcreteDecoratorISBN,
    SearchConcreteDecoratorLimitResults,
    SearchConcreteDecoratorTitle,
    SearchDecorator,
)

from Tests.mock_data import mock_book


class SearchComponentTest(unittest.TestCase):
    """This class is for testing the SearchComponent interface"""

    def setUp(self) -> None:
        self.search_component = SearchComponent()

    def test_operation(self):
        """Test for operation method"""
        result = self.search_component.operation("")
        expected = []
        self.assertEqual(result, expected)


class SearchConcreteComponentTest(unittest.TestCase):
    """This class is for testing the SearchComponent Class"""

    def setUp(self) -> None:
        self.search_concrete_component = SearchConcreteComponent()

    def test_operation(self):
        """Test for operation method"""
        result = self.search_concrete_component.operation("")
        expected = []
        self.assertEqual(result, expected)


class SearchDecoratorTest(unittest.TestCase):
    """This class is for testing the SearchDecorator class"""

    def setUp(self) -> None:
        self.search_component = SearchComponent()
        self.search_decorator = SearchDecorator(self.search_component)

    def test_search_component(self):
        """Test for search_component method"""
        self.assertEqual(self.search_decorator.search_component, self.search_component)

    def test_operation(self):
        """Test for operation method"""
        result = self.search_decorator.operation("")
        expected = self.search_component.operation("")
        self.assertEqual(result, expected)


class SearchConcreteDecoratorAuthorTest(unittest.TestCase):
    """This class is for testing the SearchConcreteDecoratorAuthor class"""

    def setUp(self) -> None:
        self.search_concrete_component = SearchConcreteComponent()
        self.search_concrete_decorator = SearchConcreteDecoratorAuthor(
            self.search_concrete_component
        )

    @patch(
        "ProductionCode.search_decorators.SearchConcreteDecoratorAuthor.search_author"
    )
    def test_operation(self, mock_search_author):
        """Test for operation method"""
        mock_search_author.return_value = mock_book
        result = self.search_concrete_decorator.operation("")
        self.assertIn(mock_book, result)


class SearchConcreteDecoratorTitleTest(unittest.TestCase):
    """This class is for testing the SearchConcreteDecoratorTitle class"""

    def setUp(self) -> None:
        self.search_concrete_component = SearchConcreteComponent()
        self.search_concrete_decorator = SearchConcreteDecoratorTitle(
            self.search_concrete_component
        )

    @patch("ProductionCode.search_decorators.SearchConcreteDecoratorTitle.search_title")
    def test_operation(self, mock_search_title):
        """Test for operation method"""
        mock_search_title.return_value = mock_book
        result = self.search_concrete_decorator.operation("")
        self.assertIn(mock_book, result)


class SearchConcreteDecoratorISBNTest(unittest.TestCase):
    """This class is for testing the SearchConcreteDecoratorISBN class"""

    def setUp(self) -> None:
        self.search_concrete_component = SearchConcreteComponent()
        self.search_concrete_decorator = SearchConcreteDecoratorISBN(
            self.search_concrete_component
        )

        self.mock_conn = MagicMock()
        self.mock_cursor = self.mock_conn.cursor.return_value

    @patch("ProductionCode.search_decorators.SearchConcreteDecoratorISBN.search_isbn")
    def test_operation(self, mock_search_isbn):
        """Test for operation method"""
        mock_search_isbn.return_value = mock_book
        result = self.search_concrete_decorator.operation("")
        self.assertIn(mock_book, result)

    @patch("ProductionCode.datasource.DataSource.get_book_from_isbn")
    @patch("ProductionCode.datasource.psycopg2.connect")
    def test_search_isbn(self, mock_connect, mock_search_isbn):
        """Test for operation method"""
        mock_connect.return_value = self.mock_conn

        mock_search_isbn.return_value = None
        result = self.search_concrete_decorator.operation("")
        self.assertEqual(result[0].get_results(), [])


class SearchConcreteDecoratorLimitResultsTest(unittest.TestCase):
    """This class is for testing the SearchConcreteDecoratorLimitResults"""

    def setUp(self) -> None:
        self.search_concrete_component = SearchConcreteComponent()
        self.search_concrete_decorator_title = SearchConcreteDecoratorTitle(
            self.search_concrete_component
        )
        self.search_concrete_decorator = SearchConcreteDecoratorLimitResults(
            self.search_concrete_decorator_title
        )

        @patch(
            "ProductionCode.search_decorators.SearchConcreteDecoratorTitle.operation"
        )
        def test_operation(self, mock_search_title_operation):
            """Test for operation method"""
            mock_search_title_operation.return_value = [
                mock_book,
                mock_book,
                mock_book,
                mock_book,
                mock_book,
                mock_book,
            ]
            result = self.search_concrete_decorator.operation("")
            self.assertTrue(len(result[0].get_results()) == 5)
