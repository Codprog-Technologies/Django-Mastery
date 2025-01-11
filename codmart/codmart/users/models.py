from django.contrib.auth.models import AbstractUser
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
