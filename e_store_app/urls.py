
from django.urls import path

from e_store_app.views import index_view, product_view, add_view

urlpatterns = [
    path('', index_view, name='index'),
    path('products/', index_view, name='products'),
    path('products/<int:pk>/', product_view, name='product_detailed'),
    path('products/add/', add_view, name='add_product')
]
