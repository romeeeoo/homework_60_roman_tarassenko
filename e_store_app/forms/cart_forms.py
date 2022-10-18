from django import forms

from e_store_app.models import CartProduct


class ProductToCartForm(forms.ModelForm):
    class Meta:
        model = CartProduct
        fields = [
            "product",
            "quantity",
        ]
