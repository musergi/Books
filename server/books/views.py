from flask import Blueprint
from flask.json import jsonify
from . import database

api = Blueprint('/api/', __name__)

@api.route('/books/', methods=['GET'])
@api.route('/books/<int:offset>/<int:count>/', method=['GET'])
def authors(offset=None, count=None):
    cursor = database.cursor()
    if offset is None:
        offset = 0
    if count is None:
        count = 10
    return jsonify(list(cursor.execute(f'SELECT * FROM books LIMIT {count} OFFSET {offset}')))


@api.route('/book/', methods=['POST'])
def add_book():
    cursor = database.cursor()
    return 200, 'OK'
