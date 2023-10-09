DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;

CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name text,
        cohort int
    );