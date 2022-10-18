
from urllib.parse import urlencode

from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from e_store_app.models import Product
from e_store_app.forms import ProductForm, SimpleSearchForm



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

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

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











