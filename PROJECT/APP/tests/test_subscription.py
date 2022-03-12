from .base import BaseTest
from APP.models import Subscriber, Subscription, Book


class TestSubscription(BaseTest):

    def test_subscription_record(self):
        subscription = Subscription.objects.count()
        self.assertEqual(subscription, 3)
        subscription = Subscription.objects.last()
        self.assertEqual(subscription.subscriber.id, 3)
        self.assertEqual(subscription.book.id, 3)
        self.assertEqual(str(subscription.borrowed_date), "2022-03-11")
        self.assertEqual(subscription.amount_paid, 120)
        self.assertEqual(subscription.days, 10)

    def test_add_new_subscription(self):
        self.assert_check_subscription(3)
        new_subscription = self.add_new_subscription()
        self.assert_check_subscription(4)
        subscription = Subscription.objects.last()
        self.assertEqual(subscription.book.title, new_subscription.book.title)
        self.assertEqual(subscription.subscriber.user.username,
                         new_subscription.subscriber.user.username)

    def test_update_subscription(self):
        self.assert_check_subscription(3)
        self.add_new_subscription()
        subscription = Subscription.objects.last()
        self.assertEqual(subscription.amount_paid, 12)
        self.assertEqual(subscription.days, 1)
        self.assertEqual(subscription.returned, False)
        subscription.returned = True
        subscription.save()
        subscription = Subscription.objects.last()
        self.assertEqual(subscription.returned, True)

    def test_delete_subscription(self):
        self.assert_check_subscription(3)
        self.add_new_subscription()
        subscription = Subscription.objects.last()
        self.assertEqual(subscription.id, 4)
        subscription.delete()
        self.assert_check_subscription(3)
        subscription = Subscription.objects.last()
        self.assertEqual(subscription.id, 3)

    def add_new_subscription(self):
        subscriber = Subscriber.objects.last()
        book = Book.objects.last()
        subscription = Subscription.objects.create(
            subscriber=subscriber,
            book=book,
            amount_paid=12,
            days=1,
            returned=False
        )
        return subscription

    def assert_check_subscription(self, count):
        subscription = Subscription.objects.count()
        self.assertEqual(subscription, count)
