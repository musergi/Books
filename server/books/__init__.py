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
