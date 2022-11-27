from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext as _

from cart.cart import Cart
from .models import Order, OrderItem
from .forms import OrderForm


def orders_create_view(request):
    form = OrderForm()
    cart = Cart(request)

    if len(cart) == 0:
        messages.warning(request, _("You can't submit your order when your cart is empty "))
        return redirect('cart_detail')

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_obj = form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product = item['product_obj']
                OrderItem.objects.create(
                    order=order_obj,
                    product=product,
                    quantity=item['quantity'],
                    price=product.get_final_price(),
                )

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()

            cart.clear()

            messages.success(request, _('Your order successfully submitted'))
        return redirect('cart_detail')
    return render(request, 'orders/create_template.html', context={
        'form': form
    })
