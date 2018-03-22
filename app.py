from flask import Flask

from api.api import api

app = Flask(__name__)

app.register_blueprint(api)

flask_app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
