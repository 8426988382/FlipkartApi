import sqlite3

from flask_restful import Resource
from flask_jwt import jwt_required, current_identity

from models.cart import CartModel
from models.product import ProductModel


class Cart(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        _id = current_identity
        user_id = _id.id
        result = CartModel.find_by_user_id(user_id)

        products = []
        for product in result:
            individual_product = {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "review_star": product.review_star,
                "description": product.description
            }
            products.append(individual_product)
        return {'products in your cart are': products}, 200

    @classmethod
    @jwt_required()
    def post(cls, product_id):
        _id = current_identity
        user_id = _id.id
        print("user_id is ", user_id)

        query = "INSERT INTO cart VALUES (?, ?)"
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute(query, (user_id, product_id))
        connection.commit()
        connection.close()

        return {'message': 'item added to cart'}, 201
