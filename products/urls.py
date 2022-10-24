from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    # path('catg/<slug:catg_slug>/', views.show_category, name='catg'),
    path('<int:pk>/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/add/<int:product_id>/', views.CommentCreateView.as_view(), name='comment create'),

    # wishlist
    path('favorites/', views.UserFavoritesView.as_view(), name='favorites'),
    path('favorites/add/<int:product_id>/', views.add_product_to_user_favorites, name='favorites_add'),
    path('favorites/delete/<int:pk>/', views.DeleteProductFromUserFavoritesPostView.as_view(), name='favorites_delete')

]
