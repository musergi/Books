import json
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist
from .models import Author


def author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    data = json.dumps(author.to_dict(), indent=2)
    return  HttpResponse(data, content_type='application/json')


def authors(request):
    if request.method == 'GET':
        authors = list(Author.objects.all())
        data = json.dumps([author.to_dict() for author in authors], indent=2)
        return  HttpResponse(data, content_type='application/json')
    if request.method == 'POST':
        return HttpResponse()
    return HttpResponseBadRequest('Method not supported.')
