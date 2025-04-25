from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    pass


@app.route("/details/<isbn>")
def details(isbn):
    pass


@app.route("/search/<field>/<query>")
def search(field, query):
    pass


@app.route("/most-banned-titles/<limit>", strict_slashes=False)
def most_banned_titles_page(limit):
    # add error handling
    most_banned = most_banned_titles(int(limit))
    # most_banned = map(lambda x: x + "\n", most_banned)
    return most_banned


if __name__ == "./main__":
    app.run()
