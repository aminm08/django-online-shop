from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('order', 'product', 'quantity', 'price')
    extra = 1


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid']
    ordering = ['-datetime_created']
    list_filter = ['is_paid']
    search_fields = ('first_name', 'last_name')
    inlines = [
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    ordering = ['-price']
