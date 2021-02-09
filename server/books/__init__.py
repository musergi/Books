import sqlite3
from flask import Flask
from flask.json import jsonify


def _dict_factory(cursor, row):
    d = {}
    for index, column in enumerate(cursor.description):
        d[column[0].lower()] = row[index]
    return d


app = Flask(__name__)
database = sqlite3.connect('data.db', check_same_thread=False)
database.row_factory = _dict_factory


@app.route('/api/author/') 
@app.route('/api/author/<author_id>/')
def author(author_id=None):
    cursor = database.cursor()
    if author_id is None:
        return jsonify(list(cursor.execute('SELECT * FROM authors')))
    return jsonify(cursor.execute(f'SELECT * FROM authors WHERE id = {author_id}').fetchone())


@app.route('/api/book/')
@app.route('/api/book/<book_id>/')
def book(book_id=None):
    cursor = database.cursor()
    if book_id is None:
        return jsonify(list(cursor.execute('SELECT * FROM books')))
    try:
        book_id_integer = int(book_id)
        return jsonify(cursor.execute(f'SELECT * FROM books WHERE id = {book_id_integer}').fetchone())
    except ValueError:
        return 'Bad Request Error', 403

