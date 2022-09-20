from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='cart_add'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='cart_remove'),
    path('empty/', views.clear_cart, name='cart_empty'),
]
