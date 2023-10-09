from lib.item import Item

def test_item_constructs():
    item = Item(1, 'cup', 2.39, 30)
    assert item.id == 1
    assert item.name == "cup"
    assert item.unit_price == 2.39
    assert item.quantity == 30

def test_items_format_niceley():
    item = Item(1,  'cup', 2.39, 30)
    assert str(item) == "Item 1: cup, £2.39, 30 left in stock"

def test_items_are_equal():
    item1 = Item(1, "name", 1.00, 10)
    item2 = Item(1, "name", 1.00, 10)
    assert item1 == item2
