from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _

from .models import Product, Comment, WishList, Category
from .forms import CommentForm


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/products_list_view.html'
    context_object_name = 'products'
    paginate_by = 9


def category_show_product_list(request, slugs):
    slugs = slugs.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [i.slug for i in category_queryset]
    parent = None
    for slug in all_slugs:
        if slug in all_slugs:
            parent = get_object_or_404(Category, slug=slug, parent=parent)
        else:
            instance = get_object_or_404(Product, slug=slug)
            breadcrumbs_link = instance.get_catg_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)


def product_detail_view(request, pk, slug):
    product = get_object_or_404(Product, pk=pk, slug=slug)
    print(product.category)
    print(product.get_catg_list()[-1])

    return render(request, 'products/products_detail_view.html', {'product': product, 'comment_form': CommentForm()})


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


class WishListView(LoginRequiredMixin, generic.ListView):
    template_name = 'products/wish_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        wish_list = self.request.user.wish_list.all()

        return [wish.product for wish in wish_list]


@require_POST
@login_required()
def add_product_to_wish_list(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_wish_list = request.user.wish_list.all()
    ids = [i['product_id'] for i in user_wish_list.values()]

    if product_id not in ids:

        WishList.objects.create(user=request.user, product=product)
        messages.success(request, _('product successfully added to wishlist'))
        return redirect('products_list')

    else:
        messages.error(request, _('this product is already in your wishlist'))
        return redirect('products_list')
