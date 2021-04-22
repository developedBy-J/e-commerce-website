from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.get_products, name="products"),
    path('products/<str:pk>/', views.get_product, name="product"),
]