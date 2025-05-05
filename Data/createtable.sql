DROP TABLE IF EXISTS bookbans;
CREATE TABLE bookbans (
    isbn int,
    ban_state text,
    ban_district text,
    ban_year int,
    ban_month int,
    ban_status text,
    ban_origin text
);

DROP TABLE IF EXISTS books;
CREATE TABLE books (
    isbn int,
    title text,
    author text[],
    summary text,
    cover text,
    genres text[],
    publish_year date
);

DROP TABLE IF EXISTS bookreviews;
CREATE TABLE bookreviews (
    isbn int,
    review_id int,
    review_title text,
    review_text text,
    review_rating int,
    review_date date,
    review_user text
);

DROP TABLE IF EXISTS datasources;
CREATE TABLE datasources (
    search_author text,
    search_title_like text,
    search_genre text,
    get_bans_per_year text,
    get_most_common_words text,
    get_most_banned_authors text,
    get_keyword text,
    get_most_banned_districts text,
    get most_banned_states text,
    get most_banned_titles text
);