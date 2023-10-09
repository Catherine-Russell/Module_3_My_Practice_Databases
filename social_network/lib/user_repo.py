from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email_address"])
            users.append(item)
        return users
    
    def create(self, user):
        self._connection.execute("INSERT INTO users (username, email_address) VALUES(%s, %s)", [user.username, user.email_address])
        return None
    
    def delete(self, user_id):
        self._connection.execute("DELETE FROM users WHERE id = %s", [user_id])
        return None