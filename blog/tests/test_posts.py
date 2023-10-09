from lib.posts import Post


def test_post_constructs_with_attributes():
    post = Post(1, 'first post', 'This is my first post')
    assert post.id == 1
    assert post.title == 'first post'
    assert post.contents == 'This is my first post'
    assert post.comments == []

def test_posts_format_prettily():
    post = Post(1, 'first post', 'This is my first post')
    assert str(post) == "Post(1, first post, This is my first post, [])" 

def test_posts_are_equal():
    post1 = Post(1, 'first post', 'This is my first post')
    post2 = Post(1, 'first post', 'This is my first post')
    assert post1 == post2