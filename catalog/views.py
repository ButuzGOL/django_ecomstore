from django.shortcuts import get_object_or_404, render_to_response
from ecomstore.catalog.models import Category, Product
from django.template import RequestContext

def index(request, template_name="catalog/index.html"):
    page_title = 'Musical Instruments and Sheet Music for Musicians'
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def show_category(request, category_slug, 
                  template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

