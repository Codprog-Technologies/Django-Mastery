from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.utils.translation import gettext as _


# Create your models here.

class User(AbstractUser):
    class RoleChoices(models.TextChoices):
        BUYER = "BY", "Buyer"
        SELLER = "SL", "Seller"

    # username = None
    email = models.EmailField(_("email address"), blank=False, unique=True)
    dob = models.DateField(null=True, verbose_name=_("Date of Birth"))
    role = models.CharField(max_length=2, choices=RoleChoices, blank=True, verbose_name=_("role"))

    REQUIRED_FIELDS = ["email", "dob"]
    # USERNAME_FIELD = "email"


class Address(models.Model):
    name = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=50)
    address_line_2 = models.CharField(max_length=50)
    pincode = models.CharField(validators=[validators.MinLengthValidator(6),
                                           validators.MaxLengthValidator(6)])
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    phone_number = models.CharField(validators=[validators.RegexValidator(r'^\d{10}$')])