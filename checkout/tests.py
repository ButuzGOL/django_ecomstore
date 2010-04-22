from django.test import TestCase, Client
from django.core import urlresolvers
from  ecomstore.checkout.forms import CheckoutForm
from  ecomstore.checkout.models import Order, OrderItem
from  ecomstore.catalog.models import Category, Product
from  ecomstore.cart import cart
from  ecomstore.cart.models import CartItem
import httplib

class CheckoutTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        home_url = urlresolvers.reverse('catalog_home')
        self.checkout_url = urlresolvers.reverse('checkout')
        self.client.get(home_url)
        # need to create customer with a shopping cart first
        self.item = CartItem()
        product = Product.active.all()[0]
        self.item.product = product
        self.item.cart_id = self.client.session[cart.CART_ID_SESSION_KEY]
        self.item.quantity = 1
        self.item.save()

    def test_checkout_page_empty_cart(self):
        """ empty cart should be redirected to cart page """
        client = Client()
        cart_url = urlresolvers.reverse('show_cart')
        response = client.get(self.checkout_url)
        self.assertRedirects(response, cart_url)
   
    def test_submit_empty_form(self):
        """ empty form should raise error on required fields """
        form = CheckoutForm()
        response = self.client.post(self.checkout_url, form.initial)
        for name, field in form.fields.iteritems():
            value = form.fields[name]
            if not value and form.fields[name].required:
                error_msg = form.fields[name].error_messages['required']
                self.assertFormError(response, "form", name, [error_msg])