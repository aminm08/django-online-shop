from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomeUser
from .forms import CustomUserChangeForm,CustomCreationForm

@admin.register(CustomeUser)
class CustomUserAdmin(UserAdmin):
    model = CustomeUser
    add_form =CustomCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email', ]


