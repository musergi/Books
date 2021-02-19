from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:author_id>/', views.author),
    path('authors/', views.authors),
]
