from flask_restful import fields, reqparse, marshal_with, Api, Resource
from flask import Flask, got_request_exception

app = Flask(__name__)
"""
app = flask app name
prefix = prefix all routes with a value
decorators = to attach to every resource
catch_all_404s = catch the 404 errors in the json format(True)
serve_challenge_on_401 = pop up username password window in browser (True)
"""
api = Api(app=app, prefix='/api', catch_all_404s=True, serve_challenge_on_401=True)

"""
this is for structuring the response
used with the marshal_with decorator
filters the response
act on response such as objects 
"""


class CustomFormat(fields.Raw):
    """
    this is for Custom formatting of the data
    """
    def format(self, value):
        return value.upper()


class UnreadItem(fields.Raw):
    def format(self, value):
        return "Unread" if value & 0x02 else "Read"


resource_field = {
    'default example': fields.String(default='Something Default'),
    'todo': fields.Integer,
    'task': fields.String,
    'url': fields.Url('todo_ep', absolute=True, scheme='https'),
    'status': fields.String,
    'formatted_string': fields.FormattedString('Hello, your task is "{task}"'),
    'some custom field': CustomFormat(attribute='task'),
    'names': fields.List(fields.String)
}

"""
Bundle error will bundle all the errors first and then send these errors together so client will know whole errors
at once
"""
parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('first', type=str, trim=True, required=True, help='Bad Request: {error_msg}')
parser.add_argument('second', type=str, trim=True, required=True, help='required first')
"""
action=append, this means that we are expecting a list, from 0 to n length
"""
parser.add_argument('name', action='append')

"""
By default parser.add_argument() tries to parse values from flask.Request.values and flask.Request.json 
location='form' or 'args' or 'headers' or 'cookies' or 'files' or [a list of multiple locations]
for manual location
"""


class TodoDao:
    def __init__(self, todo, task, names):
        self.todo = todo
        self.task = task
        self.names = names

        self.status = 'active'


class Todo(Resource):
    """
    marshal with decorator is used to structure the response with some specified resource field
    """

    @classmethod
    @marshal_with(resource_field, envelope='Your Todo Data')
    def get(cls):
        return TodoDao(todo='1', task='Remember the milk', names=['tushar', 'tambi'])

    @classmethod
    def post(cls):
        args = parser.parse_args(strict=True)
        print(args)
        return {"message": 'yes you pass'}


def log_exception(sender, exception, **extra):
    sender.logger.debug('Got Exception during processing: %s', exception)


api.add_resource(Todo, '/todo', '/home', endpoint='todo_ep')
"""
this got_request_exception is for logging or performing any actions after receiving any error
or exception
"""
got_request_exception.connect(log_exception, app)

if __name__ == '__main__':
    app.run(debug=True)
