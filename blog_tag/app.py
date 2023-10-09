from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository

connection = DatabaseConnection()
connection.connect()

connection.seed("seeds/book_store.sql")

repository = PostRepository(connection)

repository.find_by_tag('coding')