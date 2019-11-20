from django.test import TestCase
from .models import Blog


# Create your tests here.
class BlogTest(TestCase):

    # Test views
    def test_blog_without_login(self):
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blog.html")

    # Test models
    def test_blog_title(self):
        test_blog_title = Blog(title="Test title")
        self.assertEqual(str(test_blog_title.title), "Test title")

    def test_blog_description(self):
        test_blog_description = Blog(description="Description")
        self.assertEqual(str(test_blog_description.description), "Description")
