from django.test import TestCase

# Create your tests here.
class HomeTesCase(TestCase):
    def test_arrive_at_homepage(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
