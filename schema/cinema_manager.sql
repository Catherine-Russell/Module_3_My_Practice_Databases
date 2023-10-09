CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_date date
);

CREATE TABLE cinemas (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255)
);

CREATE TABLE students_tags (
    film_id int,
    cinema_id int,
    CONSTRAINT fk_film FOREIGN KEY (film_id) REFERENCES films(id) ON DELETE CASCADE,
    CONSTRAINT fk_cinema FOREIGN KEY (cinema_id) REFERENCES cinemas(id) ON DELETE CASCADE
);