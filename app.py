from flask import Flask, abort
from ProductionCode.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles,
)

app = Flask(__name__)

most_banned_map = {
    "states": most_banned_states,
    "districts": most_banned_districts,
    "authors": most_banned_authors,
    "titles": most_banned_titles,
}


@app.route("/details/<isbn>")
def details(isbn):
    pass


@app.route("/search/<field>/<query>")
def search(field, query):
    pass


@app.route("/most-banned/<field>/<limit>", strict_slashes=False)
def most_banned(field, limit):
    """
    The endpoint for the most banned titles
    """
    if not limit.isdigit() or field not in most_banned_map:
        abort(400)

    function = most_banned_map[field]
    return function(int(limit))


@app.errorhandler(400)
def python_bug(e):
    """
    The endpoint for the most banned titles
    """
    return "400: Bad Request", 400


if __name__ == "__main__":
    app.run()
