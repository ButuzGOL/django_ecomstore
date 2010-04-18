from django.shortcuts import render_to_response
from django.template import RequestContext
from ecomstore.cart import cart

def show_cart(request, template_name="cart/cart.html"):
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'     
    cart_subtotal = cart.cart_subtotal(request)
    return render_to_response(template_name, locals(),
                              context_instance=RequestContext(request))

