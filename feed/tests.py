from django.test import TestCase
from .models import Feed
from django.contrib.auth.models import User


# Create your tests here.

class FeedTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # Test views
    def test_feed_with_login(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/feed/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feed.html")

    def test_feed_without_login(self):
        page = self.client.get("/feed/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/accounts/login/?next=/checkout/")
        self.assertEqual(page.status_code, 200)

    # Test models
    def test_feed_title(self):
        test_feed_title = Feed(title="Feed title")
        self.assertEqual(str(test_feed_title.title), "Feed title")

    def test_feed_description(self):
        test_feed_description = Feed(description="Feed description")
        self.assertEqual(str(test_feed_description.description), "Feed description")
