from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Format: '+999999999'. Up to 15 digits allowed.")


class Subscriber(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(validators=[phone_regex], max_length=17)

    def __str__(self):
        return 'Subscriber {}'.format(self.user)
