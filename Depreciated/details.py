"""Methods for getting details about a book."""
from datetime import datetime
from statistics import fmean
from ProductionCode.data import goodreads_data, bookban_data
from ProductionCode.search import fuzzy_match

def print_book_full(book, bans):
    """Pretty prints all possible book info."""
    output = "Details for " + book["title"] + " by "
    output += ", ".join(book["authors"])
    # this conversion will eventually happen in the Book class
    output += f" ({datetime.fromtimestamp(book['year']/1000).year}, ISBN: {book['isbn']})"
    # print the entire summary field
    output += "\nBook details from Goodreads: "+book["summary"]
    # print entire genre list
    output += "\nGenres: " + ", ".join(book["genres"])
    # print weighted avg of reviews (this conversion will eventually happen in the Book class)
    output += f"\nAverage review: {fmean([1,2,3,4,5],weights=book['rating']):.1f} stars"
    for ban in bans:
        output += f"\nBanned in {ban['district']}, {ban['state']} in {ban['ban_date']}"
    return output

def get_book_from_isbn(isbn):
    """Returns the book object associated with an ISBN number."""
    matches = [book for book in goodreads_data if book["isbn"] == isbn]
    if len(matches) == 0:
        raise ValueError
    # TODOlater: write a test to confirm that len(matches) == 1
    return matches[0]

def get_details(isbn):
    """Returns the details for a book. ISBN should be a string."""
    book = get_book_from_isbn(isbn)
    # here we join the goodreads book data with the bookban csv data.
    # eventually this should use isbn but for now fuzzy match on title/author
    bans = [ban for ban in bookban_data if
        fuzzy_match(ban["title"], book["title"].split(":")[0], True)
    ]
    return print_book_full(book, bans)
