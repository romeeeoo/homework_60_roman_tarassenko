from django.db import models


# Create your models here.

DEFAULT_STATUS_ID = 1


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True, blank=True)
    picture_link = models.TextField(null=True, blank=True, max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=DEFAULT_STATUS_ID)
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)









