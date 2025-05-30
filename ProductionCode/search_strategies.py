"""Module for Search Strategies"""

from abc import ABC, abstractmethod
from ProductionCode.search_decorators import SearchSection
from ProductionCode.search_decorators import (
    SearchConcreteComponent,
    SearchConcreteDecoratorAuthor,
    SearchConcreteDecoratorISBN,
    SearchConcreteDecoratorTitle,
    SearchConcreteDecoratorLimitResults,
)


class SearchStrategy(ABC):
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


class SearchContext:
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


class ConcreteSearchStrategyAll(SearchStrategy):
    """
    Strategy that searches for authors, titles, and isbn
    """

    def search(self, query) -> list[SearchSection]:
        """
        Searches books database
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results, divided into sections
        """
        search_component = SearchConcreteDecoratorLimitResults(
            SearchConcreteDecoratorAuthor(
                SearchConcreteDecoratorTitle(
                    SearchConcreteDecoratorISBN(SearchConcreteComponent())
                )
            )
        )
        results = search_component.operation(query)
        # [setattr(result, "results", result.results[:MAX_RESULTS]) for result in results]
        return results


class ConcreteSearchStrategyTitle(SearchStrategy):
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


class ConcreteSearchStrategyAuthor(SearchStrategy):
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
