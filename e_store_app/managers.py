from django.db.models import Manager


class ProductManager(Manager):
    def all(self):
        return self.get_queryset().order_by('name', 'category__name')
