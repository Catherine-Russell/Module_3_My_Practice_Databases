1. Extract nouns from the user stories or specification

    As a coach
    So I can get to know all students
    I want to see a list of students' names.

    As a coach
    So I can get to know all students
    I want to see a list of students' cohorts.

        NOUNS:
        - students
        - names
        - cohorts


2. Infer the Table name and columns
        record      | properties
        students    | name, cohort

    name of table = students
    column names = name, cohort

3. Decide the column types
    id = SERIAL
    name = text
    cohort = int (year)

4. Write the SQL to create a file
    file = student_directory.sql

    CREATE TABLE students (
        id SERIAL PRIMARY KEY,
        name text,
        cohort int
    );

5. Create the table and link to the database (skip)
    psql -h 127.0.0.1 schema_practice < student_directory.sql