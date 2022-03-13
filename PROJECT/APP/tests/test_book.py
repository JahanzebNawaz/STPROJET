from .base import BaseTest
from APP.models import Book, Author


class TestBook(BaseTest):

    def test_book_record(self):
        books = Book.objects.count()
        self.assertEqual(books, 3)

    def test_add_new_book(self):
        self.assert_check_book(3)
        new_book = self.add_new_book()
        self.assert_check_book(4)
        book = Book.objects.last()
        self.assertEqual(book.title, new_book.title)
        self.assertEqual(book.description, new_book.description)
        self.assertEqual(book.count, 10)
        self.assertEqual(book.author.name, new_book.author.name)

    def test_update_book(self):
        self.assert_check_book(3)
        self.add_new_book()
        book = Book.objects.last()
        self.assertEqual(book.count, 10)
        self.assertEqual(book.subscription_cost, 6)
        book.count = 20
        book.subscription_cost = 8
        book.save()
        self.assertEqual(book.count, 20)
        self.assertEqual(book.subscription_cost, 8)

    def test_delete_book(self):
        self.assert_check_book(3)
        self.add_new_book()
        book = Book.objects.last()
        self.assertEqual(book.id, 4)
        book.delete()
        self.assert_check_book(3)
        book = Book.objects.last()
        self.assertEqual(book.id, 3)

    def add_new_book(self):
        title = 'Software testing: principles and practices'
        description = '"Software Testing: Principles and Practices is a comprehensive treatise on software testing.'
        author = Author.objects.filter(id=1)
        book = Book.objects.create(
            title=title,
            description=description,
            count=10,
            subscription_cost=6
        )
        book.author.set(author)
        book.save()
        return

    def assert_check_book(self, count):
        book = Book.objects.count()
        self.assertEqual(book, count)