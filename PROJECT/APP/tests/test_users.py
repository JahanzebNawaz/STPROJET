from .base import BaseTest
from django.contrib.auth.models import User


class TestsUser(BaseTest):

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

    def test_get_user(self):
        user = User.objects.get(username='james')
        self.assertEqual(user.username, 'james')
        self.assertEqual(user.id, 4)
        self.assertEqual(user.first_name, 'james')

    def test_delete_user(self):
        User.objects.get(username='james').delete()
        user = User.objects.filter(username='james').exists()
        self.assertEqual(user, False)
