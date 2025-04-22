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


@app.route("/most-banned/<field>/<query>")
def most_banned(field, limit):
    pass


if __name__ == "./main__":
    app.run()

