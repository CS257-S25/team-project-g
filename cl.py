"""
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
"""

import sys
import argparse

from ProductionCode.datasource import DataSource


def main():
    """Main function for the command line interface (CLI) for the project."""
    parser = argparse.ArgumentParser(
        # The command line interface (CLI) for the project.
        prog="cl.py",
        description="Command line interface for the project",
        epilog="This is the command line interface for the project.",
        usage="%(prog)s [options] [args]",
    )
    parser.add_argument(
        # Search for a title in the database
        "--search-title",
        "--st",
        help="Search for a title in the database",
        type=str,
        metavar="TITLE",
    )
    parser.add_argument(
        # Search for an author in the database
        "--search-author",
        "--sa",
        help="Search for an author in the database",
        type=str,
        metavar="AUTHOR",
    )
    parser.add_argument(
        # Search for a genre in the database
        "--search-genre",
        "--sg",
        help="Search for a genre in the database",
        type=str,
        metavar="GENRE",
    )
    parser.add_argument(
        # Get the most banned districts in the database
        "--most-banned-districts",
        "--mbd",
        help="Get the most banned districts in the database",
        type=int,
        metavar="MAX_RESULTS",
    )
    parser.add_argument(
        # Get the most banned authors in the database
        "--most-banned-authors",
        "--mba",
        help="Get the most banned authors in the database",
        type=int,
        metavar="MAX_RESULTS",
    )
    parser.add_argument(
        # Get the most banned states in the database
        "--most-banned-states",
        "--mbs",
        help="Get the most banned states in the database",
        type=int,
        metavar="MAX_RESULTS",
    )
    parser.add_argument(
        # Get the most banned titles in the database
        "--most-banned-titles",
        "--mbt",
        help="Get the most banned titles in the database",
        type=int,
        metavar="MAX_RESULTS",
    )
    args = parser.parse_args()

    ds = DataSource()

    cl_map = {
        "search_title": ds.get_books_by_title,
        "search_author": ds.get_books_by_author,
        "search_genre": ds.get_books_by_genre,
        "most_banned_districts": ds.get_most_banned_districts,
        "most_banned_authors": ds.get_most_banned_authors,
        "most_banned_states": ds.get_most_banned_states,
        "most_banned_titles": ds.get_most_banned_titles,
    }

    for user_option, corresponding_function in cl_map.items():
        user_input = getattr(args, user_option)
        if user_input is not None:
            search_results = corresponding_function(user_input)
            if search_results:
                for result in search_results:
                    print(result)
                break
            print("No results found")
            break
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
