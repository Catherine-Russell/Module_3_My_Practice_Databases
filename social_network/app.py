from lib.database_connection import DatabaseConnection


# connect to database
connection = DatabaseConnection()
connection.connect()

# seed database
connection.seed("seeds/book_store.sql")
