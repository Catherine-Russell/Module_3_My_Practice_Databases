from lib.item_repository import ItemRepository
from lib.item import Item
import pytest

def test_all_items(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    result = repository.all()
    result_as_str = [str(item) for item in result]
    assert result_as_str == [
        'Item 1: cup, £2.39, 30 left in stock',
        'Item 2: fork, £1.25, 55 left in stock',
        'Item 3: knife, £8.97, 41 left in stock',
        'Item 4: spatula, £5.24, 18 left in stock',
        'Item 5: bin, £12.65, 61 left in stock',
    ]

def test_create_item(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = ItemRepository(db_connection)
    item = Item(6, 'coffee pot', 24.30, 100)
    repository.create(item)
    result = repository.all()
    result_as_str = [str(item) for item in result]
    assert result_as_str == [
        'Item 1: cup, £2.39, 30 left in stock',
        'Item 2: fork, £1.25, 55 left in stock',
        'Item 3: knife, £8.97, 41 left in stock',
        'Item 4: spatula, £5.24, 18 left in stock',
        'Item 5: bin, £12.65, 61 left in stock',
        'Item 6: coffee pot, £24.30, 100 left in stock'
    ]

