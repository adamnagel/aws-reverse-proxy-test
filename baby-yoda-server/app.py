from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Baby Yoda Server</h1> This is my root path.'


@app.route('/<path:path>')
def show_user_profile(path):
    # show the path provided
    return '<h1>Baby Yoda Server</h1> The path you requested is: <br>%s' % escape(path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)
