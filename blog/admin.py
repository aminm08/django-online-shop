from django.contrib import admin

from .models import BlogPost


@admin.register(BlogPost)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'datetime_modified')
