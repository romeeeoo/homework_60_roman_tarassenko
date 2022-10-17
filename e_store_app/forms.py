from django.forms import ModelForm
from django import forms

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


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")
