
from django.urls import path

from e_store_app.views import index_view, product_view

urlpatterns = [
    path('', index_view, name='index'),
    path('products/', index_view, name='products'),
    path('products/<int:pk>/', product_view, name='product_detailed'),
]
