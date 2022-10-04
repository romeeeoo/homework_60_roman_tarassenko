from django.forms import ModelForm

from e_store_app.models import Product



class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'picture_link',
            'category',
            'stock',
            'price'
        ]
