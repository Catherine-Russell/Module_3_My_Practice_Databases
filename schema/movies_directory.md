# 1. Extract nouns from the user stories or specification

    As a person who loves movies,
    So I can list all my favourite movies
    I want to see a list of movies' titles.

    As a person who loves movies,
    So I can list all my favourite movies
    I want to see a list of movies' genres.

    As a person who loves movies,
    So I can list all my favourite movies
    I want to see a list of movies' release years.

        NOUNS:
        - movies
        - titles
        - genres
        - release_years


# 2. Infer the Table name and columns
        record      | properties
        movie       | title, genre, release_year

    name of table = movies
    column names = title, genre, release_year

# 3. Decide the column types
    id = SERIAL
    title = test
    genre = text
    release_year = int
    

# 4. Write the SQL to create a file (in SQL file)
    file = movies.sql

    CREATE TABLE movies (
        id SERIAL PRIMARY KEY,
        title text,
        genre text,
        release_year int
    );

# 5. Create the table and link to the database (in terminal)
    psql -h 127.0.0.1 movies_directory < movies.sql