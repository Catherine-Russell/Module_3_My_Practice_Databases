class Item:
    def __init__(self, id, name, unit_price, quantity):
        self.id = id
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity
        

    def __repr__(self):
        return f"Item {self.id}: {self.name}, £{self.unit_price}, {self.quantity} left in stock"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__