from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity

from resources.user import UserRegister
from resources.product import Product
from resources.cart import Cart

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdsafsdfefsdfsd'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth for login

api.add_resource(UserRegister, '/register')
api.add_resource(Product, '/product/<category>', '/product')
api.add_resource(Cart, '/cart/<product_id>', '/cart')

if __name__ == '__main__':
    app.run(debug=True)