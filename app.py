"""This is the main file for the Flask application."""

import json
from flask import Flask, render_template, request
from ProductionCode.datasource import DataSource
from ProductionCode.search_section import SearchSection, SearchSectionBook
from ProductionCode.search_strategies import (
    ConcreteSearchStrategyAll,
    ConcreteSearchStrategyAuthor,
    ConcreteSearchStrategyGenre,
    ConcreteSearchStrategyTitle,
    SearchContext,
)

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
    most_banned = ds.get_most_banned_states(10)
    return render_template("map.html", most_banned_states=most_banned)


@app.errorhandler(500)
def python_bug(error):
    """The endpoint for the 500 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 500: Bad Request
    """
    print(error)
    return render_template("error.html", error=error, code=500)


@app.errorhandler(404)
def page_not_found(error):
    """The endpoint for the 404 error
    Args:
        _error (Exception): the error that was raised
    Returns:
        (str): 404: Sorry page not found with usage instructions
    """
    return render_template("error.html", error=error, code=404)


@app.route("/search")
def search():
    """The endpoint for the search page"""
    query = request.args.get("searchterm")
    search_type = request.args.get("type")
    search_strategy = (
        ConcreteSearchStrategyTitle()
        if search_type == "title"
        else ConcreteSearchStrategyAuthor()
        if search_type == "author"
        else ConcreteSearchStrategyGenre()
        if search_type == "genre"
        else ConcreteSearchStrategyAll()
    )
    search_context = SearchContext(search_strategy)
    results = search_context.search(query)
    print(results)
    return render_template(
        "search.html", query=query, type=search_type, results=results
    )


@app.route("/books")
def books():
    """The endpoint for books page"""
    ds = DataSource()
    # replace later
    sections = ds.books_search_titles_to_sections("")

    return render_template("books.html", results = sections)

@app.route("/books/<letter>")
def books_starts_with(letter):
    """The endpoint for books page"""
    ds = DataSource()
    sections = ds.books_search_titles_to_sections(letter)
    return render_template("books.html", results = sections)

@app.route("/genre/<genre>")
def genres(genre):
    """The endpoint for genre page"""
    ds = DataSource()
    book_list = ds.books_search_genre(genre)
    return render_template("genre.html", books=book_list, genre=genre)


@app.route("/genres")
def genres_list():
    """The endpoint for the overall genres page"""
    ds = DataSource()
    fiction = ds.books_search_genre("Fiction")
    romance = ds.books_search_genre("Romance")
    childrens = ds.books_search_genre("Childrens")
    book_list = ds.books_search_title("")
    return render_template(
        "genres.html",
        fiction=fiction,
        romance=romance,
        childrens=childrens,
        books=book_list,
    )


@app.route("/author/<author>")
def authors(author):
    """The endpoint for author page"""
    ds = DataSource()
    book_list = ds.books_search_author(author)
    return render_template("author.html", books=book_list, author=author)


@app.route("/most-banned-authors")
def most_banned_authors():
    """The endpoint for most_banned_authors page"""
    ds = DataSource()
    banned_authors = ds.get_most_banned_authors(30)
    return render_template("most-banned-authors.html", authors=banned_authors)


@app.route("/most-banned-states")
def most_banned_states():
    """The endpoint for most_banned_authors page"""
    ds = DataSource()
    states = ds.get_most_banned_states(30)
    return render_template("most-banned-states.html", states=states)


@app.route("/most-banned-districts")
def most_banned_districts():
    """The endpoint for most_banned_districts page"""
    ds = DataSource()
    districts = ds.get_most_banned_districts(30)
    return render_template("most-banned-districts.html", districts=districts)


@app.route("/most-banned-books")
def most_banned_books():
    """The endpoint for most_banned_books page"""
    ds = DataSource()
    return render_template(
        "most-banned-books.html", most_banned_books=ds.get_most_banned_books(30)
    )


@app.route("/authors")
def authors_list():
    """The endpoint for the overall authors page"""
    ds = DataSource()
    book_list = ds.books_search_title("")
    return render_template("authors.html", books=book_list)


# API ENDPOINTS


@app.route("/get-most-banned-states")
def get_most_banned_states():
    """The endpoint for get-most-banned-states api call"""
    ds = DataSource()
    most_banned = ds.get_most_banned_states(99)
    ban_json = json.dumps(most_banned, default=lambda obj: obj.__dict__)
    return ban_json


@app.route("/get-most-banned-states-with-isbn")
def get_most_banned_states_with_isbn():
    """The endpoint for the get-book-banned-in-states api call"""
    isbn = request.args.get("isbn")

    ds = DataSource()
    bans = ds.get_most_banned_states_with_isbn(99, isbn)
    ban_json = json.dumps(bans, default=lambda obj: obj.__dict__)
    return ban_json


if __name__ == "__main__":
    app.run(port=5132)
