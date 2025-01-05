from django.db import models


# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
