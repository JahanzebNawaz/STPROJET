from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.


class BaseTest(TestCase):

    fixtures = [
        'user',
        'author',
        'book',
        'subscriber',
        'subscription'
    ]

    def setUp(self) -> None:
        self.user = self.get_user()

    @staticmethod
    def get_user():
        data = {
            'username': 'jeff',
            'first_name': 'jeff',
            'email': 'jeff@test.com',
            'password': 'testtest',
            'is_superuser': True
        }

        user = User.objects.create_superuser(**data)
        return user
