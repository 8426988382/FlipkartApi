from flask_restful import Resource
from models.product import ProductModel


class Product(Resource):
    @classmethod
    def get(cls, category=None):
        if category:
            products = ProductModel.find_by_product_category(category)

        else:
            products = ProductModel.find_all_products()

        result = []
        for product in products:
            individual_product = {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "review_star": product.review_star,
                "description": product.description
            }
            result.append(individual_product)
        return {'products': result}, 200
