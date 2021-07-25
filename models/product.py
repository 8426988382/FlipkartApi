import sqlite3


class ProductModel:
    def __init__(self, _id, name, price, category, description, review_star):
        self.id = _id
        self.name = name
        self.category = category
        self.price = price
        self.description = description
        self.review_star = review_star

    def __repr__(self):
        return f'<product is {self.id} {self.name} {self.price} {self.category} {self.description} {self.review_star}>'

    @classmethod
    def find_by_product_name(cls, name):
        query = 'SELECT * FROM products where product_name=?'

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        result = cursor.execute(query, (name,))

        connection.close()

        if result:
            product = cls(*result)
        else:
            product = None

        return product

    @classmethod
    def find_by_product_id(cls, _id):
        query = 'SELECT * FROM products where id=?'

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        result = cursor.execute(query, (_id,))
        return result
        # if result:
        #     product = cls(*result)
        # else:
        #     product = None
        # connection.close()
        # return product

    @classmethod
    def find_by_product_category(cls, category):
        query = 'SELECT * FROM products where category=?'

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        products = []
        for row in cursor.execute(query, (category,)).fetchall():
            products.append(cls(*row))

        return products

    @classmethod
    def find_all_products(cls):
        query = 'SELECT * FROM products'

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        products = []
        for row in cursor.execute(query).fetchall():
            products.append(cls(*row))

        return products
