from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Product, Comment
from .forms import CommentForm


class PruductListView(generic.ListView):
    model = Product
    template_name = 'products/products_list_view.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/products_detail_view.html'
    context_object_name = 'product'


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, pk=product_id)

        obj.product = product
        obj.author = self.request.user

        obj.save()
        return super().form_valid(form)

