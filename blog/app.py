from lib.database_connection import DatabaseConnection
from lib.posts_repo import PostRepository

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/blog.sql")

post_repository = PostRepository(connection)

# all_posts = post_repository.all()
# for post in all_posts:
#     print(post)

post1 = post_repository.find_with_comments(1)
post2 = post_repository.find_with_comments(2)
post3 = post_repository.find_with_comments(3)
post4 = post_repository.find_with_comments(4)

print(f"Post 1 = {post1}")
print(f"Post 2 = {post2}")
print(f"Post 3 = {post3}")
print(f"Post 4 = {post4}")