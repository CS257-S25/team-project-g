"""Module for Search Section class"""

from ProductionCode.book import Book


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

    def get_heading(self) -> str:
        """Get method for heading of section"""
        return self.heading

    def get_search_type(self) -> str:
        """Get method for the search type of section"""
        return self.search_type

    def get_results(self) -> list[Book]:
        """Get method for search results of section"""
        return self.results
