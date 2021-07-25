import sqlite3


class UserModel:

    def __init__(self, _id, username, password, email, phone):
        self.id = _id
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"<{self.id}, {self.username}, {self.password}>"

    @classmethod
    def find_by_username(cls, username):

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE email=?"
        result = cursor.execute(query, (username,))

        result = result.fetchone()
        if result:
            user = cls(*result)
        else:
            user = None
        connection.close()

        return user

    @classmethod
    def find_by_userid(cls, userid):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (userid,))

        result = result.fetchone()
        connection.close()

        if result:
            user = cls(*result)
        else:
            user = None

        return user
