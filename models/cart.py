import sqlite3

from models.product import ProductModel

class CartModel:
    def __init__(self, product_id):
        self.product_id = product_id

    @classmethod
    def find_by_user_id(cls, user_id):
        query = 'SELECT * FROM products WHERE id IN (SELECT product_id from cart WHERE user_id=?)'

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        result = []
        for row in cursor.execute(query, (user_id, )).fetchall():
            product = ProductModel(*row)
            result.append(product)
        return result
