from .base import BaseTest
from APP.models import Author


class TestAuthors(BaseTest):

    def test_author_record(self):
        author = Author.objects.count()
        self.assertEqual(author, 3)

    def test_add_new_author(self):
        self.assert_check_author(3)
        new_author = Author.objects.create(
            name="Dean Leffingwell",
            address="Von lingens 86"
        )
        self.assert_check_author(4)
        self.assertEqual(new_author.name, "Dean Leffingwell")

    def test_update_author(self):
        self.assert_check_author(3)
        author = Author.objects.last()
        self.assertEqual(author.name, 'Barbara Cartland')
        author.name = 'Leffingwell'
        author.save()
        author_updated = Author.objects.last()
        self.assertEqual(author_updated.name, 'Leffingwell')

    def test_delete_author(self):
        self.assert_check_author(3)
        author = Author.objects.last()
        self.assertEqual(author.id, 3)
        author.delete()
        self.assert_check_author(2)
        author = Author.objects.last()
        self.assertEqual(author.id, 2)

    def assert_check_author(self, count):
        author = Author.objects.count()
        self.assertEqual(author, count)
