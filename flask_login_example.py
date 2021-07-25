from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, \
    fresh_login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['USE_SESSION_FOR_NEXT'] = True
app.config['SECRET_KEY'] = 'secret'
"""
The login manager contains the code that let your application and Flask-Login work together
"""
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.__init__(app)
login_manager.login_view = 'login'
login_manager.login_message = 'You need to log in!'
login_manager.refresh_view = 'fresh'
login_manager.needs_refresh_message = 'You need to log in again for refresh'


# usermixin for the methods that we need to create(ex. is_authenticate, is_anonymous, etc)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# @app.route('/')
# def index():
#     user = User.query.filter_by(username='tushar').first()
#     login_user(user)
#     return 'you are logged in!'

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/logmein', methods=['POST'])
def logmein():
    username = request.form['username']
    user = User.query.filter_by(username=username).first()

    if user:
        login_user(user, remember=True)
        next_page = session.get('next')
        print(next_page)
        if next_page:
            return redirect(next_page)
        return '<h1>You are now logged in</h1>'

    return '<h1>User Not Found</h1>'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'you are now logged out!'


@app.route('/home')
@login_required
def home():
    return 'current user is ' + current_user.username


@app.route('/fresh')
@fresh_login_required
def fresh():
    return '<h1>You have a fresh login</h1>'


if __name__ == '__main__':
    app.run(debug=True)
