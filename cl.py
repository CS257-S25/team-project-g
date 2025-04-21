'''
The eventual location for the command line interface (CLI) for the project.
This will be the entry point for the project when run from the command line.
'''
import sys
import argparse
from ProductionCode.search import search_title, search_author, search_genre
from ProductionCode.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles)


def main():
    """Main function for the command line interface (CLI) for the project."""
    parser = argparse.ArgumentParser(
        # The command line interface (CLI) for the project.
                prog="cl.py",
                description="Command line interface for the project",
                epilog="This is the command line interface for the project.",
                usage="%(prog)s [options] [args]")
    parser.add_argument(
        #Search for a title in the database
                        "--search-title",
                        "--st",
                        "-st",
                        help="Search for a title in the database",
                        type=str,
                        metavar="TITLE")
    parser.add_argument(
        #Search for an author in the database
                        "--search-author",
                        "--sa",
                        "-sa",
                        help="Search for an author in the database",
                        type=str,
                        metavar="AUTHOR")
    parser.add_argument(
        #Search for a genre in the database
                        "--search-genre",
                        "--sg",
                        "-sg",
                        help="Search for a genre in the database",
                        type=str,
                        metavar="GENRE")
    parser.add_argument(
        #Get the most banned districts in the database
                        "--most-banned-districts",
                        "--mbd",
                        "-mbd",
                        help="Get the most banned districts in the database",
                        type=int,
                        metavar="LIMIT")
    parser.add_argument(
        #Get the most banned authors in the database
                        "--most-banned-authors",
                        "--mba",
                        "-mba",
                        help="Get the most banned authors in the database",
                        type=int,
                        metavar="LIMIT")
    parser.add_argument(
        #Get the most banned states in the database
                        "--most-banned-states",
                        "--mbs",
                        "-mbs",
                        help="Get the most banned states in the database",
                        type=int,
                        metavar="LIMIT")
    parser.add_argument(
        #Get the most banned titles in the database
                        "--most-banned-titles",
                        "--mbt",
                        "-mbt",
                        help="Get the most banned titles in the database",
                        type=int,
                        metavar="LIMIT")
    args = parser.parse_args()
    if args.search_title:
        search_results = search_title(args.search_title)
        for result in search_results:
            print(result)
    elif args.search_author:
        search_results = search_author(args.search_author)
        for result in search_results:
            print(result)
    elif args.search_genre:
        search_results = search_genre(args.search_genre)
        for result in search_results:
            print(result)
    elif args.most_banned_districts:
        search_results = most_banned_districts(args.most_banned_districts)
        for result in search_results:
            print(result)
    elif args.most_banned_authors:
        search_results = most_banned_authors(args.most_banned_authors)
        for result in search_results:
            print(result)
    elif args.most_banned_states:
        search_results = most_banned_states(args.most_banned_states)
        for result in search_results:
            print(result)
    elif args.most_banned_titles:
        search_results = most_banned_titles(args.most_banned_titles)
        for result in search_results:
            print(result)
    # If no arguments are provided, print the help message
    else:
        parser.print_help()
        sys.exit(1)
if __name__ == "__main__":
    main()
# The command line interface (CLI) for the project.