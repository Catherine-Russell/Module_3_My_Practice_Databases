from lib.post import Post
from lib.post_repo import PostRepository

def test_get_all(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Post(1, 'first post', 'This is my first post', 5, 1),
        Post(2, 'second post', 'This is my second post', 10, 1),
        Post(3, 'hello world', 'How are you today?', 100, 2),
        Post(4, 'Toast', 'Here is a photo of my delicious dinner', 43, 2),
        Post(5, 'databases', 'challenging at first but got better', 79, 2),
        Post(6, 'hello everyone', 'This is my first post', 99, 3),
        Post(7, 'Thursday post', 'Today is thurday', 83, 3),
        ]
    
def test_create(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    post = Post(8, 'Friday post', 'I stayed in pjs all day', 129, 2)
    assert repository.create(post) == None
    posts = repository.all()
    assert posts == [
        Post(1, 'first post', 'This is my first post', 5, 1),
        Post(2, 'second post', 'This is my second post', 10, 1),
        Post(3, 'hello world', 'How are you today?', 100, 2),
        Post(4, 'Toast', 'Here is a photo of my delicious dinner', 43, 2),
        Post(5, 'databases', 'challenging at first but got better', 79, 2),
        Post(6, 'hello everyone', 'This is my first post', 99, 3),
        Post(7, 'Thursday post', 'Today is thurday', 83, 3),
        Post(8, 'Friday post', 'I stayed in pjs all day', 129, 2)
    ]

def test_delete(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)
    repository.delete(5)
    posts = repository.all()
    assert posts == [
        Post(1, 'first post', 'This is my first post', 5, 1),
        Post(2, 'second post', 'This is my second post', 10, 1),
        Post(3, 'hello world', 'How are you today?', 100, 2),
        Post(4, 'Toast', 'Here is a photo of my delicious dinner', 43, 2),
        Post(6, 'hello everyone', 'This is my first post', 99, 3),
        Post(7, 'Thursday post', 'Today is thurday', 83, 3),
    ]