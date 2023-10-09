from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM posts")
        posts = [Post(row['id'], row["title"], row["content"], row["views"], row["user_id"]) for row in rows]
        return posts
    
    def create(self, post):
        self._connection.execute("INSERT INTO posts(id, title, content, views, user_id) VALUES (%s, %s, %s, %s, %s)", [post.id, post.title, post.content, post.views, post.user_id])
        return None
    
    def delete(self, user_id):
        self._connection.execute("DELETE FROM posts WHERE id = %s", [user_id])
        return None