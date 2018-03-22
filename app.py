from flask import Flask, request, render_template

from api.api import api

app = Flask(__name__)

app.register_blueprint(api)

flask_app = Flask(__name__)


@app.route('/user/<username>', methods=['GET', 'POST'])
def show(username):
    return username


def do_the_login():
    return "123"


def show_the_login_form():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


if __name__ == '__main__':
    app.run(debug=True)
