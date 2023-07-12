Single Table Design Recipe Template
Copy this recipe template to design and create a database table from a specification.

# Request:
POST /albums

# With body parameters:
title=Voyage
release_year=2022
artist_id=2

# Expected response (200 OK)
(No content)



1. Extract nouns from the user stories or specification
# EXAMPLE USER STORY:
# (analyse only the relevant part - here, the final line).

Nouns:

albun,
title,
release year,
artist,
id



Nouns:

album, title, release year


2. Infer the Table Name and Columns
Put the different nouns in this table. Replace the example with your own nouns.

Record	          Properties
album	   id, title, release year artist_id



Name of the table (always plural): albums

Column names: title, release_year, artist_id, id

3. Decide the column types
Here's a full documentation of PostgreSQL data types.

Most of the time, you'll need either text, int, bigint, numeric, or boolean. If you're in doubt, do some research or ask your peers.

Remember to always have the primary key id as a first column. Its type will always be SERIAL.

# EXAMPLE:

id: SERIAL
title: text
release_year: int
artist_id: int


4. Write the SQL
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, columm names and types.

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title text,
  release_year int,
  artist_id int
);




5. Create the table
psql -h 127.0.0.1 database_name < albums_table.sql