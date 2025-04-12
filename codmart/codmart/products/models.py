from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)


class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField()
