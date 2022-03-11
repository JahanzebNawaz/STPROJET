from .base import BaseTest
from django.contrib.auth.models import User


class UserTests(BaseTest):

    def test_create_new_user(self):
        user_id = User.objects.last().id
        self.assertEqual(user_id, 5)
        new_user = User.objects.create_user(
            username='testuser',
            password='testtest',
            first_name='Test',
            last_name='User'
        )
        count = User.objects.count()
        self.assertEqual(new_user.id, count)

    def test_update_user(self):
        user = User.objects.last()
        self.assertEqual(user.id, 5)
        user.first_name = 'test'
        user.save()
        user = User.objects.last()
        self.assertEqual(user.first_name, 'test')

