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

#### Map
Design Pattern: Strategies
- Originally we had repeated code for displaying different variations of our maps. Now, we refactored it to use use strategies so it is easy to specify with type of map we want to use for each page
- `static/map.js`
#### Search
Design Pattern: Decorators
- We added decorators to extend the functionality of searching, this has allowed the easy addition of new search types and modifications
- `ProductionCode.search_decorators.py`
Design Pattern: Strategies
- Originally, the search method was tightly coupled with endpoint function, making it difficult to make changes. We added strategies for searching based on the search type. This makes the code much simpler and adheres to the principle of one layer of abstracion.
- `ProductionCode.search_strategies.py`
#### DataSource method names
Originally, the method names of our DataSource class were inconsistent. Some used verb phrases, some did not. Some referred to Bookban objects as bans while others referred to them as bookbans. Here are a few examples of lines were methods were changed to adhere to good naming principles:
- `ProductionCode.datasource.py:72` : `_database_row_list_to_bookban_list` -> `_create_bookbans_from_rows`
  - Before, the method name was very wordy and had gratuitous context (the method is in the datasource class, of course the row is for a database)
  - Type was also encoded in a clunky and unnecessary way as we now explicitly type the return values of these methods
  - Similar changes were made to other methods that created objects from database rows.
-  `ProductionCode.datasource.py:141` : `book_from_isbn` -> `get_book_from_isbn`
  - Adding the get prefix, emphasizes that the method is retrieving the data from somewhere.
  - This also turns the method name into a verb phrase
### Front End Design
#### Accessiblity
Improved link color for visibility
- `static/global.css`
- Our link colors previously used a dark blue, we changed to a light blue to increase readability on dark background
#### Usability
Improved Search Functionality
- `app.py:78`
- Originally, our search feature only displayed books that matched a searched title, author, or isbn number. Now, when the user searches for an author, a result for the authors page shows up rather than the books they wrote. The same functionality was added for genres.
- Another improvement we made to the search feature was adding a dropdown to access a search type from the search bar.
-Another added improvement was adding a more specific placeholder in the search box for users. This makes it easier for users to know what to search.
Improved Navigation Bar Functionality
- `templates/nav.html`
- User's were struggling to click the menu buttons in the nav bar. We made the boxes easier to click for ease of access.

About page
- `templates/about.html`
- We added an about page to give the user some background on what we see on our webpage, improving usability
