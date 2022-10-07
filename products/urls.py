from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/add/<int:product_id>/', views.CommentCreateView.as_view(), name='comment create'),

    # wishlist
    path('wish_list/', views.WishListView.as_view(), name='wish_list'),
    path('wish_list/add/<int:product_id>/', views.add_product_to_wish_list, name='wish_list_add')

]
