from django import template
from ecomstore.cart import cart

from ecomstore.catalog.models import Category

from django.contrib.flatpages.models import FlatPage

register = template.Library()

@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count }

@register.inclusion_tag("tags/category_list.html")
def category_list(request_path):
    active_categories = Category.objects.filter(is_active=True)
    return {
         'active_categories': active_categories,
         'request_path': request_path
     }

@register.inclusion_tag("tags/footer.html")
def footer_links():
    flatpage_list = FlatPage.objects.all()
    return {'flatpage_list': flatpage_list }

@register.inclusion_tag("tags/product_list.html")
def product_list(products, header_text):
    return { 'products': products,
            'header_text': header_text }