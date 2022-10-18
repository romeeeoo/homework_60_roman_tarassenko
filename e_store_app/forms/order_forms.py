from django import forms

from e_store_app.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "client_name",
            "client_phone",
            "client_address"
        ]
