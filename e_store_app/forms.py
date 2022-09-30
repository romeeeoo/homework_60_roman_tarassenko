from django import forms
from django.forms import widgets

from e_store_app.models import Category


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    description = forms.CharField(max_length=2000, required=False, label='Description', widget=forms.Textarea)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    picture_link = forms.CharField(required=False, max_length=1000)
    stock = forms.IntegerField(min_value=0)
    price = forms.DecimalField(min_value=0.09, decimal_places=2, max_digits=7)
