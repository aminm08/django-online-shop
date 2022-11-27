from django.shortcuts import render


def orders_create_view(request):
    return render(request, 'orders/create_template.html')
