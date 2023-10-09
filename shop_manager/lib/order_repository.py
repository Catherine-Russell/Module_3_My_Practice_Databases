from lib.order import Order
from lib.item import Item
class OrderRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT orders.id, orders.customer_name, orders.date_placed, items.name, items.unit_price, items.quantity FROM orders JOIN orders_items ON orders.id = orders_items.order_id JOIN items ON orders_items.item_id = items.id")
        orders = []
        order_number = 0
        for row in rows:
            if row['id'] > order_number:
                order = Order(row['id'], row['customer_name'], row['date_placed'])
                item = f"{row['name']} (£{row['unit_price']})"
                order.items.append(item)
                order_number = int(row['id'])
                orders.append(order)
            elif row['id'] == order_number:
                item = f"{row['name']} (£{row['unit_price']})"
                order.items.append(item)
        return orders


    def create_order(self, order, items):            
        self._connection.execute("INSERT INTO orders(customer_name, date_placed) VALUES (%s, %s)", [order.customer_name, order.date_placed] "SELECT id = SCOPE_IDENTITY()")
        for item in items:
            self._connection.execute("INSERT INTO orders_items () VALUES (%s, %s)", [order.customer_name, order.date_placed])
        return None



# "Order 1: Customer = Lizzie, Date ordered = 2022-11-07, items purchased = ['cup (£2.39)', ('bin (£12.65)']",