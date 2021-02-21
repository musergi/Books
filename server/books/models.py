from django.db import models

# Create your models here.
class Author(models.Model):
    names = models.TextField(blank=True)
    surnames = models.TextField(blank=True)
    pseudonym = models.TextField(blank=True)

    def to_dict(self):
        return {
            'id': self.id,
            'names': self.names.split(' '),
            'surnames': self.surnames.split(' '),
            'pseudonym': self.pseudonym}

    def __str__(self):
        if self.pseudonym:
            return self.pseudonym
        return f'{self.names} {self.surnames}'

class Book(models.Model):
    title = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author}'
