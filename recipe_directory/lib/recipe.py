class Recipe():
    def __init__(self, id, dish, average_cooking_time, rating):
        if rating < 0 or rating > 5:
            raise Exception("rating must be between 0 and 5")
        self.id = id
        self.dish = dish
        self. average_cooking_time = average_cooking_time
        self.rating = rating
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.dish}, {self.average_cooking_time}, {self.rating})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__