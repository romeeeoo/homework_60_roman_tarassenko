from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(to="Product", related_name="orders")
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=50)
    client_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.pk}. {self.client_name}"




