# 1. Extract nouns from the user stories or specification
    As a shop manager
    So I can know which items I have in stock
    I want to keep a list of my shop items with their name and unit price.

    As a shop manager
    So I can know which items I have in stock
    I want to know which quantity (a number) I have for each item.

    As a shop manager
    So I can manage items
    I want to be able to create a new item.

    As a shop manager
    So I can know which orders were made
    I want to keep a list of orders with their customer name.

    As a shop manager
    So I can know which orders were made
    I want to assign each order to their corresponding item.

    As a shop manager
    So I can know which orders were made
    I want to know on which date an order was placed. 

    As a shop manager
    So I can manage orders
    I want to be able to create a new order.

        NOUNS = items, name, unit_price, quantity, customer name, order_placed orders

# 2. Infer the Table name and columns
    items - name, unit_price, quantity
    orders - customer_name, date_placed

# 3. Decide the column types
    items 
        id SERIAL PRIMARY KEY
        name VARCHAR(255)
        unit_price decimal(3, 2)
        quantity int

    orders
        id SERIAL PRIMARY KEY
        customer_name VARCHAR(255)
        date_placed date YYYY-MM-DD

# 4. Decide on tables' relationships
    Can one order have many items? (Yes)
    Can one item have many orders? (YES)

    a item has many orders
    And on the other side, an item belongs to an order
    In that case, the foreign key is in the table students

# 5. Write the SQL to create a file (in SQL file)
    CREATE TABLE items (
        id SERIAL PRIMARY KEY
        name VARCHAR(255)
        unit_price decimal(3, 2)
        quantity int
    );

    CREATE TABLE orders (
        id SERIAL PRIMARY KEY
        customer_name VARCHAR(255)
        date_placed date
    );

    CREATE TABLE orders_items (
        order_id int
        item_id int
        CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
        CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE
        PRIMARY KEY (order_id, item_id)
    );

# 6. Create the table and link to the database (in terminal)
    
    
