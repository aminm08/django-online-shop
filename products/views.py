from django.views import generic
from .models import Product

class PruductListView(generic.ListView):
    model= Product
    template_name = 'products/products_list_view.html'
    context_object_name = 'products'

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/products_detail_view.html'
    context_object_name = 'product'