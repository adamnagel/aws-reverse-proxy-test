from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/<path:path>')
def show_user_profile(path):
    # show the user profile for that user
    return '<h1>Yoda Server</h1> The path you requested is: <br>%s' % escape(path)
