import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text, email text, mobile text)'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY_KEY, product_name text, category text, subcategory, price text, description text, review_star)'
cursor.execute(query)

query = 'INSERT INTO products VALUES (1, "first_product", "cat1", "123", "very good prod", "4.5")'
cursor.execute(query)
query = 'INSERT INTO products VALUES (2, "second_product", "cat1", "123", "very good prod", "4.5")'
cursor.execute(query)
query = 'INSERT INTO products VALUES (3, "third_product", "cat1", "123", "very good prod", "4.5")'
cursor.execute(query)
query = 'INSERT INTO products VALUES (4, "fourth_product", "cat2", "123", "very good prod", "4.5")'
cursor.execute(query)
query = 'INSERT INTO products VALUES (5, "five_product", "cat3", "123", "very good prod", "4.5")'
cursor.execute(query)
query = 'INSERT INTO products VALUES (6, "six_product", "cat2", "123", "very good prod", "4.5")'
cursor.execute(query)

query = 'CREATE TABLE IF NOT EXISTS cart (user_id INTEGER, product_id INTEGER)'
cursor.execute(query)


connection.commit()
connection.close()
