CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT NOT NULL, quantity NUMERIC, price NUMERIC NOT NULL, description TEXT NOT NULL);

SELECT * FROM products;

ALTER TABLE products ADD photo BLOB;

CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, hash TEXT NOT NULL );