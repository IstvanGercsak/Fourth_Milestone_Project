from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class CheckoutTesCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # Testing the views

    def test_checkout_with_login(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 302)
        page = self.client.get("/accounts/login/?next=/checkout/")
        self.assertEqual(page.status_code, 200)

    def test_checkout_without_login(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
