from django.urls import path

from . import views

urlpatterns = [
    path('',views.PruductListView.as_view(),name='products_list'),
    path('<int:pk>/',views.ProductDetailView.as_view(),name='product_detail'),
    path('comment/add/<int:product_id>/', views.CommentCreateView.as_view(), name='comment create'),

]