from django.shortcuts import render, get_object_or_404, redirect

from e_store_app.forms import ProductForm
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


def add_view(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'add_product.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            new_product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                picture_link=form.cleaned_data['picture_link'],
                stock=form.cleaned_data['stock'],
                price=form.cleaned_data['price'],
            )
            return redirect("product_detailed", pk=new_product.pk)
        else:
            return render(request, 'add_product.html', context={'form': form})


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.picture_link = form.cleaned_data['picture_link']
            product.stock = form.cleaned_data['stock']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect("product_detailed", pk=product.pk)
    elif request.method == "GET":
        form = ProductForm(instance=product)
        return render(request, 'update_product.html', context={'form': form})