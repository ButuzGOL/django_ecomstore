from ecomstore.catalog.models import Product
from ecomstore.cart.models import CartItem
from ecomstore.cart import cart
from  django.test import TestCase, Client
from  django.core import urlresolvers
from  django.db import IntegrityError
from  django.contrib import csrf
from  django.conf import settings
import httplib

class CartTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.active.all()[0]
         
    def test_cart_id(self):
        home_url = urlresolvers.reverse('catalog_home')
        self.client.get(home_url)
        # check that there is a cart_id set in session
        # after a page with cart box has been requested
        self.failUnless(self.client.session.get(cart.CART_ID_SESSION_KEY, ''))
     
    def test_add_product(self):
        QUANTITY = 2
        product_url = self.product.get_absolute_url()
        response = self.client.get(product_url)
        self.assertEqual(response.status_code, httplib.OK )
        # store count in cart_count variable
        cart_item_count = self.get_cart_item_count()
        # assert that the cart item count is zero
        self.failUnlessEqual(cart_item_count, 0)
        # perform the post of adding to the cart
        cookie = self.client.cookies[settings.SESSION_COOKIE_NAME]
        csrf_token = csrf.middleware._make_token(cookie.value)
        postdata = {'product_slug': self.product.slug,
                    'quantity': QUANTITY,
                    'csrfmiddlewaretoken': csrf_token }
        response = self.client.post(product_url, postdata )
        # assert redirected to cart page - 302 then 200
        cart_url = urlresolvers.reverse('show_cart')
        self.assertRedirects(response, cart_url, status_code=httplib.FOUND,
                             target_status_code=httplib.OK)
        # assert cart item count is incremented by one
        self.assertEqual(self.get_cart_item_count(), cart_item_count + 1)
        cart_id = self.get_cart_id()
        last_item = CartItem.objects.filter(cart_id=cart_id). \
                                                            latest('date_added')
        # assert the latest cart item has a quantity of two
        self.failUnlessEqual(last_item.quantity, QUANTITY)
        # assert the latest cart item is the correct product
        self.failUnlessEqual(last_item.product, self.product)
        
    def get_cart_item_count(self):
        cart_id = self.get_cart_id()
        return CartItem.objects.filter(cart_id=cart_id).count()
        
    def get_cart_id(self):
        return self.client.session.get(cart.CART_ID_SESSION_KEY)

    def test_add_to_cart_fails_csrf(self):
        quantity = 2
        product_url = self.product.get_absolute_url()
        response = self.client.get(product_url)
        self.assertEqual(response.status_code, httplib.OK )
        # perform the post of adding to the cart
        postdata = {'product_slug': self.product.slug,
                     'quantity': quantity }
        response = self.client.post(product_url, postdata )
        # assert forbidden error due to missing CSRF input
        self.assertEqual(response.status_code, httplib.FORBIDDEN )

