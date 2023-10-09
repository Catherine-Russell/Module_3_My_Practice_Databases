# 1. Extract nouns from the user stories or specification
    As a cinema company manager,
    So I can keep track of movies being shown,
    I want to keep a list of movies with their title and release date.

    As a cinema company manager,
    So I can keep track of movies being shown,
    I want to keep a list of my cinemas with their city name (e.g 'London' or 'Manchester').

    As a cinema company manager,
    So I can keep track of movies being shown,
    I want to be able to list which cinemas are showing a specific movie.

    As a cinema company manager,
    So I can keep track of movies being shown,
    I want to be able to list which movies are being shown a specific cinema.

        NOUNS = movies, title, release_date, cinemas, city_name, movies

# 2. Infer the Table name and columns
    movies
    cinemas

# 3. Decide the column types
    movies:
        id = serial
        title VARCHAR(255)
        release_date - date
    cinemas:
        id = serial
        city = VARCHAR

    join:
        movie_id = int
        cinema_id = int

# 4. Decide on tables' relationships
    many to many


# 5. Write the SQL to create a file (in SQL file)
    CREATE TABLE films (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        release_date date,
    );

    CREATE TABLE cinemas (
        id = SERIAL PRIMARY KEY,
        city = VARCHAR(255),
    );

    CREATE TABLE students_tags (
        film_id int,
        cinema_id int,
        CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES films(id) ON DELETE CASCADE,
        CONSTRAINT fk_cinema FOREIGN KEY (cinema_id) REFERENCES cinemas(id) ON DELETE CASCADE
    );

# 6. Create the table and link to the database (in terminal)
    
    
