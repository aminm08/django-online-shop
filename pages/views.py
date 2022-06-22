from django.shortcuts import render
from django.views.generic import TemplateView

class HomepageView(TemplateView):
    template_name = 'home_page.html'

class AboutUsPageView(TemplateView):
    template_name = 'about_us.html'