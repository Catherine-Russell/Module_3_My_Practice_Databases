from lib.posts import Post
from lib.comments import Comment

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = [Post(row['id'], row['title'], row['contents']) for row in rows]
        return posts
    
    def find_with_comments(self, post_id):
        rows = self._connection.execute("SELECT posts.id, posts.title, posts.contents, comments.id, comments.contents AS comment_contents, comments.author, comments.post_id FROM posts JOIN comments ON posts.id = comments.post_id WHERE posts.id = %s", [post_id])
        comments = []
        for row in rows:
            item = Comment(row['id'], row['comment_contents'], row['author'], row['post_id'])
            comments.append(item)
        return Post(rows[0]['id'], rows[0]['title'], rows[0]['contents'], comments)