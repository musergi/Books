import sqlite3


def _dict_factory(cursor, row):
    d = {}
    for index, column in enumerate(cursor.description):
        d[column[0].lower()] = row[index]
    return d


def create_table(cursor: sqlite3.Cursor, name: str, columns: str) -> None:
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {name} ({columns})')


def create_database(address: str) -> sqlite3.Connection:
    connection = sqlite3.connect(address, check_same_thread=False)
    connection.row_factory = _dict_factory
    cursor = connection.cursor()
    create_table(cursor, 'authors', 'id INTEGER PRIMARY KEY, names TEXT, surnames TEXT, pseudonym TEXT')
    create_table(cursor, 'books', 'id INTEGER PRIMARY KEY, title TEXT, author_id INTEGER, FOREIGN KEY(author_id) REFERENCES authors(id)')
    return connection
