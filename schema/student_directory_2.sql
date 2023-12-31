DROP TABLE IF EXISTS cohortss;
DROP TABLE IF EXISTS students;


CREATE TABLE cohorts (
    id SERIAL PRIMARY KEY,
    cohort_name text,
    starting_date date
);

-- Then the table with the foreign key second.
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_name text,
-- The foreign key name is always {other_table_singular}_id
    cohort_id int,
    constraint fk_cohort foreign key(cohort_id)references cohorts(id)
    on delete cascade
);