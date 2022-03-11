from django.db import models
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=25)
    address = models.TextField()

    def __str__(self):
        return 'Author {}'.format(self.name)
