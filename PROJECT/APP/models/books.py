from django.db import models
from .author import Author


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    count = models.PositiveIntegerField()
    subscription_cost = models.PositiveIntegerField()
    author = models.ManyToManyField(Author)

    def __str__(self):
        return 'Book {}'.format(self.title)
