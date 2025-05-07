"""This is the main file for the Flask application."""

from flask import Flask, abort
from ProductionCode.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles,
)
from ProductionCode.search import search_author, search_genre, search_title
from ProductionCode.details import get_details
from ProductionCode.datasource import DataSource

app = Flask(__name__)

most_banned_map = {
    "states": most_banned_states,
    "districts": most_banned_districts,
    "authors": most_banned_authors,
    "titles": most_banned_titles,
}

USAGE = (
    'To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;".<br />'
    "&lt;field&gt; can be title, author, or genre<br />"
    "&lt;query&gt; is the search term<br /><br />"
    "To see a list of categories with the most banned books, go to "
    '"/most-banned/&lt;field&gt;/&lt;max_results&gt;".<br />'
    "&lt;field&gt; can be states, districts, authors, or titles<br />"
    "&lt;max_results&gt; is the number of results you want to display<br /><br />"
    'To get the details about a specific book, go to "/details/&lt;isbn&gt;".<br />'
    "&lt;isbn&gt; is the ISBN number of the book, which can be found using /search"
)

EXAMPLES = (
    "Examples:<br />"
    "/search/title/Kaleidoscope<br />"
    "/most-banned/states/5<br />"
    "/most-banned/authors/10<br />"
    "/details/440236924<br />"
)


@app.route("/")
def homepage():
    """The homepage for the Flask app
    args: None
    Returns:
        (str): a string of the homepage with line breaks
    """

    return (
        "The following addresses can be used to see information about banned books:<br /><br />"
        f"{USAGE}"
    )


@app.route("/details/<isbn>")
def details(isbn):
    """The endpoint for the details of a book.

    Args:
        isbn (str): the ISBN number of the book
    Returns:
        (str): a string of details with line breaks between fields
    """
    try:
        output = get_details(isbn)
    except ValueError:
        abort(400, "No book with that ISBN found!")

    # variation on format_list_with_linebreak
    return output.replace("\n", "<br /><br />")


@app.route("/search/<field>/<query>", strict_slashes=False)
def search(field, query):
    """The endpoint for searching for a field

    Args:
        field (str): the category the search query is for; title, author, or genre
        query (str): the search term
    Returns:
        (str): a string of search results, separated by line breaks
    """

    ds = DataSource()

    output = ""
    # output = search_title(query)
    # match field:
    #     case "title":
    #         output = search_title(query)
    #     case "author":
    #         output = search_author(query)
    #     case "genre":
    #         output = search_genre(query)
    #     case _:
    #         abort(
    #             400,
    #             "Invalid search field, options for field are title, author, or genre.",
    #         )
    output = ds.books_search_title(query)
    output = map(str, output)
    return format_list_with_linebreak(output)


@app.route("/most-banned/<field>/<max_results>", strict_slashes=False)
def most_banned(field, max_results):
    """The endpoint for the most banned titles
    Args:
        field (str): the category to search for; states, districts, authors, or titles
        max_results (int): the number of results to return
    Returns:
        (str): a string of the most banned titles, separated by line breaks
    """
    if not max_results.isdigit() or field not in most_banned_map:
        abort(500)

    function = most_banned_map[field]
    return format_list_with_linebreak(function(int(max_results)))


@app.errorhandler(500)
def python_bug(_error):
    """The endpoint for the 500 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 500: Bad Request
    """
    return "500: Bad Request", 500


def format_list_with_linebreak(list_of_strings):
    """Helper method for joining a list of strings with line breaks
    Args:
        list_of_strings (str[]): a list of strings
    Returns:
        (str): a string composed of each element of the list joined by line breaks
    """
    return "</br>".join(list_of_strings)


@app.errorhandler(404)
def page_not_found(_error):
    """The endpoint for the 404 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 404: Sorry page not found with usage instructions
    """

    return f"404: Sorry page not found<br /><br />{USAGE}<br /><br />{EXAMPLES}"


if __name__ == "__main__":
    app.run(port=7000)
