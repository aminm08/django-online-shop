from django.contrib import admin

from jalali_date.admin import ModelAdminJalaliMixin
from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    ordering = ['-price', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'rating', 'datetime_created', 'product']
    ordering = ['-datetime_created']
    list_filter = ['active', ]
