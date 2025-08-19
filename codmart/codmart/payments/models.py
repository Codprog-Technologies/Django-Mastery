from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.

class OrderStatus(models.TextChoices):
    CREATED = "CREATED", "Created"
    CONFIRMED = "CONFIRMED", "Confirmed"
    DELIVERED = "DELIVERED", "Delivered"
    FAILED = "FAILED", "Failed"

class PaymentChannel(models.TextChoices):
    COD = "COD", "Cash On Delivery"
    ONLINE = "ONLINE", "Online Payment"


class Order(models.Model):

    address = models.ForeignKey("users.Address", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    product = models.ForeignKey("products.Product", on_delete=models.SET_NULL, null=True)

    payment_channel = models.CharField(max_length=10, choices=PaymentChannel)
    pg_id = models.CharField(max_length=50, blank=True)

    total_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=15, choices=OrderStatus)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
