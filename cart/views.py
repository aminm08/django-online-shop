from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _

from .cart import Cart
from .forms import AddToCartForm
from products.models import Product


def cart_detail_view(request):
    cart = Cart(request)
    for item in cart:
        item['product_update_quantity_form'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True
        })

    return render(request, 'cart/cart_detail_temp.html', {'cart': cart})


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    form = AddToCartForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product, cleaned_data['quantity'], replace_current_quantity=cleaned_data['inplace'])
    return redirect('cart_detail')


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    return redirect('cart_detail')


@require_POST
def clear_cart(request):
    cart = Cart(request)

    if len(cart):
        cart.clear()
        messages.success(request, _('your cart is now empty'))
    else:
        messages.warning(request, _('your cart is already empty!'))
    return redirect('cart_detail')
