from django.db import models


class Order(models.Model):
    products = models.ManyToManyField(to="Product", related_name="orders", through="ProductsOrders", through_fields=(
        "order", "product"), blank=False)
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=50)
    client_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.pk}. {self.client_name}"


class ProductsOrders(models.Model):
    product = models.ForeignKey(to="Product", on_delete=models.CASCADE)
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField(default=0)




