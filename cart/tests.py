from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class CartTesCase(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    # Testing the views

    def test_cart_without_login(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")

    def test_cart_login(self):
        self.client.post('/accounts/login/', self.credentials, follow=True)
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
