from flask import Blueprint, jsonify

api = Blueprint('api', 'aaa', url_prefix='/api')


@api.route('/index')
def index():
    return jsonify({"status": 200, "message": "this is message"})


