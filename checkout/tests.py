from django.contrib.auth.models import User
from django.test import TestCase
from .models import Order


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

    # Test models

    def test_checkout_full_name(self):
        test_model = Order(full_name="Istvan Gercsak")
        self.assertEqual(str(test_model.full_name), "Istvan Gercsak")

    def test_checkout_phone_number(self):
        test_model = Order(phone_number=894473833)
        self.assertEqual(int(test_model.phone_number), 894473833)

    def test_checkout_country(self):
        test_model = Order(country="Ireland")
        self.assertEqual(str(test_model.country), "Ireland")

    def test_checkout_postcode(self):
        test_model = Order(postcode="Dublin 2")
        self.assertEqual(str(test_model.postcode), "Dublin 2")

    def test_checkout_town_or_city(self):
        test_model = Order(town_or_city="Dublin")
        self.assertEqual(str(test_model.town_or_city), "Dublin")

    def test_checkout_street_address1(self):
        test_model = Order(street_address1="Wintergarden Apartments 48, The Pine")
        self.assertEqual(str(test_model.street_address1), "Wintergarden Apartments 48, The Pine")

    def test_checkout_street_address2(self):
        test_model = Order(street_address2="Pearse Street 107")
        self.assertEqual(str(test_model.street_address2), "Pearse Street 107")

    def test_checkout_county(self):
        test_model = Order(county="Dublin")
        self.assertEqual(str(test_model.county), "Dublin")
