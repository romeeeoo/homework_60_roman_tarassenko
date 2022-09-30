from django.shortcuts import render

from e_store_app.models import Product


# Create your views here.
def index_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)
