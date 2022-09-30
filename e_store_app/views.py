from django.shortcuts import render, get_object_or_404

from e_store_app.models import Product


# Create your views here.
def index_view(request):
    products = Product.objects.all().order_by('category__name', 'name')
    context = {'products': products}
    return render(request, 'index.html', context)


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context)



