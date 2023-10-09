from lib.order_repository import OrderRepository
from lib.order import Order
from lib.item import Item
import pytest

def test_all_orders(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    results = repository.all()
    results_as_string = [str(order) for order in results]
    assert results_as_string == [
        "Order 1: Customer = Lizzie, Date ordered = 2022-11-07, items purchased = ['fork (£1.25)', 'bin (£12.65)']",
        "Order 2: Customer = Tom, Date ordered = 2023-08-30, items purchased = ['cup (£2.39)', 'knife (£8.97)']",
        "Order 3: Customer = Cat, Date ordered = 2020-04-12, items purchased = ['knife (£8.97)', 'spatula (£5.24)', 'bin (£12.65)']",
    ]

# @pytest.mark.skip (reason = "I don't know how to get this to work")
def test_create_order(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    repository.create(Order(4, 'Chris', '2021-05-15'), [1, 3])
    results = repository.all()
    results_as_string = [str(order) for order in results]
    assert results_as_string == [
        "Order 1: Customer = Lizzie, Date ordered = 2022-11-07, items purchased = ['fork (£1.25)', ('bin (£12.65)']",
        "Order 2: Customer = Tom, Date ordered = 2023-08-30, items purchased = ['cup (£2.39)', 'knife (£8.97)']",
        "Order 3: Customer = Cat, Date ordered = 2020-04-12, items purchased = ['knife (£8.97)', 'spatula (£5.24), 'bin (£12.65)']",
        "Order 4: Customer = Chris, Date ordered = 2021-05-15, items purchased = ['cup (£2.39)', 'knife (£8.97)'] "
    ]
