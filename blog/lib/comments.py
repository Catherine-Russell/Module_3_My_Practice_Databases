class Comment:
    def __init__(self, id, contents, author, post_id):
        self.id = id
        self.contents = contents
        self.author = author
        self.post_id = post_id

    def __repr__(self):
        return f"Comment({self.id}, {self.contents}, {self.author}, {self.post_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__