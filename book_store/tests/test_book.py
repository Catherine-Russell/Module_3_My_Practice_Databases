from lib.book import Book

def test_book_constructs_with_attributes():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'

def test_books_format_prettily():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book) == "Book(1, Nineteen Eighty-Four, George Orwell)" 

def test_books_are_equal():
    book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    book2 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book1 == book2