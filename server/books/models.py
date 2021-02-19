from django.db import models

# Create your models here.
class Author(models.Model):
    names = models.TextField(blank=True)
    surnames = models.TextField(blank=True)
    pseudonym = models.TextField(blank=True)
