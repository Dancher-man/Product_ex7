from django.urls import path

from source.views.pruducts import ProductsListView, DetailProductView, CreateProductView, UpdateProductView, DeleteProductView
from source.views.reviews import CreateReviewView, UpdateReviewView, DeleteReviewView, ListNotModerateReviewsView

app_name = 'source'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('product/<int:pk>/', DetailProductView.as_view(), name='product_view'),
    path('product/create/', CreateProductView.as_view(), name='create_product'),
    path('product/update/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('product/delete/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
    path('product/<int:pk>/review/add/', CreateReviewView.as_view(), name='create_review'),
    path('review/<int:pk>/update/', UpdateReviewView.as_view(), name='update_review'),
    path('review/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete_review'),
    path('reviews/not_moderated/', ListNotModerateReviewsView.as_view(), name='not_moderated_reviews'),
]