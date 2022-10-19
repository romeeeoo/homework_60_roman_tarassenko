from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DeleteView

from e_store_app.forms.order_forms import OrderForm
from e_store_app.models import Product, CartProduct, ProductsOrders


class ProductToCart(View):

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs["pk"])
        try:
            product_in_cart = CartProduct.objects.get(product=product)
            if product.stock == 0:
                print("product finished")
            else:
                if product_in_cart.quantity < product.stock:
                    product_in_cart.quantity += 1
                    product_in_cart.save()
        except:
            # form = ProductToCartForm()
            product_in_cart = CartProduct.objects.create(product=product)
            # product_in_cart.product = product
            product_in_cart.quantity += 1
            product_in_cart.save()
        return redirect("index")


class CartWithProductView(TemplateView):
    template_name = "cart/cart_with_product_list.html"

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = OrderForm()
        context["form"] = form
        products_in_cart = CartProduct.objects.all()
        context["products_in_cart"] = products_in_cart
        total = 0
        for p in products_in_cart:
            total += p.quantity * p.product.price
        context["total"] = total
        return context


class DeleteProductFromCart(DeleteView):
    model = CartProduct
    success_url = reverse_lazy('cart')


class CreateOrderView(View):

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            products_in_cart = CartProduct.objects.all()
            for p in products_in_cart:
                ProductsOrders.objects.create(product=p.product, order=order, order_quantity=p.quantity)
            order.save()
            products_in_cart.delete()
            return redirect("index")










