"""Methods for searching the goodreads database by field."""

from ProductionCode.data import goodreads_data

def print_book_short(book):
    """Pretty prints basic book info (title, author/s, isbn).
    Arguments:
    book - the book to print from.
    Returns: string formatted with the short book info.
    """
    output = book["title"] + " by "
    output += ", ".join(book["authors"])
    if book["isbn"] is not None:
        output += f" (ISBN: {book["isbn"]})"
    else:
        output += " (ISBN not found)"
    return output

def fuzzy_match(data, query, partial):
    """Matches two strings regardless of case or whitespace.
    Arguments:
    data - the string from the database
    query - the query to match it against
    partial: whether a partial match is ok
    Returns: boolean"""
    if partial:
        return query.lower().strip() in data.lower().strip()
    return query.lower().strip() == data.lower().strip()

def query_data(data, key, value, partial=False):
    """Queries key from the data for matching a specific value.
    Arguments:
    data - the data to search
    key - the field to compare
    value - the query of the user
    partial - whether a partial match is ok (default false)
    Returns: list of objects that match the query
    """
    matches = []
    for entry in data:
        # if field is null, skip it
        if entry[key] is None:
            continue
        # for fields that are lists, match if any value is the same
        if isinstance(entry[key], list):
            if any(fuzzy_match(item, value, partial) for item in entry[key]):
                matches.append(entry)
        # for fields that are strings, just match the string
        elif isinstance(entry[key], str):
            if fuzzy_match(entry[key], value, partial):
                matches.append(entry)
    return matches

def search_title(title):
    """High level title search, to be called by the CLI."""
    # allow titles to partially match (ie "Harry Potter" matches "Harry Potter and the...")
    entries = query_data(goodreads_data, "title", title, True)
    # for this query, only print short info
    entries = map(print_book_short, entries)
    return entries

def search_author(author):
    """High level author search, to be called by the CLI."""
    entries = query_data(goodreads_data, "authors", author, True)
    # for this query, only print short info
    entries = map(print_book_short, entries)
    return entries

def search_genre(genre):
    """High level genre search, to be called by the CLI."""
    entries = query_data(goodreads_data, "genres", genre)
    # for this query, only print short info
    entries = map(print_book_short, entries)
    return entries

def main():
    """Main function for informal testing."""
    search_results = search_title("kingdom of the")
    for result in search_results:
        print(result)
    print("----------")
    search_results = search_author("dori hillestad butler")
    for result in search_results:
        print(result)

if __name__  == "__main__":
    main()
