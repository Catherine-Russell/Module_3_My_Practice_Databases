from lib.posts_repo import PostRepository
from lib.posts import Post
from lib.comments import Comment

def test_all(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)
    result = repository.all()
    assert result == [
        Post(1, 'first post', 'This is my first post'),
        Post(2, 'second post', 'This is my second post'),
        Post(3, 'hello world', 'How are you today?'),
        Post(4, 'Toast', 'Here is a photo of my delicious dinner'),
    ]

def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog.sql")
    repository = PostRepository(db_connection)
    result = repository.find_with_comments(1)
    assert result == Post(1, 'first post', 'This is my first post', [
        Comment(1, 'congratulations', 'cat', 1),
        Comment(2, 'fantastic', 'tom', 1)
        ])