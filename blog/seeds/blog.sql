DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    contents text
    );

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    contents text,
    author VARCHAR (255),
    post_id int,
    constraint fk_post foreign key (post_id)references posts(id)
        on delete cascade
    );

-- Finally, we add any records that are needed for the tests to run
INSERT INTO posts (title, contents) VALUES ('first post', 'This is my first post');
INSERT INTO posts (title, contents) VALUES ('second post', 'This is my second post');
INSERT INTO posts (title, contents) VALUES ('hello world', 'How are you today?');
INSERT INTO posts (title, contents) VALUES ('Toast', 'Here is a photo of my delicious dinner');

INSERT INTO comments (contents, author, post_id) VALUES ('congratulations', 'cat', 1);
INSERT INTO comments (contents, author, post_id) VALUES ('fantastic', 'tom', 1);
INSERT INTO comments (contents, author, post_id) VALUES ('getting a bit old now', 'lizzie', 2);
INSERT INTO comments (contents, author, post_id) VALUES ('been better', 'Stella', 3);
INSERT INTO comments (contents, author, post_id) VALUES ('Im ok', 'Pip', 3);
INSERT INTO comments (contents, author, post_id) VALUES ('tired', 'Tina', 3);
INSERT INTO comments (contents, author, post_id) VALUES ('looks tasty', 'Ben', 4);