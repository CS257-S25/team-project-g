from ProductionCode.book import Book
from ProductionCode.datasource import DataSource
from Tests.mock_data import mock_book


class SearchComponent:
    """
    The base SearchComponent interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> list[list[Book]]:
        return []


class SearchConcreteComponent(SearchComponent):
    """
    SearchConcreteComponent provides default implimentation for SearchComponent interface
    """

    def operation(self) -> list[list[Book]]:
        return [[mock_book]]


class SearchDecorator:
    """
    SearchDecorator defines wrapping interface for all Concrete Decorators
    """

    def __init__(self, search_component: SearchComponent) -> None:
        self._search_component: SearchComponent = search_component

    @property
    def search_component(self) -> SearchComponent:
        """
        The SearchDecorator delegates all work to the wrapped component
        """
        return self._search_component

    def operation(self) -> list[list[Book]]:
        return self._search_component.operation()


class SearchConcreteDecoratorAuthor(SearchDecorator):
    """
    Appends author search to the list
    """

    def operation(self) -> list[list[Book]]:
        search_author = self.search_author("a")
        return [search_author] + self.search_component.operation()

    def search_author(self, query):
        ds = DataSource()
        results = ds.books_search_author(query)
        return results


def search(search_component: SearchComponent) -> None:
    print(search_component.operation())


if __name__ == "__main__":
    simple = SearchConcreteComponent()
    search(simple)
