
from django.urls import path

from e_store_app.views import ProductToCart, ShopListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView


urlpatterns = [
    path("", ShopListView.as_view(), name="index"),
    path("products/", ShopListView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detailed"),
    path("products/add/", ProductCreateView.as_view(), name="add_product"),
    path("products/<int:pk>/update", ProductUpdateView.as_view(), name="update_product"),
    path("products/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
    path("products/<int:pk>/confirm-delete", ProductDeleteView.as_view(), name="product_confirm_delete"),
    path("products/<int:pk>/add-to-cart", ProductToCart.as_view(), name="add_product_to_cart"),
]
