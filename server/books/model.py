from .persistance import create_database

database = create_database('data.db')

class Author:
    def __init__(self, id, names='', surnames='', pseudonym='') -> None:
        self.id = id
        self.names = names.split(' ')
        self.surnames = surnames.split(' ')
        self.pseudonym = pseudonym

    def __iter__(self) -> iter:
        yield 'id', self.id
        if self.names:
            yield 'names', list(self.names)
        if self.surnames:
            yield 'surnames', list(self.surnames)
        if self.pseudonym:
            yield self.pseudonym
    
    @staticmethod
    def get(author_id):
        author_dict = database.cursor().execute(f'SELECT * FROM authors WHERE id = {author_id}').fetchone()
        if author_dict is None:
            raise IndexError('Author does not exist')
        return Author(**author_dict)
    
    @staticmethod
    def list(offset, count):
        authors = list(dict(Author(**row)) for row in database.execute(f'SELECT * FROM authors LIMIT {count} OFFSET {offset}'))
        return authors

    @staticmethod
    def create_author(names='', surnames='', pseudonym=''):
        database.cursor().execute(f'INSERT INTO authors (names, surnames, pseudonym) VALUES ({names}, {surnames}, ({pseudonym})')
