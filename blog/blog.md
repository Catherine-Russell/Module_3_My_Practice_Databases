# 1. Extract nouns from user stories
    As a blogger
    So I can write interesting stuff
    I want to write posts having a title.

    As a blogger
    So I can write interesting stuff
    I want to write posts having a content.

    As a blogger
    So I can let people comment on interesting stuff
    I want to allow comments on my posts.

    As a blogger
    So I can let people comment on interesting stuff
    I want the comments to have a content.

    As a blogger
    So I can let people comment on interesting stuff
    I want the author to include their name in comments.

    
        NOUNS = posts, blog_title, blog_content, comments, comment_content, comment_author
        


# 2. Infer table names and columns
    table 1 = blog_posts
        columns = title, content, comments
    
    table 2 = comments
        columns = comment_content, author
    
    

# 3. decide column types
    Table 1: blog_posts
        title VARCHAR(255)
        content text
        X comments text
    
    Table 2:
        comment_content text
        author VARCHAR(255)
        affiliated post foreign key

# 4. Decide on tables' relationships
    Can one post have many comments? (Yes)
    Can one comment have many posts? (No)

    a post has many comments
    And on the other side, a comment belongs to a post
    In that case, the foreign key is in the table comments
        (fk on the one which belongs to the other)

# 5. Write the SQL
    CREATE TABLE blog_posts (
        id SERIAL PRIMARY KEY
        title VARCHAR(255)
        contents text
    );

    CREATE TABLE comments (
        id SERIAL PRIMARY KEY
        contents text
        author VARCHAR (255)
        blog_post_id int
        constraint fk_blog_post foreign key (blog_post_id) references blog_posts(id)
            on delete cascade
    );


# 6. Create the tables
