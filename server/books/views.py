from flask import Blueprint, request
from flask.json import jsonify
from .model import Author

api = Blueprint('api', __name__)

@api.after_request
def enable_cors(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@api.route('/author/<int:author_id>/', methods=['GET'])
def get_author(author_id):
    author = Author.get(author_id)
    return jsonify(dict(author))

@api.route('/authors/', methods=['GET'])
def get_authors(offset=0, count=10):
    return jsonify(Author.list(offset, count))

@api.route('/authors/', methods=['POST'])
def post_author():
    return 200, 'OK'

@api.route('/author/<int:author_id>/', methods=['DELETE'])
def delete_author():
    return 200, 'OK'
