"""This is the main file for the Flask application."""

import json
from flask import Flask, render_template, request
from ProductionCode.datasource import DataSource

app = Flask(__name__)


@app.route("/")
def homepage():
    """The homepage for the Flask app
    args: None
    Returns:
        (str): a string of the homepage with line breaks
    """
    ds = DataSource()
    return render_template("index.html", most_banned_books=ds.get_most_banned_books(5))


@app.route("/details/<isbn>")
def details(isbn):
    """The endpoint for the details of a book.

    Args:
        isbn (str): the ISBN number of the book
    Returns:
        (str): a string of details with line breaks between fields
    """
    ds = DataSource()
    return render_template(
        "book.html", ban_isbn=ds.bans_from_isbn(isbn), book_isbn=ds.book_from_isbn(isbn)
    )


@app.route("/map")
def map_page():
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

    return render_template("/404.html")


@app.errorhandler(404)
def page_not_found(_error):
    """The endpoint for the 404 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 404: Sorry page not found with usage instructions
    """

    # # TODO: Replace with 404 page
    # return "404: Sorry page not found"
    return render_template("404.html")


@app.route("/search")
def search():
    """The endpoint for search page"""
    query = request.args.get("searchterm")
    search_type = request.args.get("type")
    ds = DataSource()

    if search_type == "title":
        results_isbn = None
        results_title = ds.books_search_title(query)
        results_author = None
    elif search_type == "author":
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
        type=search_type,
        results_isbn=results_isbn,
        results_title=results_title,
        results_author=results_author,
    )


@app.route("/books")
def books():
    """The endpoint for books page"""
    ds = DataSource()
    # replace later
    book_list = ds.books_search_title("")
    return render_template("books.html", books=book_list)


@app.route("/genres/<genre>")
def genres(genre):
    """The endpoint for genre page"""
    ds = DataSource()
    book_list = ds.books_search_genre(genre)
    return render_template("genre.html", books=book_list, genre=genre)


@app.route("/authors/<author>")
def authors(author):
    """The endpoint for author page"""
    ds = DataSource()
    book_list = ds.books_search_author(author)
    return render_template("author.html", books=book_list, author=author)


# API ENDPOINTS


@app.route("/get-most-banned-states")
def get_most_banned_states():
    """The endpoint for get-most-banned-states api call"""
    ds = DataSource()
    most_banned_states = ds.get_most_banned_states(99)
    ban_json = json.dumps(most_banned_states, default=lambda obj: obj.__dict__)
    return ban_json


if __name__ == "__main__":
    app.run(port=5132)
