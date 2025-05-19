"""This is the main file for the Flask application."""

import json
from flask import Flask, abort, render_template, request
from ProductionCode.details import get_details
from ProductionCode.datasource import DataSource

ds = DataSource()
app = Flask(__name__)

database_most_banned_map = {
    "states": ds.get_most_banned_states,
    "districts": ds.get_most_banned_districts,
    "authors": ds.get_most_banned_authors,
    "titles": ds.get_most_banned_titles,
}

database_search_map = {
    "title": ds.books_search_title,
    "author": ds.books_search_author,
    "genre": ds.books_search_genre,
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


def object_list_to_string(object_list):
    return map(str, object_list)


@app.route("/")
def homepage():
    """The homepage for the Flask app
    args: None
    Returns:
        (str): a string of the homepage with line breaks
    """

    return render_template("index.html", most_banned_books=ds.get_most_banned_books(5))

    # return (
    #     "The following addresses can be used to see information about banned books:<br /><br />"
    #     f"{USAGE}"
    # )


@app.route("/details/<isbn>")
def details(isbn):
    """The endpoint for the details of a book.

    Args:
        isbn (str): the ISBN number of the book
    Returns:
        (str): a string of details with line breaks between fields
    """
    # variation on format_list_with_linebreak
    return render_template("book.html", ban_isbn = ds.bans_from_isbn(isbn), book_isbn = ds.book_from_isbn(isbn))


# @app.route("/search/<field>/<query>", strict_slashes=False)
# def search(field, query):
#     """The endpoint for searching for a field

#     Args:
#         field (str): the category the search query is for; title, author, or genre
#         query (str): the search term
#     Returns:
#         (str): a string of search results, separated by line breaks
#     """

#     function = database_search_map[field]
#     output = function(query)
#     return format_list_with_linebreak(output)


@app.route("/most-banned/<field>/<max_results>", strict_slashes=False)
def most_banned(field, max_results):
    """The endpoint for the most banned titles
    Args:
        field (str): the category to search for; states, districts, authors, or titles
        max_results (int): the number of results to return
    Returns:
        (str): a string of the most banned titles, separated by line breaks
    """
    if not max_results.isdigit() or field not in database_most_banned_map:
        abort(500)

    function = database_most_banned_map[field]
    output = function(int(max_results))
    return format_list_with_linebreak(output)

@app.route("/map")
def map():
    """Route for map page"""
    ds = DataSource()
    most_banned_states = ds.get_most_banned_states(10)
    return render_template("map.html", most_banned_states=most_banned_states)


@app.errorhandler(500)
def python_bug(_error):
    """The endpoint for the 500 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 500: Bad Request
    """
    return "500: Bad Request", 500


def format_list_with_linebreak(object_list):
    """Helper method for joining a list of strings with line breaks
    Args:
        list_of_strings (str[]): a list of strings
    Returns:
        (str): a string composed of each element of the list joined by line breaks
    """
    string_list = object_list_to_string(object_list)
    return "</br>".join(string_list)

# @app.route("/search/<query>", strict_slashes=False)
# def search(query):
#     """The endpoint for searching"""
#     ds = DataSource()
#     results_isbn = ds.book_from_isbn(query)
#     results_title = ds.books_search_title(query)
#     results_author = ds.books_search_author(query)
#     return render_template(
#         "search.html",
#         query=query,
#         results_isbn=results_isbn,
#         results_title=results_title,
#         results_author=results_author,
#     )


@app.errorhandler(404)
def page_not_found(_error):
    """The endpoint for the 404 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 404: Sorry page not found with usage instructions
    """

    return f"404: Sorry page not found<br /><br />{USAGE}<br /><br />{EXAMPLES}"



@app.route("/search")
def search():
    """The endpoint for searching"""
    query = request.args.get("searchterm")
    type = request.args.get("type")
    ds = DataSource()

    if type == "title":
        results_isbn = None
        results_title = ds.books_search_title(query)
        results_author = None
    elif type == "author":
        results_isbn = None
        results_title = None
        results_author = ds.books_search_author(query)
    else:
        results_isbn = ds.book_from_isbn(query)
        results_title = ds.books_search_title(query)[:5]
        results_author = ds.books_search_author(query)[:5]
    return render_template(
        "search.html",
        query=query,
        type=type,
        results_isbn=results_isbn,
        results_title=results_title,
        results_author=results_author,
    )

@app.route("/books")
def books():
    ds = DataSource()
    # replace later
    books = ds.books_search_title("")
    return render_template("books.html", books=books)

@app.route("/genres/<genre>")
def genres(genre):
    ds = DataSource()
    books = ds.books_search_genre(genre)
    return render_template("genre.html", books=books, genre=genre)

@app.route("/authors/<author>")
def authors(author):
    ds = DataSource()
    books = ds.books_search_author(author)
    return render_template("author.html", books=books, author=author)

@app.route("/most-banned/authors")
def most_banned_authors():
    return render_template("most-banned")

# API ENDPOINTS

@app.route("/get-most-banned-states")
def get_most_banned_states():
    ds = DataSource()
    most_banned_states = ds.get_most_banned_states(99)
    ban_json = json.dumps(most_banned_states, default=lambda obj: obj.__dict__)
    return ban_json


if __name__ == "__main__":
    app.run(port="5132")
