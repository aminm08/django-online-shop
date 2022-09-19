from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.translation import gettext as _

from .forms import CustomUserChangeForm


def user_profile_view(request):
    form = CustomUserChangeForm(instance=request.user)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('your profile updated successfully'))
    return render(request, 'account/profile.html', {'form': form})