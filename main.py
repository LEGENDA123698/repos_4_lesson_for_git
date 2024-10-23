import sqlite3

connect = sqlite3.connect("store.db")
cursor = connect.cursor()

# cursor.execute('''
#     CREATE TABLE products (
#     product_id INTEGER PRIMARY KEY,
#     name TEXT NOT NULL,
#     category TEXT NOT NULL,
#     price REAL NOT NULL
# );
# ''')

# cursor.execute('''
#                CREATE TABLE customers ( 
#                customer_id INTEGER PRIMARY KEY, 
#                first_name TEXT NOT NULL, 
#                last_name TEXT NOT NULL, 
#                email TEXT NOT NULL UNIQUE
# );
# ''')

# cursor.execute('''
#                CREATE TABLE orders ( 
#                order_id INTEGER PRIMARY KEY, 
#                customer_id INTEGER NOT NULL, 
#                product_id INTEGER NOT NULL, 
#                quantity INTEGER NOT NULL, 
#                order_date DATE NOT NULL, 
#                FOREIGN KEY (customer_id) 
#                REFERENCES customers(customer_id), 
#                FOREIGN KEY (product_id) REFERENCES products(product_id) 
# );
# ''')

# cursor.executemany('''INSERT INTO products(product_id, name, category, price)
# VALUES((?), (?), (?), (?))''',
#     [(1, "Xiaomi Redmi Pad SE 4/128GB Graphite Gray", "Tablets", 25),
#     (2, "Lenovo Tab M11  4/128 WiFi Luna Grey + Pen", "Tablets", 32),
#     (3, "Lenovo Tab M9 4/64 WiFi Arctic grey + Case&Film", "Tablets", 19),
#     (4, "Xiaomi Redmi Note 13 Pro 8/256 Lavender Purple", "Phones", 15),
#     (5, "Xiaomi 13T 8/256 Black", "Phones", 25),
#     (6, "Xiaomi Redmi Pad SE 4/128GB Graphite Gray", "Phones", 25),
#     (7, "Lenovo Ideapad Slim 5 16ABR8 Cloud Grey", "Laptops", 10),
#     (8, "Apple MacBook Air 13 M1 (MGN63) Space Grey", "Laptops", 25),
#     (9, "Lenovo LOQ 15IAX9", "Laptops", 25)])
# connect.commit()

# cursor.execute('''INSERT INTO customers(customer_id, first_name, last_name, email)
# VALUES
#     (1, "Jon", "Lar", "Jon@gmail.com"),
#     (2, "Devid", "Den", "Devid@gmail.com"),
#     (3, "Lauri", "Bar", "Lauri@gmail.com"),
#     (4, "Kenni", "Ren", "Kenni@gmail.com"),
#     (5, "Lara", "Claus", "Lara@gmail.com"),
#     (6, "Sara", "Bend", "Sara@gmail.com")
# ''')
# connect.commit()

# cursor.execute('''INSERT INTO orders(order_id, customer_id, product_id, quantity, order_date)
# VALUES
#     (1, 1, 6, 2, "2024-08-27"),
#     (2, 2, 3, 1, "2024-05-04"),
#     (3, 3, 5, 4, "2024-01-28"),
#     (4, 3, 9, 3, "2024-12-15"),
#     (5, 5, 7, 1, "2024-10-05")
# ''')
# connect.commit()

# cursor.execute('''SELECT SUM(quantity) AS total_sales 
#                 FROM orders
# ''')

# cursor.execute('''SELECT customers.customer_id, customers.first_name, customers.last_name, COUNT(orders.order_id) AS order_count
# FROM customers
# INNER JOIN orders ON customers.customer_id = orders.customer_id
# GROUP BY customers.customer_id, customers.first_name, customers.last_name
# ''')

# cursor.execute('''SELECT customers.first_name,  AVG(products.price) AS prod_price
#                FROM products 
#                INNER JOIN orders ON orders.product_id = products.product_id
#                INNER JOIN customers ON customers.customer_id = orders.customer_id
#                GROUP BY orders.customer_id                             
# ''')

# cursor.execute('''SELECT products.category, SUM(orders.quantity) AS sum_quantity
#                FROM orders
#                INNER JOIN products ON products.product_id = orders.product_id
#                GROUP BY products.category
# ''')

# cursor.execute('''UPDATE products
#                SET price = price * 11 WHERE category = "Phones"
# ''')

# cursor.execute('''SELECT products.category, COUNT(products.product_id), AS products_count
#                FROM products
#                GROUP BY products.category
# ''')



connect.commit()

res = cursor.fetchall()

print(res)

