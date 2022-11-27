from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.urls import reverse_lazy

from .models import Product, Comment, Favorite
from .forms import CommentForm


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/products_list_view.html'
    context_object_name = 'products'
    paginate_by = 9


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/products_detail_view.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context


class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    http_method_names = ['post']
    success_message = _('your comment successfully added ')

    def form_valid(self, form):
        obj = form.save(commit=False)
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product, pk=product_id)

        obj.product = product
        obj.author = self.request.user

        obj.save()
        return super().form_valid(form)


class UserFavoritesView(LoginRequiredMixin, generic.ListView):
    template_name = 'products/favorites.html'
    context_object_name = 'favorites'

    def get_queryset(self):
        return self.request.user.favorites.all()


@login_required()
@require_POST
def add_product_to_user_favorites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_favorite_products = request.user.favorites.all()
    user_favorites_all_product_ids = [favorite_obj.product.id for favorite_obj in user_favorite_products]

    if product_id not in user_favorites_all_product_ids:

        Favorite.objects.create(user=request.user, product=product)
        messages.success(request, _('product successfully added to favorites'))
        return redirect('products_list')

    else:
        messages.error(request, _('this product is already in your favorites'))
        return redirect('products_list')


class DeleteProductFromUserFavoritesPostView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin,
                                             generic.DeleteView):
    model = Favorite
    http_method = ['post']
    success_url = reverse_lazy('favorites')
    success_message = _('product successfully deleted from your favorites')

    def test_func(self):
        return self.get_object().user == self.request.user
