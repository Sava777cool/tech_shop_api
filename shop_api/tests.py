from django.test import TestCase
from .models import Product


class ProductTest(TestCase):
    """ Test module for Product model """
    def setUp(self):
        Product.objects.create(name='Notebook', price=950)
        Product.objects.create(name='Smartphone', price=1200)

    def test_product_type(self):
        notebook = Product.objects.get(name='Notebook')
        smartphone = Product.objects.get(name='Smartphone')
        self.assertEqual(
            notebook.get_name(), "Notebook it`s a cool.")
        self.assertEqual(
            smartphone.get_name(), "Smartphone it`s a cool.")



