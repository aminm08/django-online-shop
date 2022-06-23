from django.urls import path

from . import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('signupchange/',views.EditSignUpInfo.as_view(),name='edit_signup'),
]