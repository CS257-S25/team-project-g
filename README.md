# The Forbidden Library
See various information about banned books.

## Usage

```
usage: cl.py [options] [args]

Command line interface for the project

options:
  -h, --help            show this help message and exit
  --search-title, --st, -st TITLE
                        Search for a title in the database
  --search-author, --sa, -sa AUTHOR
                        Search for an author in the database
  --search-genre, --sg, -sg GENRE
                        Search for a genre in the database
  --most-banned-districts, --mbd, -mbd LIMIT
                        Get the most banned districts in the database
  --most-banned-authors, --mba, -mba LIMIT
                        Get the most banned authors in the database
  --most-banned-states, --mbs, -mbs LIMIT
                        Get the most banned states in the database
  --most-banned-titles, --mbt, -mbt LIMIT
                        Get the most banned titles in the database
```

## Usability Principles

### Scanability
Our website uses clear headings, concise labels, and organized layouts to help users quickly find relevant information. Search results and data tables are formatted for easy scanning, allowing users to identify key details at a glance.

### Satisficing
We provide straightforward search and filter options so users can efficiently get useful results without needing to explore every feature. The interface is designed to help users accomplish their goals with minimal effort.

### Muddling Through
The navigation and controls are forgiving, allowing users to try different searches or filters without penalty. Users can experiment with commands and options, learning the system as they go, and easily recover from mistakes.

Made by Joe Borncamp, Cooper Evans, Devin Gulliver, Marco Pina

## Design Improvements

### Code Design
Repeated Code
- Originally in our books, genres, authors pages, we used the same book cover html and css. Now, we moved it into a separate template so we repeat our code less.
Design Pattern: Strategies
- Originally we had repeated code for displaying different variations of our maps. Now, we refactored it to use use strategies so it is easy to specify with type of map we want to use for each page
### Front End Design
Improved link color for visibility
- Our link colors previously used a dark blue, we changed to a light blue to increase readability on dark background
