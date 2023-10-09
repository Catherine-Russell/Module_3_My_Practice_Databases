from lib.posts import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_by_tag(self, tag):
        rows = self._connection.execute("SELECT posts.id, posts.title FROM posts JOIN posts_tags ON posts.id = posts_tags.post_id JOIN tags ON tags.id = posts_tags.tag_id WHERE tags.name = %s", [tag])
        posts = [Post(row['id'], row['title']) for row in rows]
        return posts