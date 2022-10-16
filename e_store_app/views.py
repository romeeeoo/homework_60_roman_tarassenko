# from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from e_store_app.forms import ProductForm
from e_store_app.models import Product


# def index_view(request):
#     products = Product.objects.all().order_by('category__name', 'name')
#     context = {'products': products}
#     return render(request, 'index.html', context)


class ShopListView(ListView):
    template_name = "product/index.html"
    model = Product
    context_object_name = "products"
    paginate_by = 10
    paginate_orphans = 5

# def product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product_detailed.html', context)


class ProductDetailView(DetailView):
    template_name = "product/product_detailed.html"
    model = Product
    context_object_name = 'product'



# def add_view(request):
#     if request.method == 'GET':
#         form = ProductForm()
#         return render(request, 'add_product.html', context={'form': form})
#     elif request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             new_product = Product.objects.create(
#                 name=form.cleaned_data['name'],
#                 description=form.cleaned_data['description'],
#                 category=form.cleaned_data['category'],
#                 picture_link=form.cleaned_data['picture_link'],
#                 stock=form.cleaned_data['stock'],
#                 price=form.cleaned_data['price'],
#             )
#             return redirect("product_detailed", pk=new_product.pk)
#         else:
#             return render(request, 'add_product.html', context={'form': form})


class ProductCreateView(CreateView):
    template_name = "product/add_product.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product_detailed", kwargs={"pk": self.object.pk})

# def update_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product.name = form.cleaned_data['name']
#             product.description = form.cleaned_data['description']
#             product.category = form.cleaned_data['category']
#             product.picture_link = form.cleaned_data['picture_link']
#             product.stock = form.cleaned_data['stock']
#             product.price = form.cleaned_data['price']
#             product.save()
#             return redirect("product_detailed", pk=product.pk)
#     elif request.method == "GET":
#         form = ProductForm(instance=product)
#         return render(request, 'update_product.html', context={'form': form})


class ProductUpdateView(UpdateView):
    template_name = "product/update_product.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product_detailed", kwargs={"pk": self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = "product/product_confirm_delete.html"
    model = Product
    success_url = reverse_lazy("index")

