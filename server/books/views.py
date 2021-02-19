from django.http import HttpResponse
from .models import Author


def author(author_id):
    return  HttpResponse('{}', content_type='application/json')


def authors():
    return  HttpResponse('{}', content_type='application/json')
