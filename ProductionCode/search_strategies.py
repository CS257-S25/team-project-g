"""Module for Search Strategies"""

from abc import ABC, abstractmethod
from ProductionCode.search_decorators import SearchConcreteDecoratorGenre, SearchSection
from ProductionCode.search_decorators import (
    SearchConcreteComponent,
    SearchConcreteDecoratorAuthor,
    SearchConcreteDecoratorISBN,
    SearchConcreteDecoratorTitle,
    SearchConcreteDecoratorLimitResults,
)


class SearchStrategy(ABC):  # pylint: disable=too-few-public-methods
    """Interface for defining search functionality of sections"""

    @abstractmethod
    def search(self, query) -> list[SearchSection]:
        """
        Searches books database
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results, divided into sections
        """


class SearchContext:  # pylint: disable=too-few-public-methods
    """
    Defines the interface that is interacted with by the client
    """

    def __init__(self, search_strategy: SearchStrategy) -> None:
        """
        Constructor for SearchContext
        Arguments:
            search_strategy (SearchStrategy) - strategy used to search
        """

        self._search_strategy = search_strategy

    def search(self, query: str) -> list[SearchSection]:
        """
        Searches books database
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results, divided into sections
        """
        return self._search_strategy.search(query)

    # def get_search_strategy(self) -> SearchStrategy:
    #     """Get method for search strategy"""
    #     return self._search_strategy


class ConcreteSearchStrategyAll(SearchStrategy):  # pylint: disable=too-few-public-methods
    """
    Strategy that searches by authors, titles, genres, and isbn
    """

    def search(self, query) -> list[SearchSection]:  # pylint: disable=too-few-public-methods
        """
        Searches books database
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results, divided into sections
        """
        search_component = SearchConcreteDecoratorLimitResults(
            SearchConcreteDecoratorTitle(
                SearchConcreteDecoratorAuthor(
                    SearchConcreteDecoratorGenre(
                        SearchConcreteDecoratorISBN(SearchConcreteComponent())
                    )
                )
            )
        )
        results = search_component.operation(query)
        return results


class ConcreteSearchStrategyTitle(SearchStrategy):  # pylint: disable=too-few-public-methods
    """
    Strategy that searches for titles
    """

    def search(self, query) -> list[SearchSection]:
        """
        Searches books database
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results, divided into sections
        """
        search_component = SearchConcreteDecoratorTitle(SearchConcreteComponent())
        results = search_component.operation(query)
        return results


class ConcreteSearchStrategyAuthor(SearchStrategy):  # pylint: disable=too-few-public-methods
    """
    Strategy that searches for authors
    """

    def search(self, query) -> list[SearchSection]:
        """
        Searches books database
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results, divided into sections
        """
        search_component = SearchConcreteDecoratorAuthor(SearchConcreteComponent())
        results = search_component.operation(query)
        return results


class ConcreteSearchStrategyGenre(SearchStrategy):  # pylint: disable=too-few-public-methods
    """
    Strategy that searches for genres
    """

    def search(self, query) -> list[SearchSection]:
        """
        Searches books database
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results, divided into sections
        """
        search_component = SearchConcreteDecoratorGenre(SearchConcreteComponent())
        results = search_component.operation(query)
        return results
