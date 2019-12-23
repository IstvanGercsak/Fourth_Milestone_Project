from django.test import TestCase
from .models import Product


# Create your tests here.

class ProductTest(TestCase):
    """ Here we'll define the tests that we'll run against our Product moduls """

    # Test models

    def test_name(self):
        """ Test product name field """
        test_product = Product(name="A product")
        self.assertEqual(str(test_product.name), "A product")

    def test_description(self):
        """ Test product description field """
        test_product = Product(description="Description")
        self.assertEqual(str(test_product.description), "Description")

    def test_str(self):
        """ Test product price field """
        test_product = Product(price=123)
        self.assertEqual(int(test_product.price), 123)

    def test_product_slug(self):
        """ Test product slug field """
        test_product_slug = Product(slug="slug_test")
        self.assertEqual(str(test_product_slug.slug), "slug_test")
