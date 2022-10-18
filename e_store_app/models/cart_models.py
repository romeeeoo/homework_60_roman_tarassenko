from django.db import models


class CartProduct(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{}".format(self.product)


