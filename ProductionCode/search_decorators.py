from ProductionCode.book import Book
from ProductionCode.datasource import DataSource

class SearchSection:
    def __init__(self, heading: str, results: list[Book]):
        self.heading = heading
        self.results = results

class SearchComponent:
    """
    The base SearchComponent interface defines operations that can be altered by
    decorators.
    """

    def operation(self, query) -> list[SearchSection]:
        return []


class SearchConcreteComponent(SearchComponent):
    """
    SearchConcreteComponent provides default implimentation for SearchComponent interface
    """

    def operation(self, query) -> list[SearchSection]:
        return []


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

    def operation(self, query) -> list[SearchSection]:
        return self._search_component.operation(query)


class SearchConcreteDecoratorAuthor(SearchDecorator):
    """
    Appends author search to the list
    """

    def operation(self, query) -> list[SearchSection]:
        search_author = self.search_author(query)
        return self.search_component.operation(query) + [search_author]

    def search_author(self, query):
        ds = DataSource()
        results = ds.books_search_author(query)
        section = SearchSection("Author", results)
        return section 


class SearchConcreteDecoratorISBN(SearchDecorator):
    """
    Appends ISBN search to the list
    """

    def operation(self, query) -> list[SearchSection]:
        search_isbn = self.search_isbn(query)
        return self.search_component.operation(query) + [search_isbn]

    def search_isbn(self, query):
        ds = DataSource()
        results = ds.book_from_isbn(query)
        if results:
            return SearchSection("ISBN", [results])
        else:
            return SearchSection("ISBN", [])


class SearchConcreteDecoratorTitle(SearchDecorator):
    """
    Appends title search to the list
    """

    def operation(self, query) -> list[SearchSection]:
        search_isbn = self.search_title(query)
        return self.search_component.operation(query) + [search_isbn]

    def search_title(self, query):
        ds = DataSource()
        results = ds.books_search_title(query)
        section = SearchSection("Title", results)
        return section 



def search(search_component: SearchComponent, query) -> None:

   results = search_component.operation(query)
   return results


if __name__ == "__main__":
    simple = SearchConcreteComponent()
    search(simple)
