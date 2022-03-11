from django.contrib import admin
from .models import Author, Book, Subscriber, Subscription

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_filter = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'count', 'subscription_cost']
    list_filter = ['author']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['user', 'address']
    list_filter = ['user']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'book', 'borrowed_date', 'amount_paid', 'days', 'returned']
