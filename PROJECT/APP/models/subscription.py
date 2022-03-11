from django.db import models
from django.core.exceptions import ValidationError
from .subscriber import Subscriber
from .books import Book


class Subscription(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    amount_paid = models.PositiveIntegerField()
    days = models.PositiveIntegerField()
    returned = models.BooleanField()

    def total_amount(self):
        return self.book.subscription_cost * self.days

    def clean(self):
        amount = self.total_amount()
        if amount != self.amount_paid:
            raise ValidationError(
                'Paid amount {} does not matches with total amount {}'.format(
                    self.amount_paid, amount
                )
            )

    def save(self, *args, **kwargs):
        books = Subscription.objects.filter(book=self.book,
                                            returned=False).count()
        available = self.book.count - books

        if available > 0:
            return super().save(*args, **kwargs)
