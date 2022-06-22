from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['email','username', ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['email','username', ]