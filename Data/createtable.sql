DROP TABLE IF EXISTS bookbans;
CREATE TABLE bookbans (
    isbn text,
    ban_state text,
    ban_district text,
    ban_year int,
    ban_month int,
    ban_status text,
    ban_origin text
);

DROP TABLE IF EXISTS books;
CREATE TABLE books (
    isbn text,
    title text,
    authors text[],
    summary text,
    cover text,
    genres text[],
    publish_date date,
    rating real 
);
