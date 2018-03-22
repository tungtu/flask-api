import os
from flask import Flask

from api.api import api

app = Flask(__name__)

app.register_blueprint(api)

flask_app = Flask(__name__)

port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
