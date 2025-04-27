"""
This is the main file for the Flask application.
"""

from flask import Flask, abort
from ProductionCode.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles,
)

from ProductionCode.search import search_author, search_genre, search_title

app = Flask(__name__)

most_banned_map = {
    "states": most_banned_states,
    "districts": most_banned_districts,
    "authors": most_banned_authors,
    "titles": most_banned_titles,
}


@app.route("/")
def homepage():
    """The homepage for the Flask app"""

    return (
        "The following addresses can be used to see information about banned books:</br></br>"
        'To search for banned books, go to "/search/&lt;field&gt;/&lt;query&gt;".</br>'
        "&lt;field&gt; can be title, author, or genre</br>"
        "&lt;query&gt; is the search term</br></br>"
        'To see a list of categories with the most banned books, go to "/most-banned/&lt;field&gt;/&lt;max_results&gt;".</br>'
        "&lt;field&gt; can be states, districts, authors, or titles"
        "&lt;max_results&gt; is the number of results you want to display"
    )


@app.route("/details/<isbn>")
def details(_isbn):
    """
    The endpoint for the details of a book
    """


@app.route("/search/<field>/<query>", strict_slashes=False)
def search(field, query):
    """The endpoint for searching for a field

    Args:
        field (str): the category the search query is for; title, author, or genre
        query (str): the search term
    Returns:
        (str): a string of search results, separated by line breaks
    """
    output = ""
    match field:
        case "title":
            output = search_title(query)
        case "author":
            output = search_author(query)
        case "genre":
            output = search_genre(query)
        case _:
            abort(
                400,
                "Invalid search field, options for field are title, author, or genre.",
            )
    return format_list_with_linebreak(output)


@app.route("/most-banned/<field>/<max_results>", strict_slashes=False)
def most_banned(field, max_results):
    """
    The endpoint for the most banned titles
    """
    if not max_results.isdigit() or field not in most_banned_map:
        abort(500)

    function = most_banned_map[field]
    return function(int(max_results))


@app.errorhandler(500)
def python_bug(_error):
    """
    The endpoint for the 500 error
    """
    return "500: Bad Request", 500


def format_list_with_linebreak(list_of_strings):
    """Helper method for joining a list of strings with line breaks
    Args:
        list_of_strings (str[]): a list of strings
    Returns:
        (str): a string composed of each element of the list joined by line breaks
    """
    return "<br>".join(list_of_strings)


if __name__ == "__main__":
    app.run()
