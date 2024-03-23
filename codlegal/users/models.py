from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    dob = models.DateField(null=True, verbose_name="Date of Birth")

    REQUIRED_FIELDS = ["email", "dob"]
