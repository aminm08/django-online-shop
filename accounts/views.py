from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import CustomCreationForm,CustomUserChangeForm

class SignUpView(generic.CreateView):
    form_class = CustomCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

# class EditSignUpInfo(generic.UpdateView):
#     form_class = CustomUserChangeForm
#     template_name = 'registration/edit.html'
#     success_url = reverse_lazy('homepage')