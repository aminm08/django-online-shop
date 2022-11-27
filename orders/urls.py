from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.orders_create_view, name='order_create')
]