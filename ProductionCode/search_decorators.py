"""Decorators for modifying search functionality"""

from ProductionCode.book import Book
from ProductionCode.datasource import DataSource


class SearchSection:
    """Defines a section of the search results"""

    def __init__(self, heading: str, search_type: str, results: list[Book]) -> None:
        """
        Constructor for SearchSection
        Arguments:
            heading (str) - heading of the section (displayed)
            type (str) - type of the section (internal)
            results (list[Book]) - list of books in the section
        """
        self.heading = heading
        self.search_type = search_type
        self.results = results


class SearchComponent:
    """
    The base SearchComponent interface defines operations that can be altered by
    decorators.
    """

    def operation(self, _query) -> list[SearchSection]:
        """Operation to be implimented by decorators"""
        return []


class SearchConcreteComponent(SearchComponent):
    """
    SearchConcreteComponent provides default implimentation for SearchComponent interface
    """

    def operation(self, _query) -> list[SearchSection]:
        """Default operation implimentation"""
        return []


class SearchDecorator:
    """
    SearchDecorator defines wrapping interface for all Concrete Decorators
    """

    def __init__(self, search_component: SearchComponent) -> None:
        """
        Constructor for SearchDecorator
        Arguments:
            search_component (SearchComponent) - the wrapped component
        """
        self._search_component: SearchComponent = search_component

    @property
    def search_component(self) -> SearchComponent:
        """
        The SearchDecorator delegates all work to the wrapped component
        Returns:
            (SearchComponent) - the wrapped component
        """
        return self._search_component

    def operation(self, query) -> list[SearchSection]:
        """
        The SearchDecorator calls the operation on the wrapped component
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results divided into sections
        """
        return self._search_component.operation(query)


class SearchConcreteDecoratorAuthor(SearchDecorator):
    """
    Appends author search to the list
    """

    def operation(self, query) -> list[SearchSection]:
        """
        Author search
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results divided into sections
        """
        search_author = self.search_author(query)
        return self.search_component.operation(query) + [search_author]

    def search_author(self, query):
        """
        Author search database call
        Arguments:
            query (str) - the search query
        Returns:
            (SearchSection) - author search section
        """
        ds = DataSource()
        results = ds.books_search_author(query)
        section = SearchSection("Author", "author", results)
        return section


class SearchConcreteDecoratorISBN(SearchDecorator):
    """
    Appends ISBN search to the list
    """

    def operation(self, query) -> list[SearchSection]:
        """
        ISBN search
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results divided into sections
        """
        search_isbn = self.search_isbn(query)
        return self.search_component.operation(query) + [search_isbn]

    def search_isbn(self, query):
        """
        ISBN search database call
        Arguments:
            query (str) - the search query
        Returns:
            (SearchSection) - isbn search section
        """
        ds = DataSource()
        results = ds.book_from_isbn(query)
        if results:
            return SearchSection("ISBN", "isbn", [results])
        return SearchSection("ISBN", "isbn", [])


class SearchConcreteDecoratorTitle(SearchDecorator):
    """
    Appends title search to the list
    """

    def operation(self, query) -> list[SearchSection]:
        """
        Title search
        Arguments:
            query (str) - the search query
        Returns:
            (list[SearchSection]) - search results divided into sections
        """
        search_isbn = self.search_title(query)
        return self.search_component.operation(query) + [search_isbn]

    def search_title(self, query):
        """
        Title search database call
        Arguments:
            query (str) - the search query
        Returns:
            (SearchSection) - title search section
        """
        ds = DataSource()
        results = ds.books_search_title(query)
        section = SearchSection("Title", "title", results)
        return section


class SearchConcreteDecoratorLimitResults(SearchDecorator):
    """
    Limits the number of results in each section
    """

    max_results = 5
    # eventually, max a parameter
    # def __init__(self, max_results):
    #     self.max_results = max_results

    def operation(self, query) -> list[SearchSection]:
        results = self.search_component.operation(query)
        for section in results:
            section.results = section.results[: self.max_results]
        return results
