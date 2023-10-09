CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    emotion VARCHAR(255)
);

CREATE TABLE students_tags (
    student_id int,
    tag_id int,
    CONSTRAINT fk_student FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE,
    CONSTRAINT fk_tag FOREIGN KEY(tag_id) REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (student_id, tag_id)
);

--  post_id int,
--   tag_id int,
--   constraint fk_post foreign key(post_id) references posts(id) on delete cascade,
--   constraint fk_tag foreign key(tag_id) references tags(id) on delete cascade,
--   PRIMARY KEY (post_id, tag_id)