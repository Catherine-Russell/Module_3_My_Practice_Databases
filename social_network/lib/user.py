class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email_address = email

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email_address})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__