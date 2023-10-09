from lib.item import Item

class ItemRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM items")
        items = [Item(row['id'], row['name'], row['unit_price'], row['quantity']) for row in rows]
        return items
    
    def create(self, item):
        self._connection.execute('INSERT INTO items (name, unit_price, quantity) VALUES (%s, %s, %s)', [item.name, item.unit_price, item.quantity])
        return None
    # INSERT INTO items (name, unit_price, quantity) VALUES ('cup', 2.39, 30);
    # def create(self, artist):
    #     self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [artist.name, artist.genre])
    #     return None