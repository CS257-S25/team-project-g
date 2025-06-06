# Project Proposal

### Working Title
The Forbidden Library

### Summary
We are primarily working with a database on banned books from PEN America. This database includes variables on Title, Author, State, District, Date of Challenge, Ban Status, and Instantiating Action. Additionally, we will be comparing this to another database using information from Goodreads. This database has information of genre, description, rating and much more information on each book.



### Metadata
- URLs:
  - https://pen.org/book-bans/pen-america-index-of-school-book-bans-2023-2024/
  - https://pen.org/book-bans/2023-banned-book-list/
  - https://pen.org/book-bans/banned-book-list-2021-2022/
- Date downloaded: 7 April 2025
- Authorship: PEN America
- Exact name and version: PEN America Index of School Book Bans - 2021-2024
- Terms of Use: Dataset is open access; no license is stated.
- Generated Citation:
  - PEN America. (2024, November). *PEN America Index of School Book Bans – 2023-2024.* https://pen.org/book-bans/pen-america-index-of-school-book-bans-2023-2024/ 

### User Stories and Acceptance Criteria
As a reader, I can search for a book by title and see all associated information so that I can see what types of books have been banned.
- Able to search by title
- Display author/book cover/genre/rating/ban status/summary/rating
- If the book is not found the user sees “No results found”

As a user, I can sort banned books by genre, content type, and district so I can see what type is banned in specific categories and areas.
- Able to sort/filter books by genre, content type, and district
- Able to combine filters (e.g Genre + District)
- Display books that meet the criteria of selected choice
- Display district/ban status/title/author/genre
- If a book does not match criteria then the user sees “No results found”

As a researcher, I can choose a book/district/genre and get the top X most banned books/districts/categories so I can see who/what is most affected by book bans.
- Able to choose a book/district/genre
- Displays subcategory in a sorted list by number of bans (Ex: if genre is chosen, display banned genres in a sorted order)
- Displays number of bans for each subcategory
