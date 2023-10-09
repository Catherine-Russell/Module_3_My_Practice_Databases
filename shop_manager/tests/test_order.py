from lib.order import Order

def test_order_constructs():
    order = Order(1, 'Lizzie', '2022-11-07')
    assert order.id == 1
    assert order.customer_name == "Lizzie"
    assert order.date_placed == '2022-11-07'

def test_orders_format_niceley():
    order = Order(1,  'Lizzie', '2022-11-07')
    assert str(order) == "Order 1: Customer = Lizzie, Date ordered = 2022-11-07, items purchased = []"

def test_orders_are_equal():
    order1 = Order(1, "name", '2000-01-01')
    order2 = Order(1, "name", '2000-01-01')
    assert order1 == order2
