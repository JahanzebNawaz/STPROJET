from .base import BaseTest
from django.contrib.auth.models import User
from APP.models import Subscriber


class TestSubscriber(BaseTest):

    def test_subscriber_record(self):
        subscriber = Subscriber.objects.count()
        self.assertEqual(subscriber, 3)

    def test_add_new_subscriber(self):
        self.assert_check_subscriber(3)
        #new_subscriber = self.add_new_subscriber()
        self.assert_check_subscriber(4)
        subscriber = Subscriber.objects.last()
        self.assertEqual(subscriber.user.username, new_subscriber.user.username)

    def test_update_subscriber(self):
        self.assert_check_subscriber(3)
        self.add_new_subscriber()
        subscriber = Subscriber.objects.last()
        self.assertEqual(subscriber.user.username, 'Jahan')
        user = User.objects.first()
        subscriber.user = user
        subscriber.save()
        self.assertEqual(subscriber.user.username, 'admin')

    def test_delete_subscriber(self):
        self.assert_check_subscriber(3)
        self.add_new_subscriber()
        subscriber = Subscriber.objects.last()
        self.assertEqual(subscriber.id, 4)
        subscriber.delete()
        self.assert_check_subscriber(3)
        subscriber = Subscriber.objects.last()
        self.assertEqual(subscriber.id, 3)

    def add_new_subscriber(self):
        user = User.objects.create_user(
            username='Jahan'
        )
        subscriber = Subscriber.objects.create(
            user=user,
            address='Von lingen vag 23',
            phone='+909090909090'
        )
        return subscriber

    def assert_check_subscriber(self, count):
        subscriber = Subscriber.objects.count()
        self.assertEqual(subscriber, count)
