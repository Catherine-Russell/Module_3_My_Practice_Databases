# 1. Extract nouns from user stories
    As a social network user,
    So I can have my information registered,
    I'd like to have a user account with my email address.

    As a social network user,
    So I can have my information registered,
    I'd like to have a user account with my username.

    As a social network user,
    So I can write on my timeline,
    I'd like to create posts associated with my user account.

    As a social network user,
    So I can write on my timeline,
    I'd like each of my posts to have a title and a content.

    As a social network user,
    So I can know who reads my posts,
    I'd like each of my posts to have a number of views.

        NOUNS = user account, email address, username, posts, post_title, post_content, post_views


# 2. Infer table names and columns
    table 1 = users
        columns = email address, username

    table 2 = posts
        columns = post_title, post_content, post_views



# 3. decide column types
    Table 1: users
        id SERIAL PRIMARY KEY
        username VARCHAR (255)
        email_address VARCHAR(255)

    Table 2: posts
        id SERIAL PRIMARY KEY,
        title = VARCHAR(255)
        content test
        views int
        user_id foreign key
        

# 4. Decide on tables' relationships
    Can one user have many posts? (Yes)
    Can one post have many users? (No)

    a user has many posts
    And on the other side, a post belongs to a user
    In that case, the foreign key is in the table posts
        (fk on the one which belongs to the other)

# 5. Write the SQL
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255),
        email_address VARCHAR(255)
    );

    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        content text,
        views int
        user_id int
        constraint fk_user foreign key(user_id) references users(id)
            on delete cascade
    );


# 6. Create the tables
