from abc import ABC, abstractmethod
from ProductionCode.search_decorators import SearchSection
from ProductionCode.search_decorators import SearchConcreteComponent, SearchConcreteDecoratorAuthor, SearchConcreteDecoratorISBN, SearchConcreteDecoratorTitle

class SearchContext():
    def __init__(self, search_strategy) -> None:
        self._search_strategy = search_strategy
    
    def search(self, query) -> list[SearchSection]:
        return self._search_strategy.search(query)
    
class SearchStrategy(ABC):
    @abstractmethod
    def search(self, query) -> list[SearchSection]:
        pass

class ConcreteSearchStrategyAll(SearchStrategy):
    def search(self, query) -> list[SearchSection]:
        search_component = SearchConcreteDecoratorAuthor(SearchConcreteDecoratorTitle(SearchConcreteDecoratorISBN(SearchConcreteComponent())))
        results = search_component.operation(query)
        return results


class ConcreteSearchStrategyTitle(SearchStrategy):
    def search(self, query) -> list[SearchSection]:
        search_component = SearchConcreteDecoratorTitle(SearchConcreteComponent())
        results = search_component.operation(query)
        return results

class ConcreteSearchStrategyAuthor(SearchStrategy):
    def search(self, query) -> list[SearchSection]:
        search_component = SearchConcreteDecoratorAuthor(SearchConcreteComponent())
        results = search_component.operation(query)
        return results