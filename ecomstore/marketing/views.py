from django.http import HttpResponse
from ecomstore.settings import CURRENT_PATH
import os
from django.template.loader import get_template
from django.template import Context
from ecomstore.catalog.models import Product

ROBOTS_PATH = os.path.join(CURRENT_PATH, 'marketing/robots.txt')

def robots(request):
    return HttpResponse(open(ROBOTS_PATH).read(), 'text/plain')

def google_base(request):
    products = Product.active.all()
    template = get_template("marketing/google_base.xml")
    xml = template.render(Context(locals()))
    return HttpResponse(xml, mimetype="text/xml")