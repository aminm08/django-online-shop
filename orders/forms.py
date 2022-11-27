from django import forms

from .models import Order, OrderItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'order_note')
        widgets = {
            'address': forms.Textarea(
                attrs={'placeholder': 'ادرس کامل خود را بنویسید',
                       'rows': 15
                       }),

            'order_note': forms.Textarea(
                attrs={"placeholder": 'if you have any note please enter here otherwise leave it empty',
                       'rows': 15
                       })
        }
