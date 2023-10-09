DROP TABLE IF EXISTS items CASCADE;
DROP SEQUENCE IF EXISTS items_id_seq;
DROP TABLE IF EXISTS orders CASCADE;
DROP SEQUENCE IF EXISTS orders_id_seq;
DROP TABLE IF EXISTS orders_items;
DROP SEQUENCE IF EXISTS orders_items_id_seq;

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    date_placed date
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    unit_price decimal(5, 2),
    quantity int
);

CREATE TABLE orders_items (
    id SERIAL PRIMARY KEY,
    order_id int,
    item_id int,
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    CONSTRAINT fk_item FOREIGN KEY (item_id) REFERENCES items(id) ON DELETE CASCADE
    -- PRIMARY KEY (order_id, item_id)
);


INSERT INTO items (name, unit_price, quantity) VALUES ('cup', 2.39, 30);
INSERT INTO items (name, unit_price, quantity) VALUES ('fork', 1.25, 55);
INSERT INTO items (name, unit_price, quantity) VALUES ('knife', 8.97, 41);
INSERT INTO items (name, unit_price, quantity) VALUES ('spatula', 5.24, 18);
INSERT INTO items (name, unit_price, quantity) VALUES ('bin', 12.65, 61);

INSERT INTO orders(customer_name, date_placed) VALUES ('Lizzie', '2022-11-07');
INSERT INTO orders(customer_name, date_placed) VALUES ('Tom', '2023-08-30');
INSERT INTO orders(customer_name, date_placed) VALUES ('Cat', '2020-04-12');

INSERT INTO orders_items (order_id, item_id) VALUES (1, 2);
INSERT INTO orders_items (order_id, item_id) VALUES (1, 5);
INSERT INTO orders_items (order_id, item_id) VALUES (2, 1);
INSERT INTO orders_items (order_id, item_id) VALUES (2, 3);
INSERT INTO orders_items (order_id, item_id) VALUES (3, 3);
INSERT INTO orders_items (order_id, item_id) VALUES (3, 4);
INSERT INTO orders_items (order_id, item_id) VALUES (3, 4);