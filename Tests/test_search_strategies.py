"""Module for testing Search Strategies"""

import unittest
from unittest.mock import patch

from ProductionCode.search_strategies import (
    ConcreteSearchStrategyAuthor,
    ConcreteSearchStrategyGenre,
    ConcreteSearchStrategyTitle,
    SearchContext,
    ConcreteSearchStrategyAll,
)

from Tests.mock_data import mock_search_section


class SearchContextTest(unittest.TestCase):
    """Tests for SearchContext class"""

    def setUp(self) -> None:
        self.concrete_search_strategy = ConcreteSearchStrategyTitle()
        self.search_context = SearchContext(self.concrete_search_strategy)

    @patch("ProductionCode.search_strategies.ConcreteSearchStrategyTitle.search")
    def test_search(self, mock_search):
        """Test for search method"""
        mock_search.return_value = [mock_search_section]
        self.assertEqual(self.search_context.search(""), [mock_search_section])


class ConcreteSearchStrategyAllTest(unittest.TestCase):
    """Tests for SearchStrategyAll class"""

    def setUp(self) -> None:
        search_strategy = ConcreteSearchStrategyAll()
        self.search_context = SearchContext(search_strategy)

    @patch(
        "ProductionCode.search_decorators.SearchConcreteDecoratorAuthor.search_author"
    )
    @patch("ProductionCode.search_decorators.SearchConcreteDecoratorGenre.search_genre")
    @patch("ProductionCode.search_decorators.SearchConcreteDecoratorTitle.search_title")
    @patch("ProductionCode.search_decorators.SearchConcreteDecoratorISBN.search_isbn")
    def test_search(
        self, mock_search_isbn, mock_search_title, mock_search_genre, mock_search_author
    ):
        """Tests for search method"""
        mock_search_isbn.return_value = mock_search_section
        mock_search_title.return_value = mock_search_section
        mock_search_genre.return_value = mock_search_section
        mock_search_author.return_value = mock_search_section

        results = self.search_context.search("")
        expected = [
            mock_search_section,
            mock_search_section,
            mock_search_section,
            mock_search_section,
        ]
        self.assertEqual(results, expected)


class ConcreteSearchStrategyTitleTest(unittest.TestCase):
    """Tests for SearchStrategyTitle class"""

    def setUp(self) -> None:
        search_strategy = ConcreteSearchStrategyTitle()
        self.search_context = SearchContext(search_strategy)

    @patch("ProductionCode.search_decorators.SearchConcreteDecoratorTitle.search_title")
    def test_search(self, mock_search_title):
        """Tests for search method"""
        mock_search_title.return_value = mock_search_section

        results = self.search_context.search("")
        expected = [
            mock_search_section,
        ]
        self.assertEqual(results, expected)


class ConcreteSearchStrategyAuthorTest(unittest.TestCase):
    """Tests for SearchStrategyAuthor class"""

    def setUp(self) -> None:
        search_strategy = ConcreteSearchStrategyAuthor()
        self.search_context = SearchContext(search_strategy)

    @patch(
        "ProductionCode.search_decorators.SearchConcreteDecoratorAuthor.search_author"
    )
    def test_search(self, mock_search_author):
        """Tests for search method"""
        mock_search_author.return_value = mock_search_section

        results = self.search_context.search("")
        expected = [
            mock_search_section,
        ]
        self.assertEqual(results, expected)


class ConcreteSearchStrategyGenreTest(unittest.TestCase):
    """Tests for SearchStrategyGenreclass"""

    def setUp(self) -> None:
        search_strategy = ConcreteSearchStrategyGenre()
        self.search_context = SearchContext(search_strategy)

    @patch("ProductionCode.search_decorators.SearchConcreteDecoratorGenre.search_genre")
    def test_search(self, mock_search_genre):
        """Tests for search method"""
        mock_search_genre.return_value = mock_search_section

        results = self.search_context.search("")
        expected = [
            mock_search_section,
        ]
        self.assertEqual(results, expected)
