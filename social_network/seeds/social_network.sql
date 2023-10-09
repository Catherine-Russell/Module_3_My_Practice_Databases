DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    email_address VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content text,
    views INTEGER,
    user_id INTEGER,
    constraint fk_user foreign key(user_id) references users(id)
        on delete cascade
);



-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (username, email_address) VALUES ('abc123', 'abc123@gmail.com');
INSERT INTO users (username, email_address) VALUES ('crussell', 'crussell@gmail.com');
INSERT INTO users (username, email_address) VALUES ('lizzie95', 'lizzie95@gmail.com');


INSERT INTO posts (title, content, views, user_id) VALUES ('first post', 'This is my first post', 5, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('second post', 'This is my second post', 10, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('hello world', 'How are you today?', 100, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Toast', 'Here is a photo of my delicious dinner', 43, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('databases', 'challenging at first but got better', 79, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('hello everyone', 'This is my first post', 99, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('Thursday post', 'Today is thurday', 83, 3);


