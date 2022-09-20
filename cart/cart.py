from django.contrib import messages
from products.models import Product
from django.utils.translation import gettext as _


class Cart:

    def __init__(self, request):
        # Initialize the cart

        self.request = request

        self.session = request.session

        self.cart = self.session.get('cart')

        if not self.cart:
            self.cart = self.session['cart'] = {}

    def add(self, product, quantity, replace_current_quantity):

        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if replace_current_quantity:
            self.cart[product_id]['quantity'] = quantity
        elif not replace_current_quantity:
            self.cart[product_id]['quantity'] += quantity

        messages.success(self.request, _('Cart updated successfully'))
        self.save()

    def remove(self, product):

        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, _('Item successfully deleted from cart'))
            self.save()

    def save(self):

        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            item['total_price'] = item['product_obj'].get_final_price() * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        return sum(item['quantity'] * item['product_obj'].get_final_price() for item in self.cart.values())

    def is_empty(self):
        if not self.cart:
            return True
        return False
