class Order:
    def __init__(self, id, customer_name, date_placed):
        self.id = id
        self.customer_name = customer_name
        self.date_placed = date_placed
        self.items = []

    def __repr__(self):
        return f"Order {self.id}: Customer = {self.customer_name}, Date ordered = {self.date_placed}, items purchased = {self.items}"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__