import sqlite3
import bcrypt
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='username required')

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='password required')

    parser.add_argument('mobile',
                        type=str,
                        required=True,
                        help='mobile number required')

    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='email required')

    @classmethod
    def post(cls):
        data = cls.parser.parse_args(strict=True)
        username = data['username']
        password = data['password']
        email = data['email']
        mobile = data['mobile']

        if UserModel.find_by_username(username):
            return {'message': 'username is in use'}, 400

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        # here push data according to your database
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'INSERT INTO users VALUES (NULL , ?, ?, ?, ?)'
        cursor.execute(query, (username, hashed_password, email, mobile))

        connection.commit()
        connection.close()

        return {'message': 'user_created'}, 201
