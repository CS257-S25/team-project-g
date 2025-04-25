'''
This is the main file for the Flask application.
'''
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


@app.route("/details/<isbn>")
def details(_isbn):
    '''
    The endpoint for the details of a book
    '''


@app.route("/search/<field>/<query>", strict_slashes=False)
def search(field, query):
    """
    The endpoint for searching for a field
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
            abort(500)
    return output


@app.route("/most-banned/<field>/<limit>", strict_slashes=False)
def most_banned(field, limit):
    """
    The endpoint for the most banned titles
    """
    if not limit.isdigit() or field not in most_banned_map:
        abort(500)

    function = most_banned_map[field]
    return function(int(limit))


@app.errorhandler(500)
def python_bug(_error):
    """
    The endpoint for the 500 error
    """
    return "500: Bad Request", 500


if __name__ == "__main__":
    app.run()
