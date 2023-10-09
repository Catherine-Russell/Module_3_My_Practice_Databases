# Welcome to the shop management program!

# What do you want to do?
#   1 = list all shop items COMPLETE
#   2 = create a new item
#   3 = list all orders
#   4 = create a new order

# 1 [enter]

# Here's a list of all shop items:

#  #1 Super Shark Vacuum Cleaner - Unit price: 99 - Quantity: 30
#  #2 Makerspresso Coffee Machine - Unit price: 69 - Quantity: 15
#  (...)

from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository
from lib.item import Item
from lib.order import Order
from datetime import datetime
# from lib.order_repository import OrderRepository

class Application:
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/shop_manager.sql")

"""
make separate 
make order - saves order number
add item to order
(could add order to existing order)

"""

    def run(self):
        print("Welcome to the shop management program!")
        selection = input("Select a number:\n   1 = list all shop items\n   2 = create a new item\n   3 = list all orders\n   4 = create a new order\n")

        if selection == '1':
            repository = ItemRepository(self.connection)
            items = repository.all()
            for item in items:
                print(item)

        elif selection == '2':
            repository = ItemRepository(self.connection)
            name = input("What is the new item? ")
            unit_price = float(input(f"What is the unit price per {name}? "))
            quantity = int(input(f"How many {name}s are there in stock? "))
            new_item = Item(None, name, unit_price, quantity)
            repository.create(new_item)
            items = repository.all()
            for item in items:
                print(item)

        elif selection == '3':
            repository = OrderRepository(self.connection)
            orders = repository.all()
            for order in orders:
                print(order)

        elif selection == '4':
            order_repo = OrderRepository(self.connection)
            item_repo = ItemRepository
            order_complete = False
            items_in_stock = item_repo.all()
            my_basket = []
            while not order_complete:
                item_to_order = input(f"What item would you like to order?(type the corresponding number)\n {items_in_stock}\n")
                if int(item_to_order) > len(items) or int(item_to_order) < 0:
                    print("Invalid selection")
                    continue
                else:
                    my_basket.append(int(item_to_order))
                    complete = input("Is your order complete?")
            elif complete.lower() == 'yes':
                order_repo.create_order(new_order)


            
            customer_name = input("What is the name of the customer? ")
            date = datetime.date(datetime.now())
            new_order = Item(None, customer_name, date.strftime("%Y-%m-%d"))


if __name__ == '__main__':
    app = Application()
    app.run()
